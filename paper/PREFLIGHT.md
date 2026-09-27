# JOSS pre-flight checklist

Last updated 2026-09-27 on `main`.

✅ done · ⚠️ manual step outside the repository · ℹ️ note for the editor.
No item is awaiting approval. "Who" names who resolved each item.

## Pre-review fixes

| # | Item | Status | Who | Notes |
|---|---|---|---|---|
| 1 | AI usage disclosure | ✅ | Drafted by Claude Code; approved by the author | Lists what Claude Code did (infrastructure, rename, benchmarks, docstring, README sections, paper/bib drafts, source and reference checks). The author confirmed that the core `quantum_group/` code and tests predate AI use and were written by the author, and that all AI changes were reviewed by the author. |
| 2 | "pip install" wording | ✅ | Claude Code | The package installs from the Git repository (`pip install git+https://…` or clone + `pip install -e .`); it is not on PyPI. |
| 3 | Dependency list | ✅ | Claude Code | Runtime: SymPy, NetworkX, Matplotlib. Optional extras: pytest (`[test]`), Jupyter (`[notebooks]`). |
| 4a | Çelik (2021) page range | ⚠️ reopened | — | `paper.bib` currently has `pages = {259--272}` (matches the thesis bibliographies, previously treated as author-confirmed). A later audit found three independent sources — the YTÜ institutional record, Çelik's own citation of this paper in a later article, and the ScienceDirect abstract page — all giving `259--269` instead. The original "author decision" was the thesis's own self-consistent number, not an independent check against the publisher. Needs the original PDF or the publisher's page (or the co-author) before submission; do not treat this as settled. |
| 4b | `paper.md` `date` | ✅ | Author decision | `27 September 2026`, the planned `v1.0.0` release date. |
| 4c | `CITATION.cff` `date-released` | ✅ | Author decision | `2026-09-27`, alongside `version: 1.0.0`; `cffconvert --validate` passes. |
| 4d | Affiliation and acknowledgement | ✅ | Approved by the author | Author names use the Turkish spelling "Çelik" throughout (bibliography, text, acknowledgement). |
| 5 | Official PDF build | ⚠️ stale | — | Last built with `openjournals/inara` (`JOURNAL=joss`) before the item 7 wording fix below, so it no longer matches `paper.md`. `inara` is not installed in this environment; a pandoc+citeproc render (HTML, no LaTeX toolchain available here) confirms the new text has no unresolved citations or markdown errors, but the PDF itself needs regenerating with `inara` (or `@editorialbot generate pdf` once submitted) before it is trusted as the submission artifact. |
| 6 | Development history | ℹ️ | Note for the editor | Objective facts are recorded below; how to present them is the author's call. |
| 7 | `paper.md` overclaiming language | ✅ | Claude Code, verified independently against `main` | An audit flagged three overstated claims in the "Software design" section: (a) "nothing is evaluated in floating point" — false, confirmed by running `R_matrix_V1(2)` with a plain Python `int`, which returns a float entry because `int.__pow__` evaluates `q**(-1)` before SymPy sees it; (b) "the identity holds if and only if every entry simplifies to zero" — an unqualified "iff" overstates what `sympy.simplify` returning zero (or not) actually proves; (c) "functions come in pairs" (`*_residual`/`*_holds`) — false for the Hopf axiom checks, the Hecke relation check, and `local_ybe_on_four_tensor_GLq21`, which expose only a Boolean or a dict of Booleans with no matching `*_residual` function. Rewrote the paragraph to state these accurately. |

> **Reminder:** if the actual JOSS submission date differs from
> 2026-09-27, update `date` in `paper/paper.md` at submission time. Update
> `date-released` in `CITATION.cff` only if a new release (e.g. `v1.0.1`)
> is made; it must match the tagged release.

## Development history (objective note for positioning with the editor)

Based on `git log` of `main` (author dates; the date the repository became
*public* is not recorded in git and should be checked on GitHub):

- **Time span.** First commit 2026-04-28; last pre-JOSS commit 2026-06-14.
  The JOSS preparation commits all date from 2026-09-27. So there are about
  7 weeks of active development, then a 3-month gap, then one day of release
  preparation.
- **Commit activity.** 14 non-merge commits by the author, on 5 distinct
  days, plus 3 JOSS-preparation commits made with Claude Code. Nine of the
  author's commits have the message "test", which says little about the
  history.
- **Collaboration.** One contributor. No GitHub issues. The only pull
  requests are the JOSS-preparation PRs.
- **Where JOSS looks.** Reviewers assess "substantial scholarly effort" and
  signs of an open development process. Short, bursty, single-author history
  is something reviewers commonly ask about. The strongest evidence of
  effort here is the content: the thesis, the manuscript-to-code mapping and
  the 126-case test suite. Consider asking the editors in a pre-submission
  inquiry, and check JOSS's current submission requirements for any
  explicit history criteria.

## Repository

| | Item | Status / evidence |
|---|---|---|
| ✅ | OSI-approved license at repo root | `LICENSE` is the MIT text, © 2026 Taha Berk Terekli; `pyproject.toml` and `CITATION.cff` agree (MIT). |
| ✅ | Installable package | `pip install ".[test]"` and `pip install git+https://…` both work in clean venvs. |
| ✅ | Version 1.0.0 | `pyproject.toml` and `CITATION.cff`. |
| ✅ | Tests pass | `pytest -q`: 126 passed. |
| ✅ | CI green on `main` | GitHub Actions "tests", run 36321146370 on `a422f18`: success (Python 3.10/3.11/3.12). |
| ✅ | README Quickstart runs | Executed verbatim from outside the repo in a clean venv. |
| ✅ | Contribution guidelines, CHANGELOG | `CONTRIBUTING.md`, `CHANGELOG.md`. |
| ✅ | `v1.0.0` tag | Pushed to GitHub on 2026-09-27; the GitHub Release is published. The tag points to `8dcfe996`, before the later thesis cleanup commit. |
| ✅ | Zenodo DOI | Version DOI for `v1.0.0`: [10.5281/zenodo.22997681](https://doi.org/10.5281/zenodo.22997681). Included in `CITATION.cff` and the repository README. |

## paper/paper.md

| | Item | Status / evidence |
|---|---|---|
| ✅ | YAML | `title`, `tags`, `authors` (ORCID valid, with checksum), `affiliations`, `date`, `bibliography` present; affiliation index matches. |
| ✅ | Citations | All keys resolve; no unused bib entries. |
| ✅ | Length | About 1000 words in the body (JOSS guideline: about 1000), including the AI disclosure. |

## Before you submit (in order)

1. Merge PR #4 with a merge commit.
2. ✅ Enable the repository in Zenodo, create the `v1.0.0` tag, publish the
   GitHub Release, and record its version DOI: 10.5281/zenodo.22997681.
3. Decide how to present the development history (see note above).
4. If the submission date is not 2026-09-27, update `date` in `paper.md`.
5. Submit at <https://joss.theoj.org/papers/new> and run
   `@editorialbot generate pdf`.
