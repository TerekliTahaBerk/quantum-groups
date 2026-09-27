# JOSS pre-flight checklist

Last updated 2026-09-27 on branch `claude/happy-lamport-lq2yqj` (based on
`main` @ `a422f18`).

✅ done · ⚠️ needs your review, approval or a manual step · ❌ must be fixed
before submission. "Who" names who resolved an item or whose decision it
awaits.

## Pre-review fixes (latest round)

| # | Item | Status | Who | Notes |
|---|---|---|---|---|
| 1 | AI usage disclosure | ⚠️ | Drafted by Claude Code; **author approval needed** | Section added to `paper.md`. It lists what Claude Code did (infrastructure, rename, benchmarks, docstring, README sections, paper/bib drafts, source and reference checks) and what the author did. The sentence saying the core `quantum_group/` code and tests predate AI use and were written by the author is marked `ONAY BEKLİYOR`: only the author can confirm it. |
| 2 | "pip install" wording | ✅ | Claude Code | `paper.md` and `README.md` now say the package is installed from the Git repository (`pip install git+https://github.com/TerekliTahaBerk/quantum-groups` or clone + `pip install -e .`) and is not on PyPI. The `git+https` command was tested in a clean venv and the README Quickstart passes. No PyPI packaging was added. |
| 3 | Dependency list | ✅ | Claude Code | Runtime dependencies are SymPy, NetworkX and Matplotlib; all three are imported when the package is imported. pytest and Jupyter are optional extras (`[test]`, `[notebooks]`), not runtime dependencies, and are described that way. The "lighter than GAP/SageMath" claim still holds (three pip-installable libraries versus a GAP or SageMath installation); the wording now names the dependencies. |
| 4a | Çelik (2021) page range | ⚠️ | **Author decision** | Not filled in. Proposal: `259--272` (every thesis bibliography). Conflict: a ScienceDirect listing showed `259--269`. Marked `ONAY BEKLİYOR` in `paper.bib`. |
| 4b | `paper.md` `date` | ⚠️ | **Author decision** | Still `27 September 2026`; marked `ONAY BEKLİYOR`. Today's date or the actual submission date? |
| 4c | `CITATION.cff` `date-released` | ⚠️ | **Author decision** | Not added. Needs the v1.0.0 tag/release date. |
| 4d | Affiliation and acknowledgement | ⚠️ | Drafted; **author approval needed** | Both marked `ONAY BEKLİYOR` in `paper.md` (affiliation: YTÜ Department of Mathematics; acknowledgement: thanks to Prof. Dr. Salih Çelik). Note: the bibliography spells the name "Celik", as in the published article, while the acknowledgement uses "Çelik". |
| 5 | Official PDF build | ✅ | Claude Code | Built with JOSS's own toolchain (`openjournals/inara` Docker image, `JOURNAL=joss`). PDF (4 pages), Crossref XML and JATS were generated without errors, with no unresolved citations; the table and math render; `ONAY BEKLİYOR` comments do not appear in the PDF. This fixed the name order "Graaf, W. A. de" to "de Graaf". The editorialbot build at submission (`@editorialbot generate pdf`) remains the final check. |
| 6 | Development history | ⚠️ | **Author decision** (see note below) | Objective facts recorded below; no threshold is claimed. |

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
| ⚠️ | `v1.0.0` tag | Must not be pushed until items 1 and 4 are settled. After this branch is merged into `main` with a merge commit, (re)create the tag on the final commit and push it. After a squash merge, create it on the new `main` commit. |
| ⚠️ | Zenodo DOI | Not yet created; manual steps are in `paper/README.md`. JOSS needs it at acceptance. |

## paper/paper.md

| | Item | Status / evidence |
|---|---|---|
| ✅ | YAML | `title`, `tags`, `authors` (ORCID valid, with checksum), `affiliations`, `date`, `bibliography` present; affiliation index matches. |
| ✅ | Citations | All keys resolve; no unused bib entries. |
| ✅ | Length | About 1000 words in the body (JOSS guideline: about 1000), including the AI disclosure. |

## Before you submit (in order)

1. Approve or edit the AI usage disclosure, especially the `ONAY BEKLİYOR`
   sentence about the core code.
2. Decide items 4a–4d (page range, paper date, `date-released`, affiliation
   and acknowledgement), then remove the `ONAY BEKLİYOR` markers.
3. Merge; create and push `v1.0.0`; enable Zenodo; publish the GitHub Release.
4. Decide how to present the development history (item 6).
5. Submit at <https://joss.theoj.org/papers/new> and run
   `@editorialbot generate pdf`.
