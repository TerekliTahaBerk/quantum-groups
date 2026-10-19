# Documentation

`quantum-group` verifies explicit quantum-group matrices with exact SymPy
arithmetic. Start with the [README quickstart](../README.md#quickstart).
The [paper on arXiv](https://arxiv.org/abs/2610.07867) includes the
mathematical conventions, worked examples and a public API reference
(Appendix A).

## Use and reproduce

| Task | Guide |
| --- | --- |
| Install and run a first calculation | [Installation and quickstart](../README.md#installation) |
| Reproduce the paper's six listings and verification claims | [Reproducibility guide](reproducibility.md) |
| Read coproduct, basis and grading conventions | [Conventions](../README.md#conventions-and-mathematical-background) |
| Inspect supported features and limitations | [Scope](../README.md#scope-and-limitations) |
| Build the arXiv-format manuscript | [arxiv/](../arxiv/README.md) |
| Build the SciPost-format userguide | [scipost/](../scipost/README.md) |
| Inspect the GAP/QuaGroup cross-check | [Cross-check notes](../scipost/crosscheck/README.md) |
| Inspect measured performance | [Benchmark results](../benchmarks/results.md) |
| Cite the paper and software | [Citation](../README.md#citation), [BibTeX](../CITATION.bib), [CFF](../CITATION.cff) |

## Provenance and maintenance

- [Mathematical audit](../AUDIT.md): historical findings, corrections and
  source-access evidence.
- [Manuscript-to-code mapping](../MANUSCRIPT_CODE_MAPPING.md): implemented
  claims and the tests that support them.
- [Thesis archive](../thesis/README.md) and [errata](../thesis/ERRATA.md):
  original undergraduate work and subsequent corrections.
- [Contributing](../CONTRIBUTING.md), [changelog](../CHANGELOG.md) and
  [release checklist](../RELEASING.md).

The top-level audit and mapping files, package paths and manuscript example
paths are retained because the published paper and earlier archives refer
to them. `scipost/paper.tex` is the editable manuscript source;
`arxiv/build.py` generates the AMS-format version from it.
