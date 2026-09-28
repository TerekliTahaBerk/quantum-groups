# JORS submission checklist

Status **27 September 2026**, verified against the current repository and
the live JORS rules as far as they could be retrieved (`PREFLIGHT.md` §2).

Labels: **READY** · **AUTHOR ACTION REQUIRED** ·
**CREDENTIAL/AUTHORIZATION REQUIRED** · **BLOCKED** (cannot proceed until
another item is done)

A GitHub Release/tag is not strictly required by the JORS rules (a
repository with a persistent identifier for the described version, i.e. the
Zenodo deposit, is what matters) — but the author has in fact created one:
`v1.1.0`, published 28 Sep 2026, commit `103d5384e70e8b0b746b296a0bdbd2d156ba8dde`.
A stray `v1.0.1` tag on the same commit (its Release was deleted before
`v1.1.0` was created correctly) should be deleted before submission.

| # | Requirement | Status | Evidence / action |
|---|---|---|---|
| 1 | Substantive research-software contribution; no invented novelty | READY | Paper frames the contribution as software/method; no new mathematics claimed |
| 2 | Public repository, open issue tracker | READY | https://github.com/TerekliTahaBerk/quantum-groups |
| 3 | OSI licence | READY | MIT (`LICENSE`, `License-Expression: MIT`) |
| 4 | Easy installation, documented | READY | Two install commands in the paper; wheel install tested on Linux/macOS/Windows in CI |
| 5 | Package-registry installation (PyPI) | CREDENTIAL/AUTHORIZATION REQUIRED | Author approved publication. Name still unclaimed as of 27 Sep 2026. Needs: pending publisher on the author's PyPI account, `pypi` environment (`DISTRIBUTION.md` §A1–A2, done independently of the release), then *Run workflow* with `ref=103d5384e70e8b0b746b296a0bdbd2d156ba8dde`, `expected_version=1.1.0`. READY only after a public `pip install quantum-group==1.1.0` succeeds |
| 6 | Versioning; exact version identifiable | READY | 1.1.0 = commit `103d5384e70e8b0b746b296a0bdbd2d156ba8dde`, tagged as GitHub Release `v1.1.0` (published 28 Sep 2026); consistent in `pyproject.toml`, `CITATION.cff`, `CHANGELOG.md`, `__version__` |
| 7 | Repository with persistent identifier for the described version (archive) | CREDENTIAL/AUTHORIZATION REQUIRED | Author will do this directly in Zenodo (28 Sep 2026): open the `v1.0.0` record's *New version*, reserve a DOI without publishing yet, send the DOI back for `CITATION.cff`/`submission-facts.tex`, then publish. Upload either the `v1.1.0` GitHub Release tarball or `git archive` of `103d538` — both have identical content; metadata from `zenodo-metadata.json` (needs its snapshot fields updated to `103d538`, see `DISTRIBUTION.md`) |
| 8 | Archive content equals the described code | BLOCKED (by 7) | Download-and-diff procedure in `DISTRIBUTION.md` step 12, against `103d538` |
| 9 | Snapshot commit frozen with green CI | READY | All 9 CI jobs passed on `103d538` (re-verified via the GitHub API 28 Sep 2026); this is also the `v1.1.0` release commit; archive reference file and SHA-256 need updating in `DISTRIBUTION.md` (see below) |
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
| 21 | Not under consideration elsewhere; JOSS/JORS exclusivity | READY (re-check on the day) | Author confirmed 27 Sep 2026: JORS first; JOSS not submitted and will not be while JORS reviews |
| 22 | Affiliation | READY | Department of Mathematics, Yıldız Technical University, Istanbul, Türkiye (author, 27 Sep 2026) |
| 23 | Funding Information | READY | "This work received no specific funding." (author, 27 Sep 2026); also added to the JOSS draft |
| 24 | Competing Interests | READY | "The author has no competing interests to declare." (author, 27 Sep 2026) |
| 25 | Authors' Contributions; authorship | READY (sole author) | Supervisor in Acknowledgements only |
| 26 | Generative-AI disclosure | READY | Confirmed: no AI in April–June 2026; Claude Code (Claude Opus 5.5) only, for all publication-preparation work including the translation and the mathematical/technical audit; human review and validation. 28 Sep 2026: author confirmed Codex (OpenAI) was never used at any stage — the earlier text in `paper/paper.md`, `AUDIT.md`, `jors/paper.tex`, `jors/COVER_LETTER.md` and `jors/submission-facts.tex` that attributed the translation and audit to Codex was a mislabeling and has been corrected to Claude Code throughout |
| 27 | Five reviewers with e-mails | AUTHOR ACTION REQUIRED (1 of 5 only) | Five chosen; author confirmed no conflicts (27 Sep 2026). 28 Sep 2026: 4 of 5 addresses confirmed directly from the reviewers' own official pages (`POTENTIAL_REVIEWERS.md`) — Schilling, Thiéry, Regelskis, Zinn-Justin. Levandovskyy's address still could not be fetched (page returned no visible address); author must open his official Kassel page directly before submitting |
| 28 | Cover letter | BLOCKED (by 26, 27, APC, snapshot/DOI) | `COVER_LETTER.md`, bracketed fields only |
| 29 | APC | AUTHOR ACTION REQUIRED | See below |
| 30 | PDF without [PENDING] markers | BLOCKED (by 5, 7, 26) | `make -C jors check` must print `OK` |

## APC

- Current Software Metapaper APC: **£824.00**, confirmed 28 September 2026
  directly from `openresearchsoftware.metajnl.com/about/submissions` (fetched
  successfully; the site was unreachable from the environment that wrote the
  earlier version of this file). The page adds: "Tax will be added to all
  fees charged, when applicable (VAT/Sales tax or other applicable taxes)."
  About 12% of APC revenue is retained to fund the waiver programme, and
  authors without institutional funding may request a reduction or waiver.
  A third-party aggregator site (`journalsearches.com`) separately reports
  "around 350 GBP", which does not match the journal's own page; treat that
  figure as stale/unreliable and use £824.00, re-checking the official page
  once more on the actual submission day in case the fee schedule changed.
- No waiver has been requested.
- **Author decision:** `will pay` / `waiver or discount requested` /
  `institution or funder pays` — currently **undecided**.
