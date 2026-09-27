# JOSS pre-flight checklist

Checked on 2026-09-27 against `main` @ `a422f18`, plus the files added with
this checklist. ✅ done · ⚠️ needs your review or a manual step · ❌ must be
fixed before submission.

## Repository

| | Item | Status / evidence |
|---|---|---|
| ✅ | OSI-approved license at repo root | `LICENSE` is the MIT text, © 2026 Taha Berk Terekli; `pyproject.toml` and `CITATION.cff` agree (MIT). |
| ✅ | Installable package | `pip install ".[test]"` works in a clean venv (Python 3.11). |
| ⚠️ | Not on PyPI | The name `quantum-group` is free on PyPI (404). The paper says the package "needs only `pip install`"; a reviewer may try `pip install quantum-group`. Either publish to PyPI or say "installable with pip from the repository". |
| ✅ | Version 1.0.0 | `pyproject.toml` `version = "1.0.0"`; `CITATION.cff` `version: 1.0.0`. |
| ⚠️ | `CITATION.cff` `date-released` | Missing. Add the release date before the GitHub Release (Zenodo reads it). |
| ✅ | Tests pass | `pytest -q`: 126 passed (Python 3.11, clean venv). |
| ✅ | CI green on `main` | GitHub Actions "tests", run 36321146370 on `a422f18`: success (Python 3.10/3.11/3.12). |
| ✅ | README Quickstart runs | Code block executed verbatim from outside the repo in a clean venv: all assertions pass. |
| ✅ | Contribution guidelines | `CONTRIBUTING.md` (issues, PRs, tests, style). |
| ✅ | CHANGELOG | `CHANGELOG.md` with a `1.0.0` entry. |
| ⚠️ | `v1.0.0` tag | Annotated tag created **locally only**, not pushed. Push it after this branch is merged into `main` with a merge commit. After a squash merge, recreate the tag on the new `main` commit. |
| ⚠️ | Zenodo DOI | Not yet created. Manual steps are in `paper/README.md` (enable the repo in Zenodo, publish a GitHub Release). JOSS needs the DOI at acceptance, not at submission. |
| ⚠️ | Development history | Public history starts 2026-04-28. Compare with JOSS's current "substantial scholarly effort" and development-history criteria before submitting. |

## paper/paper.md

| | Item | Status / evidence |
|---|---|---|
| ✅ | YAML parses | `title`, `tags` (6), `authors`, `affiliations`, `date`, `bibliography` all present. |
| ✅ | ORCID | `0009-0004-8266-1116`: valid format and checksum (ISO 7064 mod 11-2). |
| ✅ | Affiliation indices | Author's `affiliation: 1` matches `affiliations[0].index: 1`. |
| ⚠️ | Author, affiliation, acknowledgement | Confirm "Department of Mathematics, Yıldız Technical University, Istanbul, Türkiye" is correct at submission time, and confirm the wording of the acknowledgement to Prof. Dr. Salih Çelik. |
| ⚠️ | `date` | `27 September 2026`. Set it to the submission date. |
| ✅ | Citations resolve | Every `[@key]` exists in `paper.bib` and every bib entry is cited; pandoc 3.9 `--citeproc` renders with no unresolved citations. |
| ✅ | Length | Body about 850 words (limit about 1000). |
| ❌ | AI usage disclosure | Only an HTML comment placeholder. JOSS requires this section. It must describe the tools actually used; the git history contains `Co-Authored-By: Claude` commits. |
| ⚠️ | Çelik & Çelik (2021) pages | `pages` omitted in `paper.bib`: the thesis gives 259–272, ScienceDirect 259–269. Check the publisher record and add the range. |
| ⚠️ | Installation wording | The comparison table says "`pip`; SymPy", but the package also depends on NetworkX and Matplotlib (see README). Align the wording. |
| ⚠️ | Official PDF build | Only checked with local pandoc. Run `@editorialbot generate pdf` (or JOSS's Docker/Inara build) to confirm the table and math render. |

## Before you submit (in order)

1. Write the AI usage disclosure (❌ above).
2. Add the Çelik (2021) page range; update the paper `date`; confirm
   author, affiliation and acknowledgement.
3. Fix the installation wording (and optionally publish to PyPI).
4. Add `date-released` to `CITATION.cff`.
5. Merge this branch; push the `v1.0.0` tag; publish the GitHub Release.
6. Enable Zenodo first (see `paper/README.md`) so the release gets a DOI.
7. Build the paper with JOSS's tooling, then submit at
   <https://joss.theoj.org/papers/new>.
