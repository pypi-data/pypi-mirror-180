use pyo3::prelude::*;
use std::sync::{Arc, RwLock};
extern crate corpusit as cit;
use cit::cooccur::Cooccurrence;

/// Coocurrence information of words.
#[pyclass(dict, module = "corpusit", name = "PyCooc", subclass)]
pub struct PyCooc {
    pub cooc: Arc<RwLock<Cooccurrence>>,
    pub counts: Counts,
    pub i2count: I2Count,
}

#[derive(Clone)]
#[pyclass]
pub struct Counts {
    cooc: Arc<RwLock<Cooccurrence>>,
}

#[derive(Clone)]
#[pyclass]
pub struct I2Count {
    cooc: Arc<RwLock<Cooccurrence>>,
}

#[pymethods]
impl Counts {
    pub fn __getitem__(slf: PyRef<Self>, s_pair: (&str, &str)) -> Option<i64> {
        let cooc = slf.cooc.read().unwrap();
        let id1 = cooc.vocab.get_id_by_str(s_pair.0);
        let id2 = cooc.vocab.get_id_by_str(s_pair.1);
        if id1.is_none() || id2.is_none() {
            None
        } else {
            cooc.counts
                .get_entry(*id1.unwrap(), *id2.unwrap())
                .and_then(|x| Some(x.into_value()))
                .or(Some(0))
        }
    }
}

#[pymethods]
impl I2Count {
    pub fn __getitem__(slf: PyRef<Self>, s_pair: (&usize, &usize)) -> Option<i64> {
        let cooc = slf.cooc.read().unwrap();
        ...
        cooc.counts
            .get_entry(*id1.unwrap(), *id2.unwrap())
            .and_then(|x| Some(x.into_value()))
            .or(Some(0))
    }
}