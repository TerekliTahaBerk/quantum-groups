# JORS submission package

Material for a *Journal of Open Research Software* (JORS) Software
Metapaper about `quantum-group` version **1.1.0**. It is independent of the
JOSS draft in `../paper/`, which is unchanged.

> **Status:** see `SUBMISSION_CHECKLIST.md`. Nothing has been submitted to
> JORS or JOSS, and nothing has been published to PyPI or Zenodo.

## Files

| File | Purpose | Uploaded to JORS? |
|---|---|---|
| `paper.pdf` | Compiled manuscript | **Yes** (main file) |
| `paper.tex` | LaTeX source | **Yes** (source, as JORS asks for LaTeX submissions) |
| `submission-facts.tex` | Author- and event-dependent values used by `paper.tex` | **Yes** (with the source) |
| `references.bib` | Bibliography used by `paper.tex` | **Yes** (with the source) |
| `figures/figure1_workflow.png` | Figure 1, 600 dpi, 3824 × 1264 px | **Yes** (figure file) |
| `figures/figure1_workflow.eps` | Figure 1 as vector EPS | Optional (if vector line art is requested) |
| `figures/figure1_workflow.pdf` | Figure 1, vector PDF used by `paper.tex` | With the source |
| `figures/figure1_workflow.tex` | TikZ source of Figure 1 | No (kept for reproducibility) |
| `COVER_LETTER.md` | Text for the *Comments for the Editor* box | **Paste** (after completion) |
| `POTENTIAL_REVIEWERS.md` | Five screened reviewers (+ reserves); addresses to copy from official pages | Five names + e-mails **pasted** into *Comments for the Editor* |
| `SUBMISSION_CHECKLIST.md` | Status of every submission requirement; APC decision | No |
| `PREFLIGHT.md` | Verification record, reviewer simulation, blockers | No |
| `DISTRIBUTION.md` | PyPI and Zenodo steps for 1.1.0 without a GitHub Release (not executed) | No |
| `zenodo-metadata.json` | Metadata for the manual Zenodo deposit | No (used on Zenodo) |
| `check_submission.py`, `Makefile` | `make check`: builds the PDF, checks Listing 1 and its output against `examples/`, fails while any `[PENDING]` marker is rendered | No |
| `OVERLAP_REVIEW.md` | Comparison with the JOSS draft | No |

## Figure 1

- **Caption (in the paper):** Verification workflow in `quantum-group` …
  (see `paper.tex`).
- **Alt text:** Flow diagram of six boxes. Top row, left to right: source
  identity (published matrix, basis order, coproduct, parities); exact
  construction as SymPy matrices; tensor placement via the coproduct or
  graded adjacent swaps. Bottom row, right to left: residual LHS minus RHS
  as an exact matrix; exact zero test of every entry; regression test in
  CI. A dashed arrow from the zero test back to the source identity is
  labelled "nonzero: inspect entries, check convention".

## Building

Requires TeX Live with `biblatex`, `biblatex-vancouver`, `biber`, `tikz`,
`listings` (Ubuntu: `texlive-latex-extra texlive-science
texlive-bibtex-extra biber latexmk`).

```sh
cd jors
make check                        # manuscript + consistency checks
cd figures && pdflatex figure1_workflow.tex \
  && pdftoppm -png -r 600 -singlefile figure1_workflow.pdf figure1_workflow \
  && pdftops -eps figure1_workflow.pdf figure1_workflow.eps
```

Auxiliary files are git-ignored. `jors/` is excluded from `git archive` (`.gitattributes`), so the software archive contains the software only. Listing 1 must stay identical to
`../examples/sample_verification.py` and its printed output to
`../examples/sample_verification_expected.txt`.
