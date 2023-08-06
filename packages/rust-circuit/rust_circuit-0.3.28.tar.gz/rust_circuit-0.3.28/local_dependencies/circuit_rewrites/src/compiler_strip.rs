use circuit_base::{deep_map_op, deep_map_op_context, Circuit, CircuitNode, CircuitRc};
use pyo3::prelude::*;

use crate::circuit_optimizer::OptimizationContext;

/// don't change symbols bc their names matter for correctness
#[pyfunction]
#[pyo3(name = "strip_names")]
pub fn strip_names_py(circuit: CircuitRc) -> CircuitRc {
    strip_names(circuit, &mut Default::default())
}
pub fn strip_names(circuit: CircuitRc, context: &mut OptimizationContext) -> CircuitRc {
    deep_map_op_context(
        circuit.clone(),
        &|circuit, _| match &**circuit {
            Circuit::Symbol(_sym) => None,
            _ => circuit.name().map(|_| circuit.clone().rename(None)),
        },
        &mut (),
        &mut context.cache.stripped_names,
    )
    .unwrap_or(circuit)
}

pub fn remove_autotags(circuit: CircuitRc) -> CircuitRc {
    deep_map_op(circuit.clone(), |c| {
        if let Some(at) = c.as_tag() {
            return Some(at.node.clone());
        }
        None
    })
    .unwrap_or(circuit)
}
