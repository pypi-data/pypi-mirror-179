use chinilla_protocol::coin::Coin;
use chinilla_protocol::coin_state::CoinState;
use chinilla_protocol::respond_to_ph_updates::RespondToPhUpdates;
use chinilla_protocol::bls::G1Element;
use chinilla_protocol::bls::G2Element;
use crate::run_generator::{PySpend, PySpendBundleConditions, __pyo3_get_function_run_generator};
use chinilla::gen::flags::COND_ARGS_NIL;
use chinilla::gen::flags::NO_UNKNOWN_CONDS;
use chinilla::gen::flags::STRICT_ARGS_COUNT;
use chinilla::merkle_set::compute_merkle_set_root as compute_merkle_root_impl;
use std::convert::TryInto;
//use chinilla::streamable::fullblock::Fullblock;
use clvmr_chinilla::chinilla_dialect::LIMIT_HEAP;
use clvmr_chinilla::chinilla_dialect::NO_NEG_DIV;
use clvmr_chinilla::chinilla_dialect::NO_UNKNOWN_OPS;
use clvmr_chinilla::serialize::tree_hash_from_stream;
use pyo3::prelude::*;
use pyo3::types::PyBytes;
use pyo3::types::PyModule;
use pyo3::{wrap_pyfunction, PyResult, Python};

use crate::run_program::{
    __pyo3_get_function_run_chinilla_program, __pyo3_get_function_serialized_length,
};

use crate::adapt_response::eval_err_to_pyresult;
use chinilla_protocol::bytes::Bytes32;
use chinilla::gen::get_puzzle_and_solution::get_puzzle_and_solution_for_coin as parse_puzzle_solution;
use chinilla::gen::validation_error::ValidationErr;
use clvmr_chinilla::allocator::Allocator;
use clvmr_chinilla::chinilla_dialect::ChinillaDialect;
use clvmr_chinilla::cost::Cost;
use clvmr_chinilla::node::Node;
use clvmr_chinilla::reduction::EvalErr;
use clvmr_chinilla::reduction::Reduction;
use clvmr_chinilla::run_program::run_program;
use clvmr_chinilla::serialize::node_from_bytes;
use clvmr_chinilla::serialize::node_to_bytes;

pub const MEMPOOL_MODE: u32 =
    NO_NEG_DIV | NO_UNKNOWN_CONDS | NO_UNKNOWN_OPS | COND_ARGS_NIL | STRICT_ARGS_COUNT | LIMIT_HEAP;

#[pyfunction]
pub fn compute_merkle_set_root<'p>(
    py: Python<'p>,
    values: Vec<&'p PyBytes>,
) -> PyResult<&'p PyBytes> {
    let mut buffer = Vec::<[u8; 32]>::with_capacity(values.len());
    for b in values {
        buffer.push(b.as_bytes().try_into()?);
    }
    Ok(PyBytes::new(py, &compute_merkle_root_impl(&mut buffer)))
}

#[pyfunction]
pub fn tree_hash(py: Python, blob: pyo3::buffer::PyBuffer<u8>) -> PyResult<&PyBytes> {
    if !blob.is_c_contiguous() {
        panic!("tree_hash() must be called with a contiguous buffer");
    }
    let slice =
        unsafe { std::slice::from_raw_parts(blob.buf_ptr() as *const u8, blob.len_bytes()) };
    let mut input = std::io::Cursor::<&[u8]>::new(slice);
    Ok(PyBytes::new(py, &tree_hash_from_stream(&mut input)?))
}

#[pyfunction]
pub fn get_puzzle_and_solution_for_coin<'py>(
    py: Python<'py>,
    program: &[u8],
    args: &[u8],
    max_cost: Cost,
    find_parent: Bytes32,
    find_amount: u64,
    find_ph: Bytes32,
) -> PyResult<(&'py PyBytes, &'py PyBytes)> {
    let mut allocator = Allocator::new();
    let program = node_from_bytes(&mut allocator, program)?;
    let args = node_from_bytes(&mut allocator, args)?;
    let dialect = &ChinillaDialect::new(NO_NEG_DIV);

    let r = py.allow_threads(|| -> Result<(Vec<u8>, Vec<u8>), EvalErr> {
        let Reduction(_cost, result) =
            run_program(&mut allocator, dialect, program, args, max_cost, None)?;
        match parse_puzzle_solution(&allocator, result, find_parent, find_amount, find_ph) {
            Err(ValidationErr(n, _)) => Err(EvalErr(n, "coin not found".to_string())),
            Ok((puzzle, solution)) => Ok((
                node_to_bytes(&Node::new(&allocator, puzzle)).unwrap(),
                node_to_bytes(&Node::new(&allocator, solution)).unwrap(),
            )),
        }
    });

    match r {
        Err(eval_err) => eval_err_to_pyresult(py, eval_err, allocator),
        Ok((puzzle, solution)) => Ok((PyBytes::new(py, &puzzle), PyBytes::new(py, &solution))),
    }
}

#[pymodule]
pub fn chinilla_rs(_py: Python, m: &PyModule) -> PyResult<()> {
    // generator functions
    m.add_function(wrap_pyfunction!(run_generator, m)?)?;
    m.add_class::<PySpendBundleConditions>()?;
    m.add("ELIGIBLE_FOR_DEDUP", chinilla::gen::conditions::ELIGIBLE_FOR_DEDUP)?;
    m.add_class::<PySpend>()?;

    // clvm functions
    m.add("COND_ARGS_NIL", COND_ARGS_NIL)?;
    m.add("NO_UNKNOWN_CONDS", NO_UNKNOWN_CONDS)?;
    m.add("STRICT_ARGS_COUNT", STRICT_ARGS_COUNT)?;
    m.add("MEMPOOL_MODE", MEMPOOL_MODE)?;

    // Chinilla classes
    m.add_class::<Coin>()?;
    m.add_class::<CoinState>()?;
    m.add_class::<RespondToPhUpdates>()?;
    m.add_class::<G1Element>()?;
    m.add_class::<G2Element>()?;
    //m.add_class::<Fullblock>()?;

    // facilities from clvm_rs

    m.add_function(wrap_pyfunction!(run_chinilla_program, m)?)?;
    m.add("NO_NEG_DIV", NO_NEG_DIV)?;
    m.add("NO_UNKNOWN_OPS", NO_UNKNOWN_OPS)?;
    m.add("LIMIT_HEAP", LIMIT_HEAP)?;

    m.add_function(wrap_pyfunction!(serialized_length, m)?)?;
    m.add_function(wrap_pyfunction!(compute_merkle_set_root, m)?)?;
    m.add_function(wrap_pyfunction!(tree_hash, m)?)?;
    m.add_function(wrap_pyfunction!(get_puzzle_and_solution_for_coin, m)?)?;

    Ok(())
}
