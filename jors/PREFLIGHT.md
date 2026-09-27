# JORS pre-submission verification record

Prepared **27 September 2026** on branch `claude/sleepy-darwin-o4mr5p`,
starting from `origin/main` = `05a81481e1d9e4e2e8937eea996d72e20cf5b8a8`.
This record states what was verified, how, and what is still open. Nothing
has been submitted to JORS or JOSS, and no tag, release, PyPI upload or
Zenodo deposit has been made.

**Verdict: NOT READY FOR SUBMISSION.** Hard blockers are listed in
[§8](#8-hard-blockers-and-author-actions).

## 1. How the JORS requirements were checked (and the limits of that check)

Date checked: **27 September 2026**.

The JORS website (`openresearchsoftware.metajnl.com`), the Ubiquity Press
site, arXiv, CTAN, Overleaf, Zenodo, doi.org, Crossref and all university
websites were **blocked by the network policy of the environment** used to
prepare this package (HTTP proxy refusals, recorded at the time). The
following sources were used instead:

| Source | What it established |
|---|---|
| Web-search extracts of the JORS *Submission Guidelines*, *Editorial Policies* and *About* pages (search engine, 27 Sep 2026) | Software must be in a public repository under an open licence; "easy to install and supports versioning", which "for most tools" means a package registry such as PyPI or conda; include the persistent identifier of the archive; Vancouver numeric referencing; all tables and figures referenced in the text; tables inside the document; figures uploaded separately at ≥150 dpi (300 dpi preferred); LaTeX submissions as PDF plus source; names and e-mail addresses of **five potential reviewers** and a **cover letter** in the *Comments for the Editor* box; preprints and public drafts are not prior publication; competing interests must be declared; APC waivers must be requested with the submission (e.g. in the cover letter). |
| Web-search extract of the Ubiquity Press *Policy on the Use of GenAI Tools* (`ubiquitypress.com/ai-policy`) | AI use beyond basic copy-editing and formatting must be explicitly declared; AI tools cannot be authors. |
| Three current JORS metapapers downloaded from the journal's public file store (`storage.googleapis.com/jnl-up-j-jors-files`): 10.5334/jors.523, jors.547, jors.587 (2025–2026) | Current published section structure: Introduction, Implementation and architecture, Quality control, Availability (Operating system, Programming language, Additional system requirements, Dependencies, List of contributors, Software location with archive/repository fields, Language), Reuse potential, Competing interests, Author contributions, References; title case in titles. |

The **official template file could not be downloaded**. The search extracts
contain two statements ("There is no template for submission ... you can
complete a document template" / reference to a LaTeX template in the Author
Guidelines). `paper.tex` therefore follows the JORS Software Metapaper
template's section and field headings exactly (listed in the header comment
of `paper.tex`), set in a plain `article` class with Vancouver references;
it does not reuse any template file. **Author action:** open
<https://openresearchsoftware.metajnl.com/about/submissions> and the
Software Metapaper template it links, and confirm that (a) the headings in
`paper.tex` match the current template and (b) nothing new is required
(e.g. an Author Contributions section, a word limit, an abstract limit —
the template historically asked for a ca. 100-word abstract; the current
abstract is 158 words). Record the result here.

The **APC amount could not be read from the official page**; see
`SUBMISSION_CHECKLIST.md` §APC.

## 2. Repository ground truth

| Item | Finding | How verified |
|---|---|---|
| Canonical branch | `origin/main` at `05a8148` (merge of PR 6). Local `main` in the session clone was stale (`4fce180`); all comparisons use `origin/main`. | `git fetch`, `git rev-parse` |
| Unmerged work | Branch `claude/determined-maxwell-7u3h0j` has one commit not on `main`: `33ae33c` (JOSS wording; de Graaf DOI "confirmed by the author against the ScienceDirect record"; removes the v1.0.0 DOI from 1.1.0 `CITATION.cff`). CI passed on it (run 28). | `git log origin/main..`, GitHub Actions |
| Tags / releases | One tag `v1.0.0` → commit `8dcfe99`; one GitHub Release "v1.0.0 — First release", published 2026-09-27T13:44:49Z. | `git ls-remote --tags`, GitHub API |
| Package version | `1.1.0` in `pyproject.toml`, `CITATION.cff`, `CHANGELOG.md` ("Unreleased"); `quantum_group.__version__` reads installed metadata → `1.1.0`. | files; installed wheel |
| Zenodo | DOI 10.5281/zenodo.22997681, recorded by the author in `855cade`, archives **v1.0.0 only**. `git diff v1.0.0 origin/main` changes all 13 modules present in v1.0.0 and adds two. **No archive of 1.1.0 exists.** The Zenodo record itself could not be opened (zenodo.org blocked). | git; repository records |
| PyPI | `https://pypi.org/pypi/quantum-group/json` → 404; same for `quantum_group`, `quantumgroup`, `quantum-groups`, `quantumgroups`, and on TestPyPI. The package is **not on PyPI**; the name is not taken by an existing project (PyPI may still refuse it at first upload). | `curl`, 27 Sep 2026 |
| Licence | MIT (`LICENSE`, © 2026 Taha Berk Terekli); `pyproject.toml` now uses SPDX `license = "MIT"`. | files |
| Issues / PRs | 0 issues; 6 PRs, all opened by the author's Claude Code sessions and merged by the author without review. | GitHub API |
| Commit history | 24 commits by the author (April–June 2026 development, September 2026 merges and edits); 12 commits authored by "Claude" on 27 Sep 2026, 11 with a `Co-Authored-By` trailer naming the model, `aed9cc8` without one. | `git log`, `git shortlog` |
| JOSS status | `paper/REVIEW_CHANGES.md` and `AUDIT.md` state that no JOSS submission or review exists; `paper/PREFLIGHT.md` judges JOSS submission not yet eligible (history/iteration gates). No JOSS review issue could be searched from this environment (GitHub search API returned 403; the JOSS review repository is outside this session's scope). | repository files |

## 3. Validation results (this session)

| Check | Result |
|---|---|
| `python -m pytest` (Python 3.12.3, SymPy 1.14.0, NetworkX 3.7, Matplotlib 3.11.2, Ubuntu 24.04 x86-64) | **202 passed** = 198 test cases in 10 files + 4 doctests (`__init__`, `linalg.kron`, `QuantumGroupSL2`, `utils.q_integer`), 12–14 s |
| Per file | audit_regressions 32, hopf 6, limits 9, r_matrix 7, relations 35, representations 37, supergroup_gl21 13, tensor 16, validation_and_linalg 40, visualization 3 |
| Build | `python -m build` → `quantum_group-1.1.0.tar.gz`, `quantum_group-1.1.0-py3-none-any.whl`; **no warnings** after the licence-metadata fix (before: setuptools deprecation of the licence table and classifier, removal deadline 2027-02-18) |
| Metadata | `twine check --strict` PASSED for both files; `Metadata-Version: 2.4`, `License-Expression: MIT`, `Requires-Python: >=3.10` |
| Clean install | Wheel installed into a fresh Python 3.10 venv with SymPy 1.10.1, NetworkX 2.6.3, Matplotlib 3.5.3, numpy<2 (the declared lower bounds); `examples/sample_verification.py` run from `/tmp` produced output **identical** to `examples/sample_verification_expected.txt`, as did Python 3.12 / SymPy 1.14 |
| Paper listing | Listing 1 in `paper.tex` is byte-identical to the body of `examples/sample_verification.py`; the printed output equals the expected-output file (checked by script) |
| Benchmarks | Re-run of `benchmarks/benchmark.py --repeats 3 --max-n 5` to a scratch directory (committed results unchanged): Python 3.12.3/SymPy 1.14, same Xeon type: local YBE on V⊗4 1.09 s (recorded 1.56 s), all R_ij on V⊗5 9.72 s (recorded 14.62 s). Peak RSS for the n = 5 case ≈ 112 MB. |
| CI on `96e50e4` ([run 29](https://github.com/TerekliTahaBerk/quantum-groups/actions/runs/36335566917)) | **All 9 jobs passed**: pytest 3.10/3.11/3.12/3.13 ✔, minimum dependencies ✔, wheel + quickstart + sample-output diff ✔, cross-platform (wheel install, both examples with output comparison, full suite; Python 3.12) on ubuntu-latest ✔, macos-latest ✔, windows-latest ✔. The Availability section states macOS/Windows as tested on this basis. Re-check CI on the release commit. |

## 4. Changes made to shared repository files

| File | Change | Why |
|---|---|---|
| `examples/sample_verification.py`, `examples/sample_verification_expected.txt` (new) | Short reviewer example printing each result, with an ungraded-swap negative control; exact copy of Listing 1 | JORS reviewers check sample input/output; the quickstart only asserts |
| `.github/workflows/tests.yml` | Wheel job also diffs the sample output; new `cross-platform` job (Ubuntu/macOS/Windows: wheel install, both examples, full suite) | Support the Availability claims with evidence |
| `.github/workflows/publish.yml` (new) | Trusted-Publishing upload to PyPI on a *published GitHub Release* only; tag/version check; no stored token | Registry installation without secrets; inert until the author configures PyPI |
| `pyproject.toml` | SPDX licence expression, `license-files`, licence classifier removed, `setuptools>=77` | Remove deprecation warnings that will become errors in 2027 |
| `CHANGELOG.md`, `README.md`, `CONTRIBUTING.md`, `.gitignore` | Document the above; ignore biblatex auxiliary files | Consistency |

`paper/` (the JOSS manuscript) was **not modified**.

## 5. Bibliography

Rendered with `biblatex-vancouver` (`sorting=none`: numbered by first
citation). 15 entries, all cited, no missing or unused keys (biber reports
no warnings).

| Key | Status |
|---|---|
| meurer2017sympy | Verified: citation text in SymPy's PyPI project description (27 Sep 2026). |
| jimbo1985, jimbo1986, kassel1995, drinfeld1987, celik2021 | As verified for the JOSS bibliography (Springer/ADS, ICM proceedings records, ScienceDirect listing and the original Çelik–Çelik PDF, see `paper/paper.bib` and `AUDIT.md` §11); not re-resolvable here (doi.org blocked). Issue number of Jimbo 1985 omitted because it was never verified. |
| gap (4.16.1), sagemath (10.9, concept DOI 10.5281/zenodo.8042260), quagroup (1.8.4) | Versions as re-checked on 27 Sep 2026 for the JOSS bibliography (GAP `CHANGES.md`, Sage `CITATION.cff`/`VERSION.txt`, QuaGroup `PackageInfo.g`). |
| degraaf2001 | Journal/volume/issue/pages from QuaGroup's `doc/quagroup.bib`. **DOI 10.1006/jsco.2001.0479**: stated as author-confirmed against ScienceDirect in unmerged commit `33ae33c`; it could **not be resolved independently here** (doi.org, Crossref, ScienceDirect blocked; web search found no record). **Author action:** open https://doi.org/10.1006/jsco.2001.0479 and confirm it lands on this article before submission. |
| bkk2000 | JAMS 13(2):295–331 and arXiv math/9810092 from SageMath's reference database (JOSS record). The JAMS DOI was not verified and is therefore **not given**; the arXiv identifier is. |
| hagberg2008networkx, hunter2007matplotlib | Standard citations requested by the NetworkX and Matplotlib projects (authors confirmed against installed package metadata); DOI/URL not re-resolved here. |
| pytest | Author list from the installed pytest 9.1.1 metadata; URL of the project repository. |
| terekli2026thesis | From `thesis/thesis_ytu.tex` (title, department, date June 2026); URL is the repository folder containing the submitted PDF. |

Stale verification comments of `paper/paper.bib` were not copied; the
status of each entry is recorded only here.

## 6. Manuscript build

`cd jors && latexmk -pdf paper.tex` with TeX Live 2023 (Ubuntu 24.04
packages), biber 2.19, `biblatex-vancouver`: **builds cleanly** — no
undefined references or citations, no overfull or underfull boxes, no biber
warnings. 11 pages (A4, 11 pt). All mathematics renders (checked visually
page by page). Figure 1 is embedded as vector PDF. The PDF intentionally
shows red **[PENDING: …]** markers for the fields that cannot be completed
yet (archive DOI, dates, PyPI, confirmations); it must not be submitted
while any marker remains.

Figure 1 (`figures/figure1_workflow.*`): original TikZ source; vector PDF
(134 KB) and EPS (293 KB) line art; PNG 3824 × 1264 px at **600 dpi**
(338 KB), well above the 150/300 dpi requirement. Caption numbered, cited in
the text; alt text in `README.md`.

## 7. Reviewer simulation (JORS software review questions)

Performed from the metapaper alone, as an independent reviewer would.

| Question | Answer now | After the author actions |
|---|---|---|
| Can I find the software? | Yes: GitHub URL in *Code repository*. | Also PyPI and Zenodo. |
| Can I install it? | Yes from GitHub (`pip install "git+https://github.com/TerekliTahaBerk/quantum-groups"` or a clone). **Not** via a package registry: `pip install quantum-group` fails today. | Yes, via PyPI. |
| Can I identify the correct version? | Partly: the paper says 1.1.0 and `pyproject.toml` says 1.1.0, but **no v1.1.0 tag or release exists**; `main` will move on. | Yes: tag, release, PyPI and DOI all say 1.1.0. |
| Can I get the archived version via a persistent identifier? | **No.** The only DOI (10.5281/zenodo.22997681) archives v1.0.0, which lacks most of what the paper describes. | Yes: v1.1.0 version DOI. |
| Can I run sample input? | Yes: Listing 1 = `examples/sample_verification.py`, runs from any directory against the installed package. | — |
| Do I obtain the expected output? | Yes: identical output on Linux (local, CI), macOS (CI), Windows (CI) and with the oldest supported dependencies. | — |
| Is the licence clear? | Yes: MIT, in the paper, `LICENSE` and package metadata. | — |
| Are the limitations clear? | Yes: *Scope and limitations* paragraph, *Where reuse requires new work*, *Scaling*. | — |
| Is the implementation understandable? | Yes: layered architecture, Figure 1, one paragraph per design decision with API names. | — |
| Is quality control convincing? | Yes: 202 tests, CI matrix, negative controls, independent re-derivations, source-entry tests (Table 1). Weakness: tests were written by the developer (and AI-assisted), with no external review or users yet. | — |
| Are support mechanisms obvious? | Yes: issue tracker, `CONTRIBUTING.md`, best-effort maintenance statement. | — |
| Can I reasonably reuse or extend it? | Yes for the listed scenarios; the boundary to substantial new work is stated. | — |

Problems found and fixed during the simulation: no example with visible
output (added); cross-platform claims unsupported (CI job added);
deprecated packaging metadata (fixed); the planned figure was cramped
(redrawn). Problems that cannot be fixed without the author: version
archive, registry publication, confirmations (§8).

## 8. Hard blockers and author actions

**Hard blockers (submission must not happen until all are resolved):**

1. **JOSS/JORS exclusivity.** No JOSS submission exists according to the
   repository. Immediately before submitting to JORS, confirm that the
   software paper is not under consideration at JOSS or anywhere else; if a
   JOSS submission is made first, JORS submission is **BLOCKED** until that
   process has ended or been withdrawn. Decide which venue to use first; a
   JORS publication may affect later JOSS eligibility (check JOSS's policy
   on previously published software papers).
2. **No archive of the submitted version.** Release v1.1.0 and obtain its
   Zenodo version DOI (`RELEASE_STEPS.md`). Never use 10.5281/zenodo.22997681
   for 1.1.0.
3. **No registry installation.** Publish `quantum-group` 1.1.0 to PyPI
   (`RELEASE_STEPS.md` §1–3) and record here the exact command, version and
   date of a successful `python -m pip install quantum-group` in a clean
   environment.
4. **Funding and competing-interest statements** unconfirmed.
5. **AI disclosure:** exact model names/versions for Claude Code and Codex,
   and whether AI was used before September 2026, must be supplied by the
   author (the model recorded in the commit trailers can be read with
   `git log --format='%h %(trailers:key=Co-Authored-By)'`).
6. **Five reviewers with verified e-mail addresses** (see
   `POTENTIAL_REVIEWERS.md`; no address could be verified here).
7. **Official template/guideline re-check** (§1) and the current APC.

**Other author actions:** confirm current affiliation; confirm the de Graaf
DOI; decide on commit `33ae33c`; fill every `[PENDING]` marker and rebuild
the PDF; re-run the overlap check in `OVERLAP_REVIEW.md` if the text
changes substantially.

## 9. Reproducing this record

```sh
python -m pytest                                   # 202 passed
python -m build && python -m twine check --strict dist/*
python examples/sample_verification.py | diff - examples/sample_verification_expected.txt
cd jors && latexmk -pdf paper.tex                  # needs TeX Live + biber + biblatex-vancouver
curl -s -o /dev/null -w '%{http_code}\n' https://pypi.org/pypi/quantum-group/json
```
