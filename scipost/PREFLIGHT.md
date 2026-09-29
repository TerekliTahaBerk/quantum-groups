# SciPost Physics Codebases — preflight record

Prepared 29 September 2026. Manuscript: `scipost/paper.tex` → `paper.pdf`
(20 pages; 14 before the 29 Sep extension, see §6). Build and verify with `make -C scipost check` (prints `OK`);
`make -C scipost arxiv` writes `arxiv_source.tar.gz` for arXiv.

## 0. Blockers — author actions before submitting

| # | Action | Why |
|---|---|---|
| B1 | **Withdraw the JORS submission (#798) in writing and wait for the editor's confirmation.** | The same work is under consideration at JORS; the JORS cover letter promised exclusivity. Submitting to SciPost first would be a dual submission. |
| B2 | Correct the AI disclosure you gave JORS, if the withdrawal message goes beyond a one-line withdrawal. | JORS text names only Claude Opus 5.5, but 8 commits of 28–29 Sep 2026 (publication materials only, no code) were made with Claude Sonnet 5. The SciPost text states both. |
| B3 | arXiv: account (and endorsement, if arXiv asks for one), then upload `arxiv_source.tar.gz`. Suggested primary category **math-ph** (cross-list math.QA). Put `Submission to SciPost` in the Comments field. | SciPost's recommended route is preprint first; the SciPost form then auto-fills from arXiv. |
| B4 | SciPost account; submission form: journal *SciPost Physics Codebases*, specialty *Mathematical Physics*; optional suggested referees (the five from `jors/POTENTIAL_REVIEWERS.md` can be reused). | Required to submit. No fee at any stage (verified on the journal pages). |

Optional: tag a patch release (e.g. v1.1.1) that contains `scipost/examples/`, so
that Listings 2–4 are also in an archived release. The paper already states
that these listings were written after v1.1.0 and use only its public API.
SciPost publishes the accepted release of the code on git.scipost.org anyway.

## 1. Template

Official SciPost Physics Codebases template, version 2024-07 (class
`SciPost.cls` v1f), downloaded 29 Sep 2026 from
`https://scipost.org/SciPostPhysCodeb/authoring`, SHA-256
`3305eab69cb2e4f1658ec2af5e461eb9875647f3a96a40b5d5e46f1d87441946`; copy in
`official_template/`. `SciPost.cls` and `SciPost_bibstyle.bst` are used
unmodified; the copyright placeholder block is byte-identical to the template.
The one overfull box it produces also occurs in the unmodified template.

## 2. Journal requirements

| Requirement (journal wording, abridged) | Where / status |
|---|---|
| Userguide: introduction with background | Sec. 1 and Sec. 2 (mathematical background) |
| Generic workings, novelty, added value | Sec. 3; added value vs QuaGroup/SageMath in Sec. 1 ("Related software"), Sec. 6.3 (cross-check) and Sec. 8 |
| Guide to using the software | Sec. 4 (installation, API table, documentation/support) and Appendix A (API reference) |
| Worked-out examples; ≥1 example application in detail | Sec. 5: five listings with stored outputs; Sec. 5.2 is the thesis-audit application |
| Benchmarking tests | Sec. 6: 202 tests incl. comparisons with published values and negative controls; cross-check against GAP/QuaGroup; performance table |
| Complete documentation incl. download/install/run | Sec. 3.1, 3.3 |
| OSI licence | MIT (explicitly on the journal's list) |
| Title ≤ ~150 characters | ~108 characters |
| Abstract fits 8 template lines | exactly 8 lines (checked on the rendered PDF) |
| Introduction and conclusion | Sec. 1, Sec. 7 |
| Acknowledgements after conclusion; funding information (required); competing interests | present |
| References with DOI links; "can only be published if references are externally linked" | all 16 linked; `check_submission.py` fails otherwise |
| Everything hyperlinked | sections, equations, listings, tables, figure, citations, URLs |
| Technical figures only | Fig. 1 is a workflow diagram |
| Line numbers for refereeing; TOC for papers > 6 pages | both on |

## 3. What `check_submission.py` verifies

1. Each listing equals its script; 2. each printed output equals the stored
expected output; 3. each script, rerun, reproduces that output exactly;
4. no undefined references, LaTeX errors or overfull boxes (outside the
template's own block), no BibTeX warnings; 5. every reference has a DOI or a
URL in a field the SciPost style prints, and cited keys equal bibliography
keys; 6. every entry in the rendered bibliography shows a link. Negative
controls were run for checks 2, 3, 1, 5 and 6 (each failed as intended when
a file was deliberately altered, then passed after restoring it).

## 4. Bibliography verification (new since JORS)

- Benkart–Kang–Kashiwara: DOI `10.1090/S0894-0347-00-00321-0`, read from the
  AMS table of contents of JAMS 13(2) (2000), pp. 295–331. (The DOI
  `…-99-00324-0` that search results suggested belongs to a different paper
  and was rejected.)
- Drinfeld, ICM 1986: volume-1 PDF on mathunion.org, HTTP 200.
- quantum-group 1.1.0: Zenodo API record 23015576 — title, version
  `v1.1.0`, MIT, file MD5 `2f6fafa8efb71a7f036f401ab6d8b370`.
- SageMath: `10.5281/zenodo.8042260` is Zenodo's concept DOI (all versions;
  latest deposit 10.6.beta3), so the sagemath.org URL is printed as well.
- The SciPost `.bst` does not print the `url` field; URLs are repeated in
  `note`.

## 5. Independent review (29 Sep 2026) and resolution

A separate agent that had not seen the drafting re-ran every listing, the test
suite and the claims of Secs. 2.3 and 4.1–4.4, and confirmed them. Its
findings and what was done:

| Finding | Resolution |
|---|---|
| Dual submission with JORS | Blocker B1 above |
| Listings 2–4 not in the v1.1.0 release | Stated in Sec. 3.1; optional patch release above |
| AI disclosure omitted Claude Sonnet 5 | Fixed in the paper; B2 above for JORS |
| Zenodo reference title differed from the record | Fixed (exact record title) |
| Fig. 1 caption: `kron` not in the package namespace | Caption now says where it is imported from |
| "Coproduct stated next to every tensor-product function" too strong | Now: stated in the `hopf`/`tensor` module docs and README |
| Sec. 5.2 implied Listing 2's values are fixed by tests | Reworded to what the tests actually assert |
| 27 Sep rerun timings/memory not recorded in the repo | Removed from the SciPost paper (still in `jors/paper.tex`) |
| Timing-only "benchmarks" | Sec. 5.1 now names the comparisons with published values |
| Dropped from JORS text: issue-tracker URL, no-guaranteed-support note, Ubuntu 24.04 | Restored |
| "Lower bounds exercised" imprecise | Now names the tested versions |
| Drinfeld R: which coproduct | Stated |
| Noisy first benchmark row | Min column and a note added |

## 6. Extension of 29 Sep 2026 (author request: add all four proposed items)

| Item | Where | Verification |
|---|---|---|
| Mathematical background | Sec. 2 | Every formula read from the package source (relations.py, representations.py, hopf.py, r_matrix.py, supergroup_gl21.py) and, where computable, re-derived by running the package; the 9×9 GL_q(2|1) matrix of Eq. (10) is `R_matrix_GLq21()` entry by entry, and its evenness was checked. Basis vectors are numbered from 0 (as in the code); Ref. [7] numbers them from 1, which the text states |
| Second GL_q(2|1) example | Sec. 5.5, Listing 5, `examples/graded_four_factors.py` | Four-factor local YBE and far commutativity; the reordered basis (e_2, e_0, e_1) passes with parities (1,0,0) and fails with the stale list (0,0,1) (4 nonzero entries) |
| Cross-check with existing software | Sec. 6.3, Listing 6, `crosscheck/` | Data exported from QuaGroup 1.8.4 (GAP 4.12.1, commit in `crosscheck/README.md`); findings listed in that README. SageMath itself was not installed: its `QuantumGroup` is an interface to QuaGroup, which was tested directly |
| API reference | Appendix A | Signatures, return types and record fields read with `inspect`/`dataclasses`; behavioural claims (index validation, odd-operator rejection, q ∈ {0, 1, −1} rejection, dict keys) confirmed by running the code |

The checker was extended to Listings 5–6 and now also fails on overfull
display equations (reported by LaTeX as "detected at line"), which the first
version missed; an overfull display found this way was fixed.
