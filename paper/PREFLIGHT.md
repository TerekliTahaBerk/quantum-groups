# JOSS pre-flight checklist

Last updated 2026-09-27 on branch `claude/happy-lamport-lq2yqj` (based on
`main` @ `a422f18`).

✅ done · ⚠️ manual step outside the repository · ℹ️ note for the editor.
No item is awaiting approval. "Who" names who resolved each item.

## Pre-review fixes

| # | Item | Status | Who | Notes |
|---|---|---|---|---|
| 1 | AI usage disclosure | ✅ | Drafted by Claude Code; approved by the author | Lists what Claude Code did (infrastructure, rename, benchmarks, docstring, README sections, paper/bib drafts, source and reference checks). The author confirmed that the core `quantum_group/` code and tests predate AI use and were written by the author, and that all AI changes were reviewed by the author. |
| 2 | "pip install" wording | ✅ | Claude Code | The package installs from the Git repository (`pip install git+https://…` or clone + `pip install -e .`); it is not on PyPI. |
| 3 | Dependency list | ✅ | Claude Code | Runtime: SymPy, NetworkX, Matplotlib. Optional extras: pytest (`[test]`), Jupyter (`[notebooks]`). |
| 4a | Çelik (2021) page range | ✅ | Author decision | `pages = {259--272}`, as in the thesis bibliographies. |
| 4b | `paper.md` `date` | ✅ | Author decision | `27 September 2026`, the date of the `v1.0.0` tag. |
| 4c | `CITATION.cff` `date-released` | ✅ | Author decision | `2026-09-27`, alongside `version: 1.0.0`; `cffconvert --validate` passes. |
| 4d | Affiliation and acknowledgement | ✅ | Approved by the author | Author names use the Turkish spelling "Çelik" throughout (bibliography, text, acknowledgement). |
| 5 | Official PDF build | ✅ | Claude Code | Rebuilt with `openjournals/inara` (`JOURNAL=joss`) after the final edits: 4 pages, Crossref XML generated, no unresolved citations, no leftover approval markers. `@editorialbot generate pdf` at submission remains the final check. |
| 6 | Development history | ℹ️ | Note for the editor | Objective facts are recorded below; how to present them is the author's call. |

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
| ✅ | `v1.0.0` tag | Annotated tag "First release prepared for JOSS submission" pushed on 2026-09-27. It points to the commit that finalized this checklist, on PR #4's branch. Merge PR #4 with a **merge commit** (not squash) so the tagged commit becomes part of `main`. |
| ⚠️ | Zenodo DOI | Not yet created; manual steps are in `paper/README.md`. JOSS needs it at acceptance. |

## paper/paper.md

| | Item | Status / evidence |
|---|---|---|
| ✅ | YAML | `title`, `tags`, `authors` (ORCID valid, with checksum), `affiliations`, `date`, `bibliography` present; affiliation index matches. |
| ✅ | Citations | All keys resolve; no unused bib entries. |
| ✅ | Length | About 1000 words in the body (JOSS guideline: about 1000), including the AI disclosure. |

## Before you submit (in order)

1. Merge PR #4 with a merge commit.
2. Enable the repository in Zenodo, then publish a GitHub Release from the
   `v1.0.0` tag to mint the DOI (see `paper/README.md`).
3. Decide how to present the development history (see note above).
4. If the submission date is not 2026-09-27, update `date` in `paper.md`.
5. Submit at <https://joss.theoj.org/papers/new> and run
   `@editorialbot generate pdf`.
