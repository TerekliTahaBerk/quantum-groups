# JORS submission checklist

**SUBMITTED 28 September 2026.** The manuscript was submitted to the
*Journal of Open Research Software*, Software Metapapers section (submission
#798 in the journal's OJS system), with `paper.pdf` as the manuscript file,
`paper.tex` and `references.bib` as supplementary source files (for review),
and `figures/figure1_workflow.png` as the figure. The cover-letter text,
five recommended reviewers, and APC waiver request were entered in their own
OJS fields (Comments for the Editor / Recommended reviewers), not attached
as a separate file. Everything below is the pre-submission record kept for
reference.

Status **27 September 2026**, verified against the current repository and
the live JORS rules as far as they could be retrieved (`PREFLIGHT.md` §2).

Labels: **READY** · **AUTHOR ACTION REQUIRED** ·
**CREDENTIAL/AUTHORIZATION REQUIRED** · **BLOCKED** (cannot proceed until
another item is done)

A GitHub Release/tag is not strictly required by the JORS rules (a
repository with a persistent identifier for the described version, i.e. the
Zenodo deposit, is what matters) — but the author has in fact created one:
`v1.1.0`, published 28 Sep 2026, commit `103d5384e70e8b0b746b296a0bdbd2d156ba8dde`.
A stray `v1.0.1` tag was suspected on the same commit from an earlier,
misnamed release attempt; re-checked 28 September 2026 via `git ls-remote
--tags origin` — no such tag exists on the remote (only `v1.0.0` and
`v1.1.0`). Nothing to delete.

| # | Requirement | Status | Evidence / action |
|---|---|---|---|
| 1 | Substantive research-software contribution; no invented novelty | READY | Paper frames the contribution as software/method; no new mathematics claimed |
| 2 | Public repository, open issue tracker | READY | https://github.com/TerekliTahaBerk/quantum-groups |
| 3 | OSI licence | READY | MIT (`LICENSE`, `License-Expression: MIT`) |
| 4 | Easy installation, documented | READY | Two install commands in the paper; wheel install tested on Linux/macOS/Windows in CI |
| 5 | Package-registry installation (PyPI) | READY | Published by the author 28 Sep 2026 via Trusted Publishing (`publish.yml`, `ref=103d5384e70e8b0b746b296a0bdbd2d156ba8dde`, `expected_version=1.1.0`). Verified independently from a clean venv the same day: `pip install quantum-group==1.1.0` installs, `__version__ == 1.1.0`, and `examples/sample_verification.py` from the snapshot commit matches its expected output byte for byte. https://pypi.org/project/quantum-group/1.1.0/ |
| 6 | Versioning; exact version identifiable | READY | 1.1.0 = commit `103d5384e70e8b0b746b296a0bdbd2d156ba8dde`, tagged as GitHub Release `v1.1.0` (published 28 Sep 2026); consistent in `pyproject.toml`, `CITATION.cff`, `CHANGELOG.md`, `__version__` |
| 7 | Repository with persistent identifier for the described version (archive) | READY | Published by the author 28 Sep 2026: Zenodo DOI [10.5281/zenodo.23015576](https://doi.org/10.5281/zenodo.23015576), archiving `git archive`/`v1.1.0` of commit `103d538`. Filled into `submission-facts.tex`, `CITATION.cff`, `README.md`, `CHANGELOG.md`. Content independently verified, see item 8 |
| 8 | Archive content equals the described code | READY | Download-and-diff run by the author 28 Sep 2026 (via a session with working Zenodo access, since this environment's egress policy blocks `zenodo.org`): downloaded `quantum-groups-v1.1.0.zip` from the Zenodo record, MD5 `2f6fafa8efb71a7f036f401ab6d8b370` matched the value Zenodo itself lists; compared file-by-file against `git archive` of `103d5384e70e8b0b746b296a0bdbd2d156ba8dde` (using GitHub's own `{owner}-{repo}-{short-sha}` zip prefix, which is what Zenodo's GitHub-integration archives actually use, not the `quantum-group-1.1.0/` prefix this file's own step 9 assumed) — 201 files on each side, `diff -r` empty, per-file hashes identical. `DISTRIBUTION.md` step 12 and the prefix note there should be corrected accordingly |
| 9 | Snapshot commit frozen with green CI | READY | All 9 CI jobs passed on `103d538` (re-verified via the GitHub API 28 Sep 2026); this is also the `v1.1.0` release commit; archive reference file and SHA-256 need updating in `DISTRIBUTION.md` (see below) |
| 10 | Template sections and fields | READY | Official `JORS_Template` (LaTeX `.cls`/`.tex` + `.docx`, both v0.2) obtained from the author 28 Sep 2026 and checked against `paper.tex` directly (previously only inferred from current articles, `PREFLIGHT.md` §3). Section headings now match exactly ("Funding statement", "Competing interests"); extra sections (Data Accessibility, Authors' Contributions, generative-AI disclosure) are additions the template does not forbid |
| 11 | Title | READY | Title case, no novelty claim |
| 12 | Abstract | READY | 143 words (updated 28 Sep 2026 to name the thesis-error catch), at the top of the range of current JORS articles (104–143) |
| 13 | Sample input and output | READY | Listing 1 = `examples/sample_verification.py`; expected output compared in CI and by `make -C jors check` |
| 14 | Quality control, supported systems, dependencies | READY | 202 tests (198 + 4 doctests); Python 3.10–3.13; minimum dependencies; Linux, macOS, Windows (CI) |
| 15 | Reuse potential and support | READY | Section (3) |
| 16 | Data Accessibility Statement | READY | "No research data were generated or analysed …" |
| 17 | Figures: cited, captioned, ≥300 dpi, uploaded separately, alt text | READY | Figure 1: 600-dpi PNG, EPS, PDF; alt text in `README.md` |
| 18 | Tables in text and cited | READY | Table 1 |
| 19 | References in citation order; DOIs/URLs | READY | 15 entries, all cited; de Graaf DOI author-confirmed (`33ae33c`). **Corrected 28 Sep 2026**: the official template's own words are "Harvard style ... citing them in the text with a number in square brackets", not Vancouver as earlier assumed without the template in hand. `paper.tex` now uses a custom biblatex style (`style=numeric` + custom entry drivers) producing exactly that: `Family, Initials Year. Title. Journal Vol(Issue): Pages. DOI: <url>`, numbered `[n]` in citation order |
| 20 | Not previously published | READY (re-confirm on the day) | Thesis and public JOSS draft disclosed; neither is prior journal publication |
| 21 | Not under consideration elsewhere; JOSS/JORS exclusivity | READY (re-check on the day) | Author confirmed 27 Sep 2026: JORS first; JOSS not submitted and will not be while JORS reviews |
| 22 | Affiliation | READY | Department of Mathematics, Yıldız Technical University, Istanbul, Türkiye (author, 27 Sep 2026) |
| 23 | Funding Information | READY | "This work received no specific funding." (author, 27 Sep 2026); also added to the JOSS draft |
| 24 | Competing Interests | READY | "The author has no competing interests to declare." (author, 27 Sep 2026) |
| 25 | Authors' Contributions; authorship | READY (sole author) | Supervisor in Acknowledgements only |
| 26 | Generative-AI disclosure | READY | Confirmed: no AI in April–June 2026; Claude Code (Claude Opus 5.5) only, for all publication-preparation work including the translation and the mathematical/technical audit; human review and validation. 28 Sep 2026: author confirmed Codex (OpenAI) was never used at any stage — the earlier text in `paper/paper.md`, `AUDIT.md`, `jors/paper.tex`, `jors/COVER_LETTER.md` and `jors/submission-facts.tex` that attributed the translation and audit to Codex was a mislabeling and has been corrected to Claude Code throughout |
| 27 | Five reviewers with e-mails | READY | Five chosen; author confirmed no conflicts (27 Sep 2026). 28 Sep 2026: Levandovskyy dropped (address unreachable after repeated automated attempts across three of his pages) and replaced with Max Horn (GAP/OSCAR, RPTU Kaiserslautern), whose address is plainly published on his page. All 5 addresses now confirmed directly from the reviewers' own official pages (`POTENTIAL_REVIEWERS.md`) and copied into `COVER_LETTER.md` |
| 28 | Cover letter | READY | `COVER_LETTER.md`; snapshot SHA, Zenodo DOI, APC, AI disclosure and all 5 reviewers filled in. Only the day-of-submission re-confirmations (venue exclusivity, JOSS status) remain, by design |
| 29 | APC | READY (waiver requested) | £824.00; author decided 28 Sep 2026 to request a full waiver (no funding, thesis-derived work). Waiver request text is in `COVER_LETTER.md`. The editor decides independently of ability to pay; a decline would mean either paying or withdrawing, not an automatic rejection |
| 30 | PDF without [PENDING] markers | READY | `make -C jors check` prints `OK` (verified 28 Sep 2026, after PyPI publication filled the last field, `\PyPIIdentifier`) |

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
- **Author decision (28 Sep 2026): waiver or discount requested.** Grounds:
  thesis-derived work, no specific funding (matches the Funding statement).
  The waiver request text is in `COVER_LETTER.md`, submitted with the
  manuscript as required. This is a request, not a guarantee — the editor's
  acceptance decision is independent of it, and a decline on the waiver
  itself would mean choosing to pay or withdrawing, not an automatic
  rejection of the paper.
