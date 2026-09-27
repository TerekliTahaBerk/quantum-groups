# Publication verification record

Updated 27 September 2026 for the uncommitted publication-audit corrections.
The active manuscript is `paper.md`, with references in `paper.bib`.
This record supersedes the earlier pre-submission checklist; historical
release/CI records do not certify the current working tree.

| Item | Current status and evidence |
|---|---|
| Primary GL source | Original author-supplied PDF inspected. Every R entry and the super-permutation match printed p.261. Pagination corrected to 259–269. |
| Fundamental R convention | Both conventions are explicit. New package-compatible APIs preserve historical outputs. Tests cover all four intertwiners and compatible CG eigenspaces. |
| Representation and tensor claims | Generic-q qualifications explicit. Full descendant basis changes checked for (1,1), (2,2), (3,2). General proof corrections are in `../thesis/ERRATA.md`. |
| Grading | Independent component oracle checks all six n=4 placements; all disjoint commutators tested; ordinary-swap negative control fails as expected. |
| Exact arithmetic | Native integers remain exact. Laurent q-arithmetic handles removable singularities. Floating inputs are explicitly approximate. |
| Scope | No new mathematics, Jones polynomial, Gauss verification, abstract Hopf proof, root-of-unity classification or crystal-basis algorithm is claimed. |
| AI disclosure | Updated to include Codex code and test changes. Does not claim the author has already reviewed this latest revision. |
| Local tests | 158 pytest cases plus three package doctests; final command and result below. |
| CI | Workflow covers Python 3.10, 3.11, 3.12. These local changes have not been pushed, so there is no new remote CI run. |
| Manuscript preview | `../output/pdf/quantum-group-review.pdf` is a local Pandoc/citeproc/XeLaTeX reading copy, not official JOSS typesetting. |
| Official JOSS PDF | Still requires the journal's Inara/editorialbot build. Docker client exists locally, but its daemon is unavailable. Do not submit an older PDF as if it reflected this source. |
| Archived thesis | Existing Turkish sources and PDFs remain historical artifacts; `../thesis/ERRATA.md` supplies corrections. A regenerated thesis PDF is not part of this JOSS revision. |
| Release/archive | Existing version and DOI metadata are unchanged. The current fixes are **Unreleased** in `../CHANGELOG.md` and are not covered by an older archived release. |
| Git and communication | No commit, push, tag, release, submission or reviewer message performed. |

## Reproducible checks

```sh
MPLCONFIGDIR=/tmp/quantum-audit-mpl python3 -m pytest tests/ --doctest-modules quantum_group -q
```

**Final result: 161 passed in 7.52 s (158 pytest cases + 3 doctests).**
`git diff --check` also passed. All 11 bibliography keys resolve, with no
unused entries or citeproc warnings. The body is approximately 960 words. Local environment:
Python 3.12.10, SymPy 1.14.0. The 158-case count excludes three doctests.

The local PDF uses the exact `paper.md` and `paper.bib` sources with Pandoc
citeproc; it is intended for reading and layout inspection. Journal-specific
YAML (author affiliation, ORCID) remains in `paper.md` for the official build.

## Author/editor handoff

Review the revised manuscript, `../AUDIT.md`, `../thesis/ERRATA.md` and the
working-tree diff. `REVIEW_CHANGES.md` provides a ready-to-use factual change
summary for the existing review; it has not been sent. After accepting these
changes, run the configured CI, build the official JOSS PDF, and archive the
actual revised release as required by the journal. Do not reuse an old
version DOI as though it contained these changes. Publication acceptance is
an editorial decision; passing local tests is not an acceptance guarantee.
