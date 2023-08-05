use std::collections::{btree_map::Entry, BTreeMap};

use anyhow::{anyhow, bail, Context, Result};
use circuit_base::{
    expand_node::{expand_node, ReplaceMapRc},
    module::has_sym,
    CircuitNode, CircuitRc, Module, ModuleArgSpec, ModuleSpec, Rearrange, Symbol,
};
use circuit_rewrites::{
    deep_rewrite::SimpFnSubset,
    module_rewrite::{extract_rewrite_raw, module_remove_unused_inputs},
};
use get_update_node::{AnyFound, IterativeMatcher, IterativeMatcherRc, MatcherData};
use macro_rules_attribute::apply;
use pyo3::{
    exceptions::{PyRuntimeError, PyValueError},
    prelude::*,
    PyObject,
};
use rr_util::{
    cached_method,
    eq_by_big_hash::EqByBigHash,
    fn_struct, impl_eq_by_big_hash, pycall, python_error_exception,
    rearrange_spec::{OpSize, RearrangeSpec, RearrangeSpecError},
    sv,
    util::{DimNumMaker, HashBytes},
};
use rustc_hash::{FxHashMap as HashMap, FxHashSet as HashSet};
use thiserror::Error;

#[pyfunction(
    prefix_to_strip = "None",
    module_name = "None",
    check_all_args_present = "true",
    check_unique_arg_names = "true",
    circuit_to_arg_spec = "None"
)]
pub fn extract_rewrite(
    circuit: CircuitRc,
    matcher: IterativeMatcherRc,
    prefix_to_strip: Option<String>,
    module_name: Option<String>,
    check_all_args_present: bool,
    check_unique_arg_names: bool,
    circuit_to_arg_spec: Option<PyObject>,
) -> Result<Module> {
    let edges: Vec<CircuitRc> = matcher.get(circuit.clone(), false)?.into_iter().collect();
    let mut specs: Vec<(CircuitRc, ModuleArgSpec)> = edges
        .into_iter()
        .map(|n| {
            if let Some(cts) = &circuit_to_arg_spec {
                pycall!(cts, (n.clone(),), anyhow)
            } else {
                Ok(ModuleArgSpec::just_name_shape(n.clone(), true, true, false))
            }
            .map(|z| (n, z))
        })
        .collect::<Result<Vec<_>>>()?;
    specs.sort_by_key(|x| x.1.symbol.name_cloned());
    extract_rewrite_raw(
        circuit,
        specs,
        prefix_to_strip,
        module_name,
        check_all_args_present,
        check_unique_arg_names,
    )
}

#[pyclass]
#[derive(Debug, Clone)]
pub struct BindItem {
    #[pyo3(get, set)]
    pub matcher: IterativeMatcherRc,
    #[pyo3(get, set)]
    pub input_circuit: CircuitRc,
    #[pyo3(get, set)]
    pub batchable: bool,
    #[pyo3(get, set)]
    pub expandable: bool,
    #[pyo3(get, set)]
    pub ban_non_symbolic_size_expand: bool,
}

#[pymethods]
impl BindItem {
    #[new]
    #[args(
        batchable = "ModuleArgSpec::default().batchable",
        expandable = "ModuleArgSpec::default().expandable",
        ban_non_symbolic_size_expand = "ModuleArgSpec::default().ban_non_symbolic_size_expand"
    )]
    fn new(
        matcher: IterativeMatcherRc,
        input_circuit: CircuitRc,
        batchable: bool,
        expandable: bool,
        ban_non_symbolic_size_expand: bool,
    ) -> Self {
        Self {
            matcher,
            input_circuit,
            batchable,
            expandable,
            ban_non_symbolic_size_expand,
        }
    }
}

impl Binder {
    fn into_item(self) -> BindItem {
        match self {
            Self::Tup(matcher, input_circuit) => BindItem {
                matcher,
                input_circuit,
                batchable: ModuleArgSpec::default().batchable,
                expandable: ModuleArgSpec::default().expandable,
                ban_non_symbolic_size_expand: ModuleArgSpec::default().ban_non_symbolic_size_expand,
            },
            Self::Item(item) => item,
        }
    }
}

#[derive(Debug, FromPyObject)]
pub enum Binder {
    Tup(IterativeMatcherRc, CircuitRc),
    Item(BindItem),
}

#[pyfunction(binders = "*", check_unique_arg_names = "true", name = "None")]
pub fn module_new_bind(
    spec_circuit: CircuitRc,
    binders: Vec<Binder>,
    check_unique_arg_names: bool,
    name: Option<String>,
) -> Result<Module> {
    let (nodes, arg_specs) = binders
        .into_iter()
        .map(|binder| {
            let BindItem {
                matcher,
                input_circuit,
                batchable,
                expandable,
                ban_non_symbolic_size_expand,
            } = binder.into_item();
            let matched_circuit =
                matcher
                    .get_unique(spec_circuit.clone(), false)
                    .context(format!(
                        "failed to get unique for matcher={} in bind",
                        *matcher
                    ))?;

            let symbol = matched_circuit.as_symbol().cloned().ok_or_else(|| {
                ModuleBindError::ExpectedSymbol {
                    matched_circuit,
                    matcher,
                    spec_circuit: spec_circuit.clone(),
                }
            })?;

            Ok((
                input_circuit,
                ModuleArgSpec {
                    symbol,
                    batchable,
                    expandable,
                    ban_non_symbolic_size_expand,
                },
            ))
        })
        .collect::<Result<Vec<_>>>()?
        .into_iter()
        .unzip();

    Module::try_new(
        nodes,
        ModuleSpec::new(spec_circuit, arg_specs, true, check_unique_arg_names)?,
        name,
    )
}

#[apply(python_error_exception)]
#[base_error_name(ModuleBind)]
#[base_exception(PyRuntimeError)]
#[derive(Error, Debug, Clone)]
pub enum ModuleBindError {
    #[error("expected to match symbol, matched_circuit={matched_circuit:?}\nfor matcher={matcher:?}\nspec_circuit={spec_circuit:?}\n({e_name})")]
    ExpectedSymbol {
        matched_circuit: CircuitRc,
        matcher: IterativeMatcherRc,
        spec_circuit: CircuitRc,
    },
}

/// args are outer to inner
pub fn fuse_modules_impl(
    orig_modules: &[Module],
    new_nodes: &[Vec<CircuitRc>],
) -> Result<Vec<(CircuitRc, ModuleArgSpec)>> {
    // reverse to get inner shapes inside of outer
    let batch_shapes_per_mod: Vec<_> = orig_modules
        .into_iter()
        .map(|m| m.aligned_batch_shape())
        .collect();
    let cumulative_batch_shapes = batch_shapes_per_mod
        .iter()
        .rev()
        .scan(vec![], |state, sh| {
            let old_state = state.clone();
            state.extend(sh.iter().cloned());
            Some(old_state)
        })
        .collect::<Vec<_>>()
        .into_iter()
        .rev(); // reverse again

    let out: Vec<_> = new_nodes
        .into_iter()
        .zip(cumulative_batch_shapes)
        .zip(orig_modules)
        .zip(batch_shapes_per_mod)
        .map(|(((items, cum_batch_shape), m), overall_mod_batch_shape)| {
            (*items)
                .to_owned()
                .into_iter()
                .zip(&m.nodes)
                .zip(m.spec.arg_specs.clone())
                .zip(m.spec.batch_shapes(&m.nodes))
                .map(|(((node, orig_node), arg_spec), orig_batch_shape)| {
                    let missing_ndims = overall_mod_batch_shape.len() - orig_batch_shape.len();
                    let non_batch = orig_node.ndim() - orig_batch_shape.len();
                    let extra_dims = node.ndim() - orig_node.ndim();
                    let any_batching = extra_dims > 0 || orig_batch_shape.len() > 0;
                    let needs_pad_orig = missing_ndims > 0 && extra_dims > 0;
                    let new_node = if (any_batching && cum_batch_shape.len() > 0) || needs_pad_orig
                    {
                        let mut maker = DimNumMaker::default();
                        let same_outer = maker.next_range(extra_dims);
                        let pad_for_orig = if needs_pad_orig {
                            maker.next_range(missing_ndims)
                        } else {
                            0..0
                        };
                        let same_orig_batch = maker.next_range(orig_batch_shape.len());
                        let cum = maker.next_range(cum_batch_shape.len());
                        let same_non_batch = maker.next_range(non_batch);

                        if maker.running > u8::MAX as usize {
                            bail!(anyhow!(RearrangeSpecError::LenShapeTooLarge {
                                len_shape: maker.running
                            })
                            .context("too many dims in fuse module for flatten"));
                        }

                        let mut sizes = sv![OpSize::NONE; maker.running];
                        for i in pad_for_orig.clone() {
                            sizes[i] = Some(overall_mod_batch_shape[i - pad_for_orig.start]).into();
                        }
                        for i in cum.clone() {
                            sizes[i] = Some(cum_batch_shape[i - cum.start]).into();
                        }

                        let spec = RearrangeSpec::new(
                            same_outer
                                .clone()
                                .chain(same_orig_batch.clone())
                                .chain(same_non_batch.clone())
                                .map(|i| sv![i as u8])
                                .collect(),
                            same_outer
                                .chain(pad_for_orig)
                                .chain(same_orig_batch)
                                .chain(cum)
                                .chain(same_non_batch.clone())
                                .map(|i| sv![i as u8])
                                .collect(),
                            sizes,
                        )
                        .unwrap();

                        let rep_name = node.name().map(|x| format!("{} rep_fuse", x));
                        Rearrange::nrc(node, spec, rep_name)
                    } else {
                        node
                    };
                    Ok((new_node, arg_spec))
                })
                .collect::<Result<Vec<_>>>()
        })
        .collect::<Result<Vec<_>>>()?
        .into_iter()
        .flatten()
        .collect();

    // resolve all references
    let out = out
        .into_iter()
        .scan(
            HashMap::<_, CircuitRc>::default(),
            |sym_map, (circ, arg_spec)| {
                let circ = if let Some(circ) = sym_map.get(&arg_spec.symbol) {
                    circ.clone()
                } else {
                    circ
                };

                sym_map.insert(arg_spec.symbol.clone(), circ.clone());

                Some((circ, arg_spec))
            },
        )
        .collect();

    Ok(out)
}

#[derive(Debug, Clone)]
struct NestedModuleItems {
    modules: Vec<Module>,
    new_nodes: Vec<Vec<CircuitRc>>,
    flat: Vec<(CircuitRc, ModuleArgSpec)>,
    flat_sym_to_arg: HashMap<Symbol, CircuitRc>,
    hash: HashBytes,
}

impl Default for NestedModuleItems {
    fn default() -> Self {
        Self::new(vec![], vec![]).unwrap()
    }
}

impl NestedModuleItems {
    fn new(modules: Vec<Module>, new_nodes: Vec<Vec<CircuitRc>>) -> Result<Self> {
        let flat = fuse_modules_impl(&modules, &new_nodes)?;
        let flat_sym_to_arg = flat
            .iter()
            .map(|(circ, arg_spec)| (arg_spec.symbol.clone(), circ.clone()))
            .collect();

        let mut hasher = blake3::Hasher::new();

        for (m, this_new_nodes) in modules.iter().zip(&new_nodes) {
            for n in this_new_nodes {
                hasher.update(&n.hash());
            }
            hasher.update(&m.hash());
        }

        Ok(Self {
            modules,
            new_nodes,
            flat,
            flat_sym_to_arg,
            hash: hasher.finalize().into(),
        })
    }

    fn push(&self, m: Module, this_new_nodes: Vec<CircuitRc>) -> Result<Self> {
        let mut modules = self.modules.clone();
        let mut new_nodes = self.new_nodes.clone();
        modules.push(m);
        new_nodes.push(this_new_nodes);
        Self::new(modules, new_nodes)
    }
}

impl EqByBigHash for NestedModuleItems {
    fn hash(&self) -> HashBytes {
        self.hash
    }
}
impl_eq_by_big_hash!(NestedModuleItems);

// inner to outer
// NOTE: this is reverse order from how we store in NestedModuleItems!!!
fn_struct!(
    pub NestedModuleNamer: Fn(
        base_circuit: CircuitRc,
        running_circuit: CircuitRc,
        modules: Vec<Module>
    ) -> Option<String>
);

#[pyfunction]
pub fn default_nested_module_namer() -> NestedModuleNamer {
    Default::default()
}

impl Default for NestedModuleNamer {
    fn default() -> Self {
        NestedModuleNamer::Dyn(NestedModuleNamerDynStruct(std::sync::Arc::new(
            |base_circuit, _, modules| {
                if modules.is_empty() {
                    return Ok(base_circuit.name_cloned());
                }

                if base_circuit.name().is_none() || modules.iter().any(|m| m.name().is_none()) {
                    return Ok(None);
                }

                Ok(Some(format!(
                    "{} bind:{}",
                    base_circuit.name().unwrap(),
                    modules
                        .iter()
                        .map(|x| x.name().unwrap())
                        .collect::<Vec<_>>()
                        .join(",")
                )))
            },
        )))
    }
}

#[pyclass]
#[derive(Debug, Clone)]
pub struct ModulePusher {
    #[pyo3(get)]
    flatten_modules: bool,
    #[pyo3(get)]
    remove_unused_inputs: bool,
    #[pyo3(get)]
    elim_no_input_modules: bool,
    #[pyo3(get)]
    bind_encountered_symbols: bool,
    #[pyo3(get)]
    namer: NestedModuleNamer,
    any_found: AnyFound,
    cache: cached::UnboundCache<
        (
            HashBytes,
            IterativeMatcherRc,
            IterativeMatcherRc,
            bool,
            HashBytes,
            HashBytes,
        ),
        (CircuitRc, HashSet<CircuitRc>),
    >,
    replace_expand_cache: cached::UnboundCache<(HashBytes, HashBytes), CircuitRc>,
}

impl Default for ModulePusher {
    fn default() -> Self {
        Self {
            flatten_modules: true,
            remove_unused_inputs: true,
            elim_no_input_modules: true,
            bind_encountered_symbols: true,
            namer: Default::default(),
            any_found: Default::default(),
            cache: cached::UnboundCache::new(),
            replace_expand_cache: cached::UnboundCache::new(),
        }
    }
}

#[pymethods]
impl ModulePusher {
    #[new]
    #[args(
        flatten_modules = "Self::default().flatten_modules",
        remove_unused_inputs = "Self::default().remove_unused_inputs",
        elim_no_input_modules = "Self::default().elim_no_input_modules",
        bind_encountered_symbols = "Self::default().bind_encountered_symbols",
        namer = "Self::default().namer"
    )]
    pub fn new(
        flatten_modules: bool,
        remove_unused_inputs: bool,
        elim_no_input_modules: bool,
        bind_encountered_symbols: bool,
        namer: NestedModuleNamer,
    ) -> Self {
        Self {
            flatten_modules,
            remove_unused_inputs,
            elim_no_input_modules,
            bind_encountered_symbols,
            namer,
            ..Default::default()
        }
    }

    #[args(skip_module = "MatcherData::Always(false).into()", is_get = "true")]
    pub fn push_down_modules_get(
        &mut self,
        circuit: CircuitRc,
        get: IterativeMatcherRc,
        skip_module: IterativeMatcherRc,
        is_get: bool,
    ) -> Result<(CircuitRc, HashSet<CircuitRc>)> {
        self.push_down_modules_rec(
            circuit,
            get,
            skip_module,
            is_get,
            &Default::default(),
            &Default::default(),
        )
    }

    #[args(skip_module = "MatcherData::Always(false).into()")]
    fn __call__(
        &mut self,
        _py: Python<'_>,
        circuit: CircuitRc,
        traversal: IterativeMatcherRc,
        skip_module: IterativeMatcherRc,
    ) -> Result<CircuitRc> {
        self.push_down_modules(circuit, traversal, skip_module)
    }

    #[args(skip_module = "MatcherData::Always(false).into()")]
    pub fn push_down_modules(
        &mut self,
        circuit: CircuitRc,
        traversal: IterativeMatcherRc,
        skip_module: IterativeMatcherRc,
    ) -> Result<CircuitRc> {
        self.push_down_modules_get(circuit, traversal, skip_module, false)
            .map(|x| x.0)
    }

    // TODO: fancy validate
    #[args(skip_module = "MatcherData::Always(false).into()")]
    pub fn get_push_down_modules(
        &mut self,
        circuit: CircuitRc,
        get: IterativeMatcherRc,
        skip_module: IterativeMatcherRc,
    ) -> Result<HashSet<CircuitRc>> {
        self.push_down_modules_get(circuit, get, skip_module, true)
            .map(|x| x.1)
    }

    #[args(skip_module = "MatcherData::Always(false).into()")]
    pub fn get_unique_op_push_down_modules(
        &mut self,
        circuit: CircuitRc,
        get: IterativeMatcherRc,
        skip_module: IterativeMatcherRc,
    ) -> Result<Option<CircuitRc>> {
        let out = self.get_push_down_modules(circuit, get, skip_module)?;
        if out.len() > 1 {
            bail!("found {} matches which is > 1", out.len());
        }
        Ok(out.into_iter().next())
    }

    #[args(skip_module = "MatcherData::Always(false).into()")]
    pub fn get_unique_push_down_modules(
        &mut self,
        circuit: CircuitRc,
        get: IterativeMatcherRc,
        skip_module: IterativeMatcherRc,
    ) -> Result<CircuitRc> {
        self.get_unique_op_push_down_modules(circuit, get, skip_module)?
            .ok_or_else(|| anyhow!("found no matches!"))
    }
}

impl ModulePusher {
    #[apply(cached_method)]
    #[self_id(self_)]
    #[key((circuit.info().hash,  get.clone(), skip_module.clone(), is_get, items.hash(), extra_replacements.hash()))]
    #[use_try]
    #[cache_expr(cache)]
    fn push_down_modules_rec(
        &mut self,
        circuit: CircuitRc,
        get: IterativeMatcherRc,
        skip_module: IterativeMatcherRc,
        is_get: bool,
        items: &NestedModuleItems,
        extra_replacements: &ReplaceMapRc,
    ) -> Result<(CircuitRc, HashSet<CircuitRc>)> {
        if let Some(arg) = circuit
            .as_symbol()
            .and_then(|sym| items.flat_sym_to_arg.get(sym))
        {
            if !self_.bind_encountered_symbols {
                bail!(PushDownModuleError::PushPastPreviouslyBoundSymbol {
                    symbol: circuit.as_symbol().unwrap().clone()
                })
            }
            return Ok((arg.clone(), Default::default()));
        }
        if let Some(out) = extra_replacements.get(&circuit) {
            return Ok((out.clone(), Default::default()));
        }

        let (new_get, found_get) = get
            .match_iterate(circuit.clone())?
            .unwrap_or_same(get.clone());
        let all_done = new_get.all_finished()
            || (is_get && !self_.any_found.are_any_found(circuit.clone(), get)?);

        let mut get_fin = || self_.finalize(circuit.clone(), items, extra_replacements);
        let mut out_set = HashSet::default();

        let finalized = if is_get && found_get {
            let out = get_fin()?;
            out_set.insert(out.clone());
            Some(out)
        } else {
            None
        };

        if all_done {
            let out = if let Some(fin) = finalized {
                // avoid recomputation
                fin
            } else {
                get_fin()?
            };
            return Ok((out, out_set));
        }

        let new_get = new_get.per_child_with_term(circuit.num_children());

        let (new_skip_module, found_skip_module) = skip_module
            .match_iterate(circuit.clone())?
            .unwrap_or_same(skip_module);
        let new_skip_module = new_skip_module.per_child_with_term(circuit.num_children());

        let mut rec = |self_: &mut Self, c, get, skip, items, extra_replacements: &_| {
            let (out, new_set) =
                self_.push_down_modules_rec(c, get, skip, is_get, items, extra_replacements)?;
            if is_get {
                out_set.extend(new_set);
            }
            Ok(out)
        };

        let out = if let Some(m) = circuit
            .as_module()
            .and_then(|x| (!found_skip_module).then_some(x))
        {
            let mut new_iter = new_get.into_iter().zip(new_skip_module);
            let (spec_circuit_get, spec_circuit_skip_module) = new_iter.next().unwrap();
            let node_get_skip: Vec<_> = new_iter.collect();
            assert_eq!(node_get_skip.len(), m.nodes.len());

            let new_nodes = m
                .nodes
                .clone()
                .into_iter()
                .zip(node_get_skip)
                .map(|(c, (get, skip))| rec(self_, c, get, skip, items, extra_replacements))
                .collect::<Result<Vec<_>>>()?;

            rec(
                self_,
                m.spec.circuit.clone(),
                spec_circuit_get,
                spec_circuit_skip_module,
                &items.push(m.clone(), new_nodes)?,
                extra_replacements,
            )?
        } else {
            let new_children = circuit
                .children()
                .into_iter()
                .zip(new_get.clone())
                .zip(new_skip_module.clone())
                .map(|((c, get), skip)| rec(self_, c, get, skip, items, extra_replacements))
                .collect::<Result<Vec<_>>>()?;

            expand_node(circuit.clone(), &new_children, |c, rep, child_idx| {
                let rep = ReplaceMapRc::new(
                    extra_replacements
                        .iter()
                        .map(|(a, b)| (a.clone(), b.clone()))
                        .chain(rep)
                        .collect(),
                );
                rec(
                    self_,
                    c,
                    new_get[child_idx].clone(),
                    new_skip_module[child_idx].clone(),
                    items,
                    &rep,
                )
            })
            // maybe we're supposed to just panic on rearrange rank errors?
            .context(concat!(
                "expand fail in push down modules, should be rearrange ",
                "overflow error (otherwise internal error)"
            ))?
        };

        // rename if we didn't create new
        let out = if out != circuit {
            let new_name = self_
                .namer
                .call(
                    circuit.clone(),
                    circuit.clone(),
                    items.modules.iter().rev().cloned().collect(),
                )
                .context("namer failed in push down module")?;
            out.rename(new_name)
        } else {
            out
        };

        Ok((out, out_set))
    }

    fn finalize(
        &mut self,
        circuit: CircuitRc,
        items: &NestedModuleItems,
        extra_replacements: &ReplaceMapRc,
    ) -> Result<CircuitRc> {
        let finished_circuit = self.finish_replace_expand(circuit.clone(), extra_replacements)?;
        let rep_expand_extra_dims = finished_circuit.ndim() - circuit.ndim();

        let mut updated_extra_replacements = (**extra_replacements).clone();
        let mut update_flat = |flat: Vec<(CircuitRc, ModuleArgSpec)>, extra_dims_here| -> Vec<_> {
            // compare to conform_to_input_batch_shape in Module
            flat.into_iter()
                .map(|(c, arg_spec)| {
                    let current_batch_shape = &c.shape()[..c.ndim() - arg_spec.symbol.ndim()];
                    let batch_start = current_batch_shape.len().saturating_sub(extra_dims_here);
                    if batch_start == current_batch_shape.len() {
                        return (c, arg_spec);
                    }

                    let new_sym = Symbol::new(
                        current_batch_shape[batch_start..]
                            .iter()
                            .chain(arg_spec.symbol.shape())
                            .copied()
                            .collect(),
                        arg_spec.symbol.uuid.clone(),
                        arg_spec.symbol.name_cloned(),
                    );

                    let orig_sim = arg_spec.symbol.clone();

                    updated_extra_replacements.insert(orig_sim.rc(), new_sym.crc());

                    (
                        c,
                        ModuleArgSpec {
                            symbol: new_sym,
                            ..arg_spec
                        },
                    )
                })
                .collect()
        };

        if self.flatten_modules {
            let (finished_circuit, new_flat) = if rep_expand_extra_dims > 0 {
                // if we have extra dims, we have to pull the symbols and resub to sync up batching
                let new_flat = update_flat(items.flat.clone(), rep_expand_extra_dims);
                let new_finished_circuit = self.finish_replace_expand(
                    circuit.clone(),
                    &ReplaceMapRc::new(updated_extra_replacements),
                )?;
                (new_finished_circuit, new_flat)
            } else {
                (finished_circuit, items.flat.clone())
            };

            self.build_module_flat(
                finished_circuit.clone(),
                finished_circuit,
                new_flat,
                items.modules.clone().into_iter().rev().collect(),
            )
        } else {
            let (finished_circuit, rev_nested) = if rep_expand_extra_dims > 0 {
                // if we have extra dims, we have to pull the symbols and resub to sync up batching
                let rev_nested: Vec<_> = items
                    .modules
                    .clone()
                    .into_iter()
                    .rev()
                    .scan(0, |prev_dims_covered, m| {
                        let extra_dims_here =
                            rep_expand_extra_dims.saturating_sub(*prev_dims_covered);
                        *prev_dims_covered += m.aligned_batch_shape().len();
                        Some(update_flat(m.arg_items(), extra_dims_here))
                    })
                    .collect();
                let new_finished_circuit = self.finish_replace_expand(
                    circuit.clone(),
                    &ReplaceMapRc::new(updated_extra_replacements),
                )?;
                (new_finished_circuit, rev_nested)
            } else {
                (
                    finished_circuit,
                    items
                        .modules
                        .clone()
                        .into_iter()
                        .rev()
                        .map(|m| m.arg_items())
                        .collect(),
                )
            };

            self.build_module_nested(finished_circuit, rev_nested, items.modules.clone())
        }
    }

    fn build_module_flat(
        &mut self,
        base_circuit: CircuitRc, // just for naming
        circuit: CircuitRc,
        flat: Vec<(CircuitRc, ModuleArgSpec)>,
        rev_modules: Vec<Module>,
    ) -> Result<CircuitRc> {
        let (nodes, arg_specs) = flat.into_iter().unzip();
        let name = self
            .namer
            .call(base_circuit, circuit.clone(), rev_modules)
            .context("namer failed in push down module")?;
        let m_out = Module::new(nodes, ModuleSpec { circuit, arg_specs }, name.clone());
        if self.remove_unused_inputs {
            module_remove_unused_inputs(&m_out, self.elim_no_input_modules)
        } else {
            Ok(m_out.rc())
        }
    }

    fn build_module_nested(
        &mut self,
        base_circuit: CircuitRc,
        rev_nested: Vec<Vec<(CircuitRc, ModuleArgSpec)>>,
        modules: Vec<Module>,
    ) -> Result<CircuitRc> {
        if modules.is_empty() {
            return Ok(base_circuit.clone());
        }
        let cum_rev_mods = modules
            .clone()
            .into_iter()
            .rev()
            .scan(vec![], |state, new_mod| {
                state.push(new_mod);
                Some(state.clone())
            });

        rev_nested.into_iter().zip(cum_rev_mods).fold(
            Ok(base_circuit.clone()),
            |circuit, (arg_items, running_modules)| {
                self.build_module_flat(base_circuit.clone(), circuit?, arg_items, running_modules)
            },
        )
    }

    #[apply(cached_method)]
    #[self_id(self_)]
    #[key((circuit.info().hash,  extra_replacements.hash()))]
    #[use_try]
    #[cache_expr(replace_expand_cache)]
    fn finish_replace_expand(
        &mut self,
        circuit: CircuitRc,
        extra_replacements: &ReplaceMapRc,
    ) -> Result<CircuitRc> {
        if extra_replacements.is_empty() {
            return Ok(circuit);
        }
        if let Some(out) = extra_replacements.get(&circuit) {
            return Ok(out.clone());
        }
        let new_args = circuit
            .children()
            .map(|c| self_.finish_replace_expand(c, &extra_replacements))
            .collect::<Result<_>>()?;
        expand_node(circuit, &new_args, |c, rep, _child_idx| {
            self_.finish_replace_expand(
                c,
                &ReplaceMapRc::new(
                    extra_replacements
                        .iter()
                        .map(|(a, b)| (a.clone(), b.clone()))
                        .chain(rep)
                        .collect(),
                ),
            )
        })
    }
}

struct SymbolExtractor {
    cache:
        cached::UnboundCache<HashBytes, (CircuitRc, BTreeMap<Symbol, (CircuitRc, ModuleArgSpec)>)>,
    conform_batch_if_needed: bool,
    symbols: HashSet<Symbol>,
}

impl Default for SymbolExtractor {
    fn default() -> Self {
        Self {
            cache: cached::UnboundCache::new(),
            conform_batch_if_needed: false,
            symbols: Default::default(),
        }
    }
}

impl SymbolExtractor {
    #[apply(cached_method)]
    #[self_id(self_)]
    #[key(circ.info().hash)]
    #[use_try]
    #[cache_expr(cache)]
    fn extract_symbols_rec(
        &mut self,
        circ: CircuitRc,
    ) -> Result<(CircuitRc, BTreeMap<Symbol, (CircuitRc, ModuleArgSpec)>)> {
        let mut out_syms = BTreeMap::default();
        let add_sym_circ = |out_syms: &mut BTreeMap<_, (CircuitRc, ModuleArgSpec)>,
                            arg_spec: ModuleArgSpec,
                            circ| {
            match out_syms.entry(arg_spec.symbol.clone()) {
                Entry::Occupied(entry) => {
                    if &entry.get().0 != &circ {
                        bail!(ExtractSymbolsError::BoundInputInconsistent {
                            symbol: arg_spec.symbol,
                            old_bound: entry.get().0.clone(),
                            new_bound: circ
                        })
                    }
                    if &entry.get().1 != &arg_spec {
                        bail!(ExtractSymbolsError::ArgSpecInconsistent {
                            old_arg_spec: entry.get().1.clone(),
                            new_arg_spec: arg_spec
                        })
                    }
                }
                Entry::Vacant(entry) => {
                    entry.insert((circ, arg_spec));
                }
            }
            Ok(())
        };

        let circ = if let Some(m) = circ.as_module() {
            let new_mod = if self_.conform_batch_if_needed {
                let batch = m
                    .nodes
                    .iter()
                    .zip(&m.spec.arg_specs)
                    .filter_map(|(node, arg_spec)| {
                        assert!(node.ndim() >= arg_spec.symbol.ndim());
                        self_
                            .symbols
                            .contains(&arg_spec.symbol)
                            .then_some(node.ndim() - arg_spec.symbol.ndim())
                    })
                    .max();
                batch.map(|dims| m.conform_to_input_batch_shape(Some(dims)).unwrap())
            } else {
                None
            };
            let new_m = new_mod.as_ref().unwrap_or(m);
            let (nodes, arg_specs): (Vec<_>, Vec<_>) = new_m
                .arg_items()
                .into_iter()
                .zip(&m.spec.arg_specs)
                .filter_map(|((node, arg_spec), orig_arg_spec)| {
                    if !self_.symbols.contains(&orig_arg_spec.symbol) {
                        return Some(Ok((node, arg_spec)));
                    }
                    if node.ndim() > arg_spec.symbol.ndim() {
                        assert!(!self_.conform_batch_if_needed); // this should have been handled
                        return Some(Err(ExtractSymbolsError::BatchedInput {
                            node_ndim: node.ndim(),
                            symbol_ndim: arg_spec.symbol.ndim(),
                            symbol: arg_spec.symbol.clone(),
                            node,
                        }
                        .into()));
                    }
                    if let Err(e) = add_sym_circ(&mut out_syms, arg_spec, node) {
                        return Some(Err(e));
                    }
                    None
                })
                .collect::<Result<Vec<_>>>()?
                .into_iter()
                .unzip();
            if nodes.len() == m.nodes.len() {
                m.crc()
            } else {
                Module::nrc(
                    nodes,
                    ModuleSpec {
                        circuit: new_m.spec.circuit.clone(),
                        arg_specs,
                    },
                    m.name().map(|s| format!("{} extracted", s)),
                )
            }
        } else {
            circ
        };

        let new_circ = circ.map_children(|c| {
            let (new, map) = self_.extract_symbols_rec(c)?;
            for (_, (circ, arg_spec)) in map {
                add_sym_circ(&mut out_syms, arg_spec, circ)?;
            }
            Ok(new)
        })?;

        if let Some(m) = circ.as_module() {
            for (sym, (bound_input, _)) in &out_syms {
                for arg_spec in &m.spec.arg_specs {
                    if has_sym(bound_input, &arg_spec.symbol) {
                        bail!(ExtractSymbolsError::HasBindingFromOuterModule {
                            bound_input: bound_input.clone(),
                            symbol: sym.clone(),
                            outer_symbol: arg_spec.symbol.clone()
                        })
                    }
                }
            }
        }

        Ok((new_circ, out_syms))
    }
}

#[pyfunction(use_elim_no_input_modules = "true", conform_batch_if_needed = "false")]
pub fn extract_symbols(
    circuit: CircuitRc,
    symbols: HashSet<Symbol>,
    use_elim_no_input_modules: bool,
    conform_batch_if_needed: bool,
) -> Result<Module> {
    let name = circuit.name_cloned();
    let (extracted_circ, extracted_syms) = SymbolExtractor {
        symbols,
        conform_batch_if_needed,
        ..Default::default()
    }
    .extract_symbols_rec(circuit)?;

    let extracted_circ = if use_elim_no_input_modules {
        SimpFnSubset::none()
            .include(vec!["elim_no_input_module".to_owned()])
            .unwrap()
            .simp(extracted_circ)
    } else {
        extracted_circ
    };

    let (nodes, arg_specs) = extracted_syms.into_values().unzip();

    Ok(Module::new(
        nodes,
        ModuleSpec {
            circuit: extracted_circ,
            arg_specs,
        },
        name,
    ))
}

#[pyfunction(use_elim_no_input_modules = "true", conform_batch_if_needed = "false")]
pub fn extract_symbols_get(
    circuit: CircuitRc,
    get: IterativeMatcherRc,
    use_elim_no_input_modules: bool,
    conform_batch_if_needed: bool,
) -> Result<Module> {
    let syms = get
        .get(circuit.clone(), false)
        .context("get failed in extract symbols")?
        .into_iter()
        .map(|x| {
            x.as_symbol().cloned().ok_or_else(|| {
                ExtractSymbolsError::GetFoundNonSymbol {
                    circ: x,
                    get: (**get).clone(),
                }
                .into()
            })
        })
        .collect::<Result<_>>()?;
    extract_symbols(
        circuit,
        syms,
        use_elim_no_input_modules,
        conform_batch_if_needed,
    )
}

#[apply(python_error_exception)]
#[base_error_name(PushDownModule)]
#[base_exception(PyValueError)]
#[derive(Error, Debug, Clone)]
pub enum PushDownModuleError {
    #[error("the encountered symbol={symbol:?} was bound by a pushed module, but bind_encountered_symbols is false ({e_name})")]
    PushPastPreviouslyBoundSymbol { symbol: Symbol },
}

#[apply(python_error_exception)]
#[base_error_name(ExtractSymbols)]
#[base_exception(PyValueError)]
#[derive(Error, Debug, Clone)]
pub enum ExtractSymbolsError {
    #[error("non-symbol={circ:?} (get={get}) ({e_name})")]
    GetFoundNonSymbol {
        circ: CircuitRc,
        get: IterativeMatcher,
    },

    #[error("node_ndim={node_ndim}>symbol_ndim={symbol_ndim} which implies batching\n{}\nsymbol={symbol:?} node={node:?} ({e_name})",
        concat!("batched inputs aren't handled by default (at the momement) but ",
        "can be handled by conforming the module to the batch shape.",
        "\nIf you want this to be done automatically, pass conform_batch_if_needed=true.")
        )]
    BatchedInput {
        node_ndim: usize,
        symbol_ndim: usize,
        symbol: Symbol,
        node: CircuitRc,
    },

    #[error("old_arg_spec={old_arg_spec:?} != new_arg_spec={new_arg_spec:?} ({e_name})")]
    ArgSpecInconsistent {
        old_arg_spec: ModuleArgSpec,
        new_arg_spec: ModuleArgSpec,
    },

    #[error("for symbol={symbol:?} old_bound={old_bound:?} != new_bound={new_bound:?} ({e_name})")]
    BoundInputInconsistent {
        symbol: Symbol,
        old_bound: CircuitRc,
        new_bound: CircuitRc,
    },

    #[error("the bound_input={bound_input:?} (for symbol={symbol:?}) contains outer_symbol={outer_symbol:?} which is bound by an outer module ({e_name})")]
    HasBindingFromOuterModule {
        bound_input: CircuitRc,
        symbol: Symbol,
        outer_symbol: Symbol,
    },
}
