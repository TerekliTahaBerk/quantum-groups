# JORS submission checklist

Status **27 September 2026**, verified against the current repository and
the live JORS rules as far as they could be retrieved (`PREFLIGHT.md` §2).

Labels: **READY** · **AUTHOR ACTION REQUIRED** ·
**CREDENTIAL/AUTHORIZATION REQUIRED** · **BLOCKED** (cannot proceed until
another item is done)

Not required and therefore not listed as blockers: a GitHub Release, a Git
tag (the current rules ask for a repository with a persistent identifier
for the described version, which the Zenodo deposit of the snapshot commit
provides).

| # | Requirement | Status | Evidence / action |
|---|---|---|---|
| 1 | Substantive research-software contribution; no invented novelty | READY | Paper frames the contribution as software/method; no new mathematics claimed |
| 2 | Public repository, open issue tracker | READY | https://github.com/TerekliTahaBerk/quantum-groups |
| 3 | OSI licence | READY | MIT (`LICENSE`, `License-Expression: MIT`) |
| 4 | Easy installation, documented | READY | Two install commands in the paper; wheel install tested on Linux/macOS/Windows in CI |
| 5 | Package-registry installation (PyPI) | CREDENTIAL/AUTHORIZATION REQUIRED | Name `quantum-group` unclaimed (404). Build, `twine check`, clean install and the manual Trusted-Publishing workflow are ready. Author: pending publisher, `pypi` environment, dispatch with the snapshot SHA (`DISTRIBUTION.md` §A, C). READY only after `pip install quantum-group==1.1.0` works publicly |
| 6 | Versioning; exact version identifiable | BLOCKED (by 9) | Version 1.1.0 is consistent in `pyproject.toml`, `CITATION.cff`, `CHANGELOG.md`, `__version__`, paper. The identifying snapshot commit is frozen after the reserved DOI is inserted |
| 7 | Repository with persistent identifier for the described version (archive) | CREDENTIAL/AUTHORIZATION REQUIRED | Required by the repository criteria (`PREFLIGHT.md` §2, §4). Manual Zenodo deposit of `git archive` of the snapshot, no GitHub Release (`DISTRIBUTION.md` §A3, D) |
| 8 | Archive content equals the described code | BLOCKED (by 7) | Download-and-diff procedure in `DISTRIBUTION.md` step 12 |
| 9 | Snapshot commit frozen with green CI | BLOCKED (by 7: reserved DOI) | Package source already frozen (`PREFLIGHT.md` §1 tree hashes) |
| 10 | Template sections and fields | READY | `PREFLIGHT.md` §3 (official template file unobtainable; headings as in current articles) |
| 11 | Title | READY | Title case, no novelty claim |
| 12 | Abstract | READY | 138 words, within the range of current JORS articles |
| 13 | Sample input and output | READY | Listing 1 = `examples/sample_verification.py`; expected output compared in CI and by `make -C jors check` |
| 14 | Quality control, supported systems, dependencies | READY | 202 tests (198 + 4 doctests); Python 3.10–3.13; minimum dependencies; Linux, macOS, Windows (CI) |
| 15 | Reuse potential and support | READY | Section (3) |
| 16 | Data Accessibility Statement | READY | "No research data were generated or analysed …" |
| 17 | Figures: cited, captioned, ≥300 dpi, uploaded separately, alt text | READY | Figure 1: 600-dpi PNG, EPS, PDF; alt text in `README.md` |
| 18 | Tables in text and cited | READY | Table 1 |
| 19 | Vancouver references in citation order; DOIs/URLs | READY | 15 entries, all cited; de Graaf DOI author-confirmed (`33ae33c`) |
| 20 | Not previously published | READY (re-confirm on the day) | Thesis and public JOSS draft disclosed; neither is prior journal publication |
| 21 | Not under consideration elsewhere; JOSS/JORS exclusivity | AUTHOR ACTION REQUIRED | Repository records: JOSS not submitted. Author to confirm JORS goes first and JOSS stays unsubmitted while JORS reviews |
| 22 | Affiliation | AUTHOR ACTION REQUIRED | `submission-facts.tex` `\AuthorAffiliation` |
| 23 | Funding Information | AUTHOR ACTION REQUIRED | `\FundingText`; the repository contains no funding information |
| 24 | Competing Interests | AUTHOR ACTION REQUIRED | `\CompetingText` |
| 25 | Authors' Contributions; authorship | READY (sole author) | Supervisor in Acknowledgements only |
| 26 | Generative-AI disclosure | AUTHOR ACTION REQUIRED | Model names, thesis-period use, review confirmation (`\ClaudeModel`, `\CodexModel`, `\ThesisPeriodAI`, `\AIReviewStatement`) |
| 27 | Five reviewers with e-mails | AUTHOR ACTION REQUIRED | Five chosen and screened (`POTENTIAL_REVIEWERS.md`); each address must be copied from the official page (pages unreachable here) |
| 28 | Cover letter | BLOCKED (by 21–27, APC) | `COVER_LETTER.md`, bracketed fields only |
| 29 | APC | AUTHOR ACTION REQUIRED | See below |
| 30 | PDF without [PENDING] markers | BLOCKED (by 5–9, 22–26) | `make -C jors check` must print `OK` |

## APC

- Current Software Metapaper APC: **not retrievable** on 27 September 2026
  (journal and publisher sites blocked; no search extract states the
  amount). Confirmed from extracts: an Article Publication Charge is due on
  acceptance; waivers/discounts exist; a waiver request must be part of the
  submission information (e.g. the cover letter); editorial decisions are
  independent of ability to pay. Tax (VAT) may be added depending on the
  payer. **Author:** read the amount on the journal site and note it here.
- No waiver has been requested.
- **Author decision:** `will pay` / `waiver or discount requested` /
  `institution or funder pays` — currently **undecided**.
