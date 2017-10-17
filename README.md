rougescore
==========

This is a Python re-implementation of the ROUGE evaluation package.

ROUGE is a suite of evaluation metrics for automatic text summarization. In
ROUGE, a "peer" summary produced by a machine summarization system is compared
against one or more hand-written "model" summaries and then assigned a score
from 0 to 1. This score is the F-meausure of recall vs. precision, and the
evaluator can adjust a parameter α to control whether this score favors recall
(does the peer summary contain all of the information in the model summaries?)
or precision (does the peer summary contain *only* information in the model
summaries?). When α ≈ 0, this score favors recall; when α ≈ 1, it favors
precision. In the DUC conferences, α was set to 0, and a hard length limit was
imposed on generated summaries. The original ROUGE implementation uses α = 0.5
by default.

This package is meant to serve as a faithful replacement for parts of the
original Perl implementation of ROUGE, providing pure Python implementations
of ROUGE-N and ROUGE-L. The standard Perl script requires that all inputs be
passed through files on disk, which makes it cumbersome to fit into a Python
workflow and limits performance. In many cases it is more convenient to be able
to call a Python function which operates on native Python data types. This
version also does not perform any pre-processing of words or characters,
admitting lists of arbitrary objects that support equality and hashing.

This package deliberately does not implement stemming or stopword removal. It
is up to you to pre-process the peer and model summaries as you see fit before
comparing them.

One difference in the implementation of ROUGE-L from the original is that
separation of the peer and model summaries into "units" (i.e. sentences) is
not supported. That is, peer and model summaries are always treated as single,
continuous strings of tokens, whereas the original ROUGE script allows the
user to split them into sub-units, which affects the matching of common
sub-sequences.

Installation
------------

To install this package (possibly in a
[virtualenv](https://virtualenv.pypa.io/en/stable/)), run:

```sh
git clone https://github.com/bdusell/rougescore.git
cd rougescore
python setup.py install
```

or simply

```sh
pip install git+git://github.com/bdusell/rougescore.git
```
