use itertools::Itertools;
use nalgebra_sparse::{CooMatrix, CsrMatrix};
use rayon::prelude::*;
use serde::{Deserialize, Serialize};
use std::collections::HashMap;
use std::fs::File;
use std::hash::Hash;
use std::io::{BufRead, BufReader, BufWriter};
use std::ops::{Add, AddAssign};
use tqdm::Iter;

use crate::vocab::Vocab;

type Sep = String;

#[derive(Default, Debug, Clone, Deserialize, Serialize)]
pub struct Rank {
    pub i2r: HashMap<usize, usize>,
    pub r2i: HashMap<usize, usize>,
}

impl Rank {
    pub fn build(ids: impl Iterator<Item = usize>) -> Self {
        let mut rank = Rank::default();
        let mut r: usize = 0;
        for i in ids {
            rank.r2i.entry(r).and_modify(|e| *e = i).or_insert(i);
            rank.i2r.entry(i).and_modify(|e| *e = r).or_insert(r);
            r += 1;
        }
        rank
    }
}

#[derive(Deserialize, Serialize)]
pub struct Cooccurrence {
    pub counts: CooMatrix<i64>, // index with rank
    pub vocab: Vocab,           // index with i
    pub rank: Rank,
}

pub struct CooccurrenceBuilder {
    pub corpus_path: String,
    pub vocab: Vocab,
    pub win_size: usize,
    pub sep: Sep,
}

impl CooccurrenceBuilder {
    pub fn new(corpus_path: &str, vocab: Vocab, win_size: usize, sep: Option<Sep>) -> Self {
        CooccurrenceBuilder {
            corpus_path: corpus_path.to_string(),
            vocab: vocab,
            win_size: win_size,
            sep: sep.unwrap_or(" ".to_string()),
        }
    }

    pub fn build(&self) -> Cooccurrence {
        let rank = Rank::build(self.vocab.i2s.keys().map(|i| *i).sorted());

        let unk_id = self.vocab.unk_id();

        let f = File::open(&self.corpus_path).unwrap();
        let f = BufReader::new(f);
        let mut counts = CsrMatrix::<i64>::zeros(self.vocab.len(), self.vocab.len());
        for large_chunk in f
            .lines()
            .map(Result::unwrap)
            .tqdm()
            .into_iter()
            .chunks(1000000)
            .into_iter()
        {
            let large_chunk: Vec<String> = large_chunk.collect();
            let chunk_counts = large_chunk
                .chunks(10000)
                .par_bridge()
                .map(|chunk| -> CsrMatrix<i64> {
                    let mut counts1 = HashMap::<(usize, usize), i64>::new();
                    for line in chunk {
                        let rankseq = line
                            .split(&self.sep)
                            .filter_map(|token| self.vocab.s2i.get(token).or(unk_id))
                            .map(|id| rank.i2r[id])
                            .collect_vec();
                        for i in 0..rankseq.len() {
                            let left = if i >= self.win_size {
                                i - self.win_size
                            } else {
                                0
                            };
                            let right = (i + self.win_size).min(rankseq.len());
                            for j in left..right {
                                counts1
                                    .entry((rankseq[i], rankseq[j]))
                                    .and_modify(|c| *c += 1)
                                    .or_insert(1);
                            }
                        }
                    }
                    let mut coo = CooMatrix::<i64>::new(self.vocab.len(), self.vocab.len());
                    for ((i, j), c) in counts1.into_iter() {
                        coo.push(i, j, c);
                    }
                    CsrMatrix::<i64>::from(&coo)
                })
                .reduce(
                    || CsrMatrix::<i64>::zeros(self.vocab.len(), self.vocab.len()),
                    |counts1: CsrMatrix<i64>, counts2: CsrMatrix<i64>| -> CsrMatrix<i64> {
                        counts1 + counts2
                    },
                );

            counts = counts + chunk_counts;
        }

        let cooc_path = self.corpus_path.clone() + ".cooc.bin";
        let cooc = Cooccurrence {
            counts: CooMatrix::from(&counts),
            vocab: self.vocab.to_owned(),
            rank: rank,
        };
        cooc.to_bin(&cooc_path);

        cooc
    }
}

impl Cooccurrence {
    pub fn to_bin(&self, path: &str) {
        let vocab_f = File::create(path).unwrap();
        let vocab_f = BufWriter::new(vocab_f);
        bincode::serialize_into(vocab_f, self).unwrap();
    }

    pub fn from_bin(path_to_bin: &str) -> Self {
        let f = File::open(path_to_bin).unwrap();
        let f = BufReader::new(f);
        let cooc: Self = bincode::deserialize_from(f).unwrap();
        cooc
    }
}

fn _merge_counts<K, T>(mut c1: HashMap<K, T>, c2: HashMap<K, T>) -> HashMap<K, T>
where
    K: Eq + Hash + Copy,
    T: Add + AddAssign + Copy,
{
    c2.iter().for_each(|(key, count)| {
        c1.entry(*key)
            .and_modify(|e| *e += *count)
            .or_insert(*count);
    });
    c1
}

#[cfg(test)]
mod tests {
    use crate::vocab::Vocab;
    use crate::cooccur::{Cooccurrence, CooccurrenceBuilder};

    #[test]
    fn build() {
        let path = "data/corpus.txt";
        let vocab = Vocab::from_json("data/corpus.txt.vocab.json", Some(1), None, Some("<unk>"));
        let builder = CooccurrenceBuilder::new(path, vocab, 2, Some(" ".to_string()));
        let cooc = builder.build();
    }

    #[test]
    fn load() {
        let cooc_path = "data/corpus.txt.cooc.bin";
        let cooc = Cooccurrence::from_bin(cooc_path);
        let vocab = cooc.vocab;
        let counts = cooc.counts;

        let mut i = 0;
        println!("Number of word pairs: {}", counts.nnz());
        for (irow, icol, count) in counts.triplet_iter() {
            i += 1;
            if i > 100 {
                break;
            }

            println!(
                "Cooccurrence count of word {} ({}) and {} ({}): {}",
                irow, vocab.i2s[&irow], icol, vocab.i2s[&icol], count
            );
        }
    }
}
