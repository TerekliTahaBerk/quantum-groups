# JORS submission checklist

Status on **27 September 2026**. Each item was verified directly (see
`PREFLIGHT.md` for evidence), not taken from earlier documentation.

Legend: **READY** · **AUTHOR CONFIRMATION REQUIRED** ·
**TECHNICAL ACTION REQUIRED** · **HARD BLOCKER**

The journal's own checklist could not be read verbatim (site blocked, see
`PREFLIGHT.md` §1). The rows below cover every item that the journal's
guidelines and the software review form were confirmed to contain, plus the
items requested for this package. Re-read the live checklist before
submitting and add any item missing here.

## Journal checklist and review criteria

| # | Item | Status | Evidence / action |
|---|---|---|---|
| 1 | Software is a substantive research contribution (not trivial) | **READY** | Residual-first verification layer, convention-aware R-matrix APIs, graded embedding machinery, 202 tests incl. negative controls; paper claims software/method contribution only, no new mathematics |
| 2 | Public open-source repository | **READY** | https://github.com/TerekliTahaBerk/quantum-groups (public, browsable, open issue tracker) |
| 3 | OSI-approved licence | **READY** | MIT (`LICENSE`; `License-Expression: MIT` in package metadata) |
| 4 | Easy to install | **READY** (from GitHub) | `pip install "git+https://github.com/TerekliTahaBerk/quantum-groups"`; wheel install tested on Linux, macOS, Windows in CI |
| 5 | Installable from a package registry (PyPI/conda) | **HARD BLOCKER** | Not on PyPI (404, 27 Sep 2026). Build, `twine check`, clean install and Trusted-Publishing workflow are ready; the author must configure PyPI and publish (`RELEASE_STEPS.md`). Then record the successful `python -m pip install quantum-group` in `PREFLIGHT.md`. |
| 6 | Supports versioning | **TECHNICAL ACTION REQUIRED** | Semantic versioning and changelog exist; version 1.1.0 is untagged and unreleased. Tag/release v1.1.0 (`RELEASE_STEPS.md` §2–3). |
| 7 | Archive with persistent identifier for the described version | **HARD BLOCKER** | Only DOI 10.5281/zenodo.22997681 exists and archives v1.0.0. A v1.1.0 Zenodo version DOI is required. |
| 8 | Archive contents match the code described | **HARD BLOCKER** (follows 7) | After the release, diff the Zenodo zip against `git archive v1.1.0` (`RELEASE_STEPS.md` §4). |
| 9 | Manuscript follows the Software Metapaper template | **AUTHOR CONFIRMATION REQUIRED** | `paper.tex` uses the template's headings and fields; the official template file could not be downloaded here. Compare with the live template. |
| 10 | Title objective, no novelty claim, journal capitalisation | **READY** | "quantum-group: Exact SymPy Verification of Explicit U_q(sl_2) and GL_q(2\|1) Matrix Identities" (title case as in current JORS articles; package name kept lower-case as a proper name) |
| 11 | Abstract length | **AUTHOR CONFIRMATION REQUIRED** | 158 words; the template historically asked for ca. 100 words. Shorten if the live template still says so. |
| 12 | Sample input and output available | **READY** | Listing 1 = `examples/sample_verification.py`; expected output file; compared in CI |
| 13 | Quality control described | **READY** | Quality control section, Table 1, CI description |
| 14 | Reuse potential with concrete extension routes and support statement | **READY** | Section (3) |
| 15 | Manuscript not previously published | **READY** (author to re-confirm at submission) | Not published in any journal. Related public material, not prior publication under the journal's preprint policy: the JOSS draft `paper/paper.md` in the repository (never submitted) and the undergraduate thesis (cited). Disclosed in the cover letter. |
| 16 | Manuscript not under consideration elsewhere | **AUTHOR CONFIRMATION REQUIRED — conditional HARD BLOCKER** | Repository records state that no JOSS submission exists. Confirm immediately before submitting. If a JOSS (or other) submission exists at that moment, JORS submission is **BLOCKED** until it has ended or been withdrawn. |
| 17 | Figures referenced in text, numbered captions | **READY** | Figure 1 cited in *Implementation and architecture* |
| 18 | Figure files uploaded separately, resolution ≥150 dpi (300 preferred) | **READY** | `figures/figure1_workflow.png` 600 dpi; also EPS and PDF |
| 19 | Figure alt text | **READY** | In `README.md` (paste into the upload form if asked) |
| 20 | Tables inside the manuscript and cited | **READY** | Table 1 in *Quality control*, cited in the text |
| 21 | Vancouver numeric references in order of first citation | **READY** | `biblatex-vancouver`, `sorting=none`; 15 entries, all cited |
| 22 | References have DOI/URL where available and correct | **AUTHOR CONFIRMATION REQUIRED** | de Graaf 2001 DOI not independently resolvable here; resolve it once. Other entries: see `PREFLIGHT.md` §5 |
| 23 | Competing-interests statement | **AUTHOR CONFIRMATION REQUIRED** | Placeholder in the paper. If none: "The author has no competing interests to declare." |
| 24 | Funding statement | **AUTHOR CONFIRMATION REQUIRED** | The repository contains no funding information. State funder and grant number, or confirm that there was no funding. |
| 25 | Generative-AI disclosure (Ubiquity Press policy) | **AUTHOR CONFIRMATION REQUIRED** | Drafted from the Git record in the paper and cover letter; the author must insert exact model names/versions and confirm AI use (or not) before September 2026 |
| 26 | Authorship and consent | **AUTHOR CONFIRMATION REQUIRED** | Sole human author. Supervisor acknowledged, not listed as author; Çelik & Çelik are not authors. Confirm current affiliation. |
| 27 | Five potential reviewers with names and e-mail addresses | **HARD BLOCKER** | `POTENTIAL_REVIEWERS.md` lists 8 screened candidates, but no e-mail address could be verified from an official page here. Choose five and copy each address from the official page. |
| 28 | Cover letter in *Comments for the Editor* | **AUTHOR CONFIRMATION REQUIRED** | `COVER_LETTER.md` drafted; marked NOT SUBMITTABLE until blockers are cleared |
| 29 | APC acknowledged / waiver decision | **AUTHOR CONFIRMATION REQUIRED** | See below |
| 30 | Manuscript PDF + LaTeX source | **TECHNICAL ACTION REQUIRED** | Builds cleanly; rebuild after filling every `[PENDING]` marker |
| 31 | No remaining `[PENDING]` markers in the PDF | **TECHNICAL ACTION REQUIRED** | `grep -n pending jors/paper.tex` must return only the macro definition |
| 32 | Metadata consistency: version in `pyproject.toml`, `CHANGELOG.md`, tag, GitHub Release, PyPI, Zenodo, `CITATION.cff`, paper | **TECHNICAL ACTION REQUIRED** | Source metadata agree on 1.1.0 now; tag/release/PyPI/Zenodo do not exist yet; `CITATION.cff` still lists the v1.0.0 DOI under 1.1.0 (fix in the release commit) |

## APC and waiver

- Current Software Metapaper APC: **not verified**. The official JORS page
  could not be opened on 27 September 2026. Web-search extracts confirm that
  JORS charges an Article Publication Charge on acceptance, that waivers or
  discounts can be requested, that waiver requests must be made as part of
  the submission information (e.g. the cover letter), and that editorial
  decisions are independent of ability to pay. A Ubiquity Press marketing
  page mentions a generic starting APC; it is not JORS-specific and is not
  recorded here as the fee. **Author action:** read the current fee on
  <https://openresearchsoftware.metajnl.com/about/submissions> (or the
  journal's APC page) and record it here, noting that applicable tax (VAT)
  may be added.
- Waiver: not requested. The cover letter contains no waiver request.
- **Author decision:** `APC funding available` / `waiver requested` /
  `undecided` ← currently **undecided**.

## Author confirmation items (minimal wording)

1. Funding: "This work received no specific funding." — or funder + grant number.
2. Competing interests: "The author has no competing interests to declare." — or the declaration.
3. AI: model names/versions for Claude Code and for Codex; AI use during April–June 2026: yes/no (and what).
4. Current affiliation and e-mail for correspondence.
5. Not under consideration elsewhere: confirmed on (date), JOSS not submitted.
6. Five reviewers chosen; e-mails copied from official pages.
7. APC decision.
