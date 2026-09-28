# JORS pre-submission verification record

Rewritten **27 September 2026** from the current repository state; updated
**28 September 2026** after the Codex-attribution correction and the v1.1.0
GitHub Release. Earlier versions of this file are superseded. The author
reversed the earlier "no release" decision: **`v1.1.0` is now a published
GitHub Release** (created by the author, 28 Sep 2026), target `main`,
pointing at commit `103d538` (below). Nothing has been published to PyPI or
Zenodo yet. **Re-checked 28 Sep 2026 (later same day):** `git ls-remote
--tags origin` shows only `v1.0.0` and `v1.1.0` — no `v1.0.1` tag exists on
the remote. The earlier note about a stray `v1.0.1` tag was based on a
first, misnamed release attempt that was evidently cleaned up (tag and all)
before this check; there is nothing left to delete.

## 1. Repository topology (fetched 27 Sep 2026, releases re-checked 28 Sep 2026)

| Ref | SHA | Content |
|---|---|---|
| `origin/main` | `103d5384e70e8b0b746b296a0bdbd2d156ba8dde` (`103d538`) | Codex-attribution correction on top of the merged JORS package |
| `claude/determined-maxwell-7u3h0j` | `33ae33c2484505b7d8dbe61a34b32f8e78a012c8` | JOSS wording, de Graaf DOI, v1.0.0 DOI removed from 1.1.0 `CITATION.cff` — merged into `main` |
| `claude/sleepy-darwin-o4mr5p` | see `git log` | JORS package (`96e50e4`, `0c36fb2`) + `33ae33c` + distribution work — merged into `main` (PR #8) |
| `claude/happy-lamport-lq2yqj` | — | fully contained in `main` |
| tag `v1.0.0` | `8dcfe99` | historical; untouched. GitHub Release: "v1.0.0 — First release" (2026-09-27T13:44:49Z); untouched |
| tag `v1.1.0` | `103d538` | **GitHub Release published 28 Sep 2026T11:18:18Z**, title "v1.1.0", target `main` |
| tag `v1.0.1` | — | **does not exist** (re-checked via `git ls-remote --tags origin`, 28 Sep 2026, later same day); the earlier misnamed release attempt left no tag behind, so there is nothing to delete |

Package source identity: `quantum_group/` tree `804d66f83a1d`, `tests/` tree
`a2a4fdc80bf4`, `pyproject.toml` blob `b17aa2bbc012` — all identical between
the earlier JORS snapshot commit (`892dfae`) and the released commit
(`103d538`); only `jors/` and `paper/` documentation changed in between
(verified 28 Sep 2026 by direct tree-hash comparison). No package-code
re-validation is therefore needed beyond re-confirming CI on `103d538`
(done: run passed, all 9 jobs, §7).

## 1a. JORS submission software snapshot

`103d5384e70e8b0b746b296a0bdbd2d156ba8dde` (`103d538`), committed
2026-09-28T14:13:05+03:00 (`git show -s --format=%cI 103d538`); version
1.1.0; package source trees identical to the earlier
snapshot (see above); 202 tests passed locally; CI: all 9 jobs green (§7).
**This commit is now tagged `v1.1.0` with a published GitHub Release** — the
earlier "no release" plan in this file and in `DISTRIBUTION.md` no longer
applies; PyPI and Zenodo should be built from this commit / this release.
Archive reference: `git archive --format=zip --prefix=quantum-group-1.1.0/
103d538…` = 236 files, 13,011,364 bytes, SHA-256
`47433ae4feef57f81daf2c219fd4051dd60a04435aed38a5ba8b3a5b77cd5c1d`
(git 2.43.0; deterministic on repeat; file count matches the earlier
snapshot exactly, byte size differs only because of the documentation
changes).

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
| APC amount | **£824.00**, confirmed 28 Sep 2026 directly from `openresearchsoftware.metajnl.com/about/submissions` (reachable from a later environment; see `SUBMISSION_CHECKLIST.md`) |

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
Abstract **143 words** as rendered (updated 28 Sep 2026 to name the thesis-error
catch, its strongest selling point, which the earlier draft left out; current
articles: 104–143 words, so this is at the top of the range but within it;
the historical "ca. 100 words" instruction could not be confirmed as current).

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
| `892dfae` (earlier snapshot, superseded) | [33](https://github.com/TerekliTahaBerk/quantum-groups/actions/runs/36338318144) | passed, all 9 jobs |
| `103d538` (**current snapshot = `v1.1.0` release commit**) | [36414857192](https://github.com/TerekliTahaBerk/quantum-groups/actions/runs/36414857192), re-verified via the GitHub API 28 Sep 2026 | **passed, all 9 jobs** (pytest 3.10–3.13, minimum dependencies, wheel + examples, Linux, macOS, Windows) |

The final snapshot commit must itself show green CI before PyPI/Zenodo.

## 8. Remaining open items (current, not inherited)

| Item | Class | Why it cannot be closed here |
|---|---|---|
| Codex use/model | RESOLVED 28 Sep 2026 | Author confirmed Codex (OpenAI) was never used at any stage. All mentions in `paper/paper.md`, `paper/PREFLIGHT.md`, `AUDIT.md`, `jors/paper.tex`, `jors/COVER_LETTER.md`, `jors/SUBMISSION_CHECKLIST.md` and `jors/submission-facts.tex` corrected to attribute that work to Claude Code |
| Reviewer e-mails (5) | AUTHOR ACTION REQUIRED (1 of 5) | 28 Sep 2026: 4 confirmed directly from official pages (`POTENTIAL_REVIEWERS.md`); Levandovskyy's page returned no visible address in two fetch attempts, needs a direct human visit |
| APC amount and choice | RESOLVED 28 Sep 2026 | Amount £824.00; author chose to request a full waiver (thesis-derived work, no specific funding). Request text in `COVER_LETTER.md` |
| Zenodo DOI reservation, deposit, publication | CREDENTIAL/AUTHORIZATION REQUIRED | author's Zenodo account; irreversible |
| PyPI publication of `quantum-group` 1.1.0 | CREDENTIAL/AUTHORIZATION REQUIRED | pending-publisher setup on the author's PyPI account; environment approval; name still unclaimed (404 on 27 Sep 2026) |
| Merge to `main` | DONE | merged 28 Sep 2026 (PR #8); this file's branch references predate the merge and are historical |
| GitHub Release for 1.1.0 | DONE | `v1.1.0` published 28 Sep 2026, commit `103d538`; author reversed the earlier "no release" decision |
| Stray `v1.0.1` tag | AUTHOR ACTION REQUIRED (trivial) | Delete the tag (its Release was already deleted); same commit as `v1.1.0`, harmless but should not remain as a second identifier for this version |
| Snapshot SHA/date in the paper (`\SnapshotSHA`, `\SnapshotDate` in `submission-facts.tex`) | AUTHOR/CLAUDE ACTION — not yet updated in the LaTeX facts file | Re-frozen here (§1a) as `103d538`, 2026-09-28T14:13:05+03:00; still needs to be copied into `jors/submission-facts.tex` and `make -C jors check` re-run |
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
