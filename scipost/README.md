# SciPost-format userguide

This directory contains the userguide prepared in the *SciPost Physics
Codebases* template. The public preprint is
[arXiv:2610.07867](https://arxiv.org/abs/2610.07867), DOI
[10.48550/arXiv.2610.07867](https://doi.org/10.48550/arXiv.2610.07867).
The template format does not imply journal acceptance or publication.

- [paper.pdf](paper.pdf): userguide with conventions, worked examples and
  the public API reference (Appendix A).
- `paper.tex` and `references.bib`: editable manuscript source, also used
  to generate the [AMS-format preprint](../arxiv/README.md).
- `examples/`: Listings 2–5 and their expected outputs.
- [crosscheck/](crosscheck/README.md): Listing 6, exported GAP/QuaGroup data
  and instructions for regenerating them.
- `figures/`: workflow diagram source and PDF.
- `SciPost.cls`, `SciPost_bibstyle.bst`, `official_template/`: retained
  upstream template assets.
- [PREFLIGHT.md](PREFLIGHT.md): dated preparation and verification record.

From the repository root:

```bash
make listings   # verify all six listings; Python only
make paper      # rebuild and check the userguide; requires LaTeX
```

`check_submission.py` compares manuscript listings and printed outputs
with the scripts and expected files, reruns the scripts, and checks LaTeX
diagnostics and bibliography links. See the
[reproducibility guide](../docs/reproducibility.md) for environment setup.
