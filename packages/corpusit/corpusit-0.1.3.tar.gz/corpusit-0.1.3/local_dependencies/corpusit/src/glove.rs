use crate::cooccur::{Cooccurrence, CooccurrenceBuilder};
use crate::vocab::{Vocab, VocabBuilder};
use std::iter::{IntoIterator, Iterator};
use std::sync::{Arc, RwLock};

type Sep = String;

#[derive(Debug, Clone)]
pub struct GloVeConfig {
    pub corpus_path: String,
    pub win_size: usize,
    pub sep: Sep,
    pub power: f64,
    pub xmax: usize,
}

pub struct GloVeDataset {
    cooc: Arc<RwLock<Cooccurrence>>,
    config: GloVeConfig,
}

pub struct GloVeDatasetBuilder {
    config: GloVeConfig,
}

impl GloVeDatasetBuilder {
    pub fn new(config: GloVeConfig) -> Self {
        Self { config: config }
    }

    pub fn build(self) -> GloVeDataset {
        let vocab: Vocab = VocabBuilder::new(&self.config.corpus_path).build();
        self.build_with_vocab(&vocab)
    }

    pub fn build_with_vocab(self, vocab: &Vocab) -> GloVeDataset {
        let cooc = CooccurrenceBuilder::new(
            &self.config.corpus_path,
            vocab.to_owned(),
            self.config.win_size,
            None,
        )
        .build();

        GloVeDataset {
            cooc: Arc::new(RwLock::new(cooc)),
            config: self.config,
        }
    }
}

impl GloVeDataset {
    pub fn new(config: GloVeConfig) -> Self {
        GloVeDatasetBuilder::new(config).build()
    }

    pub fn new_with_vocab(config: GloVeConfig, vocab: &Vocab) -> Self {
        GloVeDatasetBuilder::new(config).build_with_vocab(vocab)
    }
}

pub struct GloVeSample {
    pub i: usize,
    pub j: usize,
    pub logx: f64,
    pub fx: f64,
}

pub struct GloVeDatasetIter {
    cooc: Arc<RwLock<Cooccurrence>>,
    config: GloVeConfig,
    progress: usize,
}

impl Iterator for GloVeDatasetIter {
    type Item = GloVeSample;
    fn next(&mut self) -> Option<Self::Item> {
        let cooc = self.cooc.read().unwrap();
        if self.progress >= cooc.counts.nnz() {
            None
        } else {
            let i = cooc.counts.row_indices()[self.progress];
            let j = cooc.counts.col_indices()[self.progress];
            let c = cooc.counts.values()[self.progress];

            let xmax = self.config.xmax as f64;
            let power = self.config.power;

            let c = c as f64;
            let logx = c.ln();
            let fx: f64 = if c >= xmax {
                1.
            } else {
                (c / xmax).powf(power)
            };
            self.progress += 1;
            Some(GloVeSample {
                i: cooc.rank.r2i[&i],
                j: cooc.rank.r2i[&j],
                logx: logx,
                fx: fx,
            })
        }
    }
}

impl IntoIterator for GloVeDataset {
    type Item = GloVeSample;
    type IntoIter = GloVeDatasetIter;

    fn into_iter(self) -> Self::IntoIter {
        Self::IntoIter {
            cooc: Arc::clone(&self.cooc),
            config: self.config,
            progress: 0,
        }
    }
}
