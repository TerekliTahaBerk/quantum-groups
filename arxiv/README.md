# arXiv preprint

The paper is available as [arXiv:2610.07867](https://arxiv.org/abs/2610.07867),
submitted 6 October 2026, with DOI
[10.48550/arXiv.2610.07867](https://doi.org/10.48550/arXiv.2610.07867).
Primary category: **math.QA**; cross-list: **cs.MS**.

[Read the published PDF](https://arxiv.org/pdf/2610.07867) or the
[repository PDF](paper.pdf). See [citation metadata](../CITATION.cff) and
[downloadable BibTeX](../CITATION.bib).

## Source and build

`../scipost/paper.tex` is the editable source. `build.py` generates the
AMS `amsart` version here, copying the body, appendix and declarations with
layout adjustments. Edit the SciPost source and regenerate; do not edit
`paper.tex` or `references.bib` here by hand.

From the repository root, with the Python package installed and a LaTeX
distribution providing `pdflatex`, `bibtex` and the required packages:

```bash
make -C arxiv check
make -C arxiv bundle
```

`check.py` checks source synchronization, LaTeX diagnostics, bibliography
links and (when present) independent compilation of the upload archive.
`bundle` writes `arxiv_source.tar.gz`, including `paper.bbl` so that the
upload can compile without BibTeX. Generated upload archives are ignored.

The repository sources may evolve after submission. The versioned
[arXiv v1 record](https://arxiv.org/abs/2610.07867v1) identifies the published
version. See the [reproducibility guide](../docs/reproducibility.md) for the
software release and paper listings.
