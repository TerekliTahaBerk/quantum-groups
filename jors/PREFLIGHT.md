# JORS pre-submission verification record

Rewritten **27 September 2026** from the current repository state; earlier
versions of this file are superseded. Nothing has been submitted to JORS or
JOSS, nothing has been published to PyPI or Zenodo, and no tag or GitHub
Release has been created (by the author's decision, 1.1.0 gets neither).

## 1. Repository topology (fetched 27 Sep 2026)

| Ref | SHA | Content |
|---|---|---|
| `origin/main` | `05a81481e1d9` | Merge of PR 6 (1.1.0 code, JOSS draft) |
| `claude/determined-maxwell-7u3h0j` | `33ae33c2484505b7d8dbe61a34b32f8e78a012c8` | JOSS wording, de Graaf DOI, v1.0.0 DOI removed from 1.1.0 `CITATION.cff` — **merged into this branch** (merge commit after `0c36fb2`) |
| `claude/sleepy-darwin-o4mr5p` (this branch) | see `git log` | JORS package (`96e50e4`, `0c36fb2`) + `33ae33c` + no-release distribution work |
| `claude/happy-lamport-lq2yqj` | — | fully contained in `main` |
| tag `v1.0.0` | `8dcfe99` | historical; untouched. Only GitHub Release: "v1.0.0 — First release" (2026-09-27T13:44:49Z); untouched |

Package source identity: `quantum_group/` tree `804d66f83a1d`, `tests/` tree
`a2a4fdc80bf4`, both identical to `origin/main`; `pyproject.toml` blob
`b17aa2bbc012` (licence metadata changed in `96e50e4`, version 1.1.0). Any
later snapshot commit must keep these hashes unless the change is deliberate
and re-validated (`git rev-parse <SHA>:quantum_group`).

## 1a. JORS submission software snapshot

`892dfaee23644ede78d940051eb3a20c9e6a5918` (`892dfae`), committed
2026-09-27T17:48:22Z; version 1.1.0; package source trees identical to those
listed above; 202 tests passed locally on it; CI run 33 (§7). No tag and no
GitHub Release. PyPI and Zenodo must be built from this commit; later
commits on the branch change only `jors/` (excluded from `git archive`).
Archive reference: `git archive --format=zip --prefix=quantum-group-1.1.0/
892dfae…` = 236 files, 13,011,184 bytes, SHA-256
`2e2621916eb5c9d85b72e7f9a3be9a0c6f1df7d1f714f307a39a24a5a7c40984`
(git 2.43.0; deterministic on repeat).

## 2. JORS rules: sources and retrieval (27 Sep 2026)

The JORS site, the Ubiquity Press site, Zenodo, doi.org, Crossref,
Software Heritage and university sites are **blocked by the network policy
of the preparation environment** (proxy refusal; retried on 27 Sep 2026).
Rules were therefore taken from search-engine extracts of the live pages
and from three current JORS articles (10.5334/jors.523, .547, .587;
2025–2026) downloaded from the journal's public file store. The official
template file could not be downloaded; see §3.

| Rule (live source, as extracted) | Consequence for this submission |
|---|---|
| *About*: the described version must be available in **at least one repository** meeting the criteria; *ideally* both a source-code repository and a preservation repository | GitHub alone is not sufficient if it fails the criteria below |
| *About/Editorial policies*: repositories must be sustainable and **provide persistent identifiers** (DOI, handle, ARK); a good repository gives "a unique, persistent identifier which references a particular version" | GitHub and PyPI do not issue persistent identifiers → a PID-issuing archive (Zenodo) is **required in substance**. The reviewer-form phrasing "if the Archive section is filled out" does not remove this. All three current JORS articles list a Zenodo archive. |
| Software "easy to install and supports versioning", for most tools via a package registry such as PyPI or conda | PyPI publication of 1.1.0 expected |
| Vancouver numeric references; tables in the text; figures uploaded separately, ≥150 dpi (300 preferred); LaTeX: PDF plus source | Done (§6) |
| Suggested structure: Abstract, Main text, **Data Accessibility**, Ethics (if relevant), Acknowledgements, **Funding Information**, **Competing Interests**, **Authors' Contributions**, References | All present in `paper.tex` (added in this revision) |
| Editorial policies, Data Policy: a **Data Accessibility Statement** before the references | Added: no research data were generated or analysed |
| Authorship per ICMJE-derived criteria; all authors consent | Sole author; supervisor acknowledged only |
| Ubiquity Press GenAI policy: AI use beyond basic copy-editing must be declared (ideally in Methods); AI cannot be an author | "Use of generative AI" section; model names from the author |
| Preprints and public drafts are not prior publication | Public JOSS draft disclosed, not prior publication |
| Five potential reviewers (names + e-mails) and a cover letter in *Comments for the Editor*; APC waiver requests with the submission | `POTENTIAL_REVIEWERS.md`, `COVER_LETTER.md` |
| APC amount | **Not retrievable** (no extract states the amount) |

## 3. Template compliance

Section and field headings follow the JORS Software Metapaper template as
used by current articles: (1) Overview — Title, Paper Authors, Paper Author
Roles and Affiliations, Abstract, Keywords, Introduction, Implementation
and architecture, Quality control; (2) Availability — Operating system,
Programming language, Additional system requirements, Dependencies, List of
contributors, Software location (Archive, Code repository, plus Package
registry as in jors.523), Language; (3) Reuse potential; then the statements
of §2. The layout is a plain LaTeX `article` because the official template
file could not be obtained; JORS typesets accepted papers itself, and the
guidelines accept PDF + LaTeX source. Title case as in current articles.
Abstract **138 words** as rendered (current articles: 104–143 words; the historical
"ca. 100 words" instruction could not be confirmed as current).

## 4. Archive decision

**Required** (see §2). Chosen mechanism, consistent with "no GitHub
Release": a **manual Zenodo software deposit** of
`git archive --format=zip --prefix=quantum-group-1.1.0/ <snapshot SHA>`,
preferably as *New version* of the existing v1.0.0 Zenodo record (same
concept DOI, no GitHub involvement), with a DOI reserved before the
snapshot commit so that `CITATION.cff` in the archive already carries it.
`jors/` is `export-ignore`d so the archive holds software only. Procedure:
`DISTRIBUTION.md` §A3, B, D; metadata: `zenodo-metadata.json`. Not
executed: requires the author's Zenodo account and approval.

## 5. Validation results (commit `86f794b`, package source identical to `main`)

| Check | Result |
|---|---|
| `python -m pytest` (Python 3.12.3, SymPy 1.14.0, NetworkX 3.7, Matplotlib 3.11.2, Ubuntu 24.04 x86-64) | **202 passed** = 198 test cases + **4 doctests** |
| Per file | audit_regressions 32, hopf 6, limits 9, r_matrix 7, relations 35, representations 37, supergroup_gl21 13, tensor 16, validation_and_linalg 40, visualization 3 |
| `python -m build` | `quantum_group-1.1.0.tar.gz`, `quantum_group-1.1.0-py3-none-any.whl`, **0 warnings** |
| `twine check --strict` | PASSED (both) |
| Wheel contents | the 15 modules of `quantum_group/` + metadata (`License-Expression: MIT`, `Requires-Python: >=3.10`) |
| Clean install | fresh venv (Python 3.12), wheel only; `quantum_group.__version__` = `1.1.0`, imported from site-packages; quickstart passed; sample output **identical** to `examples/sample_verification_expected.txt` (run from outside the repository). Also identical with SymPy 1.10.1 / NetworkX 2.6.3 / Matplotlib 3.5.3 on Python 3.10 (earlier today, same package source). |
| `compileall`, `git diff --check` | clean |
| `ruff --select F,E9` | 9 pre-existing findings (7 unused imports, 1 f-string without placeholders, 1 unused variable), none new, no syntax/runtime errors; left unchanged to avoid touching reviewed package code |
| Manuscript checks (`make -C jors check`) | Listing 1 = `examples/sample_verification.py`; printed output = expected file; **fails only on the [PENDING] markers** listed in §8 |
| CI, run 31 on `86f794b` | see §7 |

## 6. Manuscript build

`make -C jors pdf` (TeX Live 2023, biber 2.19, biblatex-vancouver): builds
with no undefined references, no overfull/underfull boxes, no biber
warnings; 11 pages A4. 15 references, all cited, numbered by first citation.
Figure 1: TikZ original, PDF/EPS vector, PNG 3824 × 1264 px at 600 dpi;
cited; alt text in `README.md`. Table 1 cited.

Bibliography status: SymPy verified from its PyPI project description;
Jimbo 1985/1986, Kassel, Drinfeld, Çelik–Çelik as verified for the JOSS
bibliography; GAP 4.16.1, SageMath 10.9, QuaGroup 1.8.4 as re-checked on
27 Sep 2026 for the JOSS bibliography; **de Graaf 2001, DOI
10.1006/jsco.2001.0479: author-confirmed against the ScienceDirect record
(commit `33ae33c`)**; not re-resolvable from this environment, treated as
resolved on the author's instruction. Benkart–Kang–Kashiwara given with
arXiv id (JAMS DOI not verified, so not given).

## 7. CI

| Commit | Run | Result |
|---|---|---|
| `96e50e4` | 29 | all 9 jobs passed (pytest 3.10/3.11/3.12/3.13, minimum dependencies, wheel + examples, Linux/macOS/Windows) |
| `0c36fb2` | 30 | passed |
| `86f794b` | [31](https://github.com/TerekliTahaBerk/quantum-groups/actions/runs/36337629367) | passed (all 9 jobs, incl. macOS and Windows) |
| `892dfae` (snapshot) | [33](https://github.com/TerekliTahaBerk/quantum-groups/actions/runs/36338318144) | **passed, all 9 jobs** (pytest 3.10–3.13, minimum dependencies, wheel + examples, Linux, macOS, Windows) |

The final snapshot commit must itself show green CI before PyPI/Zenodo.

## 8. Remaining open items (current, not inherited)

| Item | Class | Why it cannot be closed here |
|---|---|---|
| Codex use/model (answer "none" conflicts with the repository record) | AUTHOR ACTION REQUIRED | one clarification; all other declarations were confirmed on 27 Sep 2026 and are in `submission-facts.tex` |
| Reviewer e-mails (5) | AUTHOR ACTION REQUIRED | official pages unreachable here; the search index gave conflicting values |
| APC amount and choice | AUTHOR ACTION REQUIRED | amount not retrievable; the choice was left unfilled in the author's answers |
| Zenodo DOI reservation, deposit, publication | CREDENTIAL/AUTHORIZATION REQUIRED | author's Zenodo account; irreversible |
| PyPI publication of `quantum-group` 1.1.0 | CREDENTIAL/AUTHORIZATION REQUIRED | pending-publisher setup on the author's PyPI account; environment approval; name still unclaimed (404 on 27 Sep 2026) |
| Merge to `main` | AUTHOR ACTION REQUIRED | `workflow_dispatch` is only offered for workflows on the default branch |
| Snapshot SHA/date in the paper | READY | filled (`892dfae`, 27 September 2026) |
| Venue exclusivity re-check on the submission day | AUTHOR ACTION REQUIRED | time-dependent |

## 9. Reviewer simulation (from the manuscript alone)

| Question | Answer once §8 is closed | Evidence |
|---|---|---|
| Find the software? | Yes | Code repository, PyPI, Zenodo fields |
| Identify the exact version? | Yes: 1.1.0 = one named commit, same in PyPI provenance and Zenodo | Software location paragraph |
| Get it via a persistent identifier? | Yes: Zenodo DOI | Archive field |
| Install it? | Yes: two commands in Quality control (PyPI, or git+commit) | CI wheel jobs, clean-install test |
| Run sample input and get the expected output? | Yes: Listing 1 and its output; identical on Linux, macOS, Windows, old and new dependencies | CI diff step |
| Licence, contributors, support, limitations clear? | Yes | Availability; Reuse potential; Scope and limitations |
| Architecture and quality control understandable? | Yes | Figure 1, Table 1 |
| Reuse and extension routes concrete? | Yes, with the boundary to substantial new work | Reuse potential |

Weakness a reviewer may raise, stated honestly in the paper: no external
users yet; tests written by the developer (partly AI-assisted).

## 10. Reproducing

```sh
python -m pytest
python -m build && python -m twine check --strict dist/*
python examples/sample_verification.py | diff - examples/sample_verification_expected.txt
make -C jors check
curl -s -o /dev/null -w '%{http_code}\n' https://pypi.org/pypi/quantum-group/json
```
