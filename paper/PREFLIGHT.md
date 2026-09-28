# Publication verification record

Updated 27 September 2026 for the commit that contains this file (on top of
`05a8148`, the merge of pull request #6). It supersedes earlier versions of this record, which described
an uncommitted working tree. The active manuscript is `paper.md` with
`paper.bib`; `../thesis/` contains historical material only.

JOSS requirements were checked against the current documentation source
(`docs/submitting.md`, `paper.md`, `review_criteria.md`,
`review_checklist.md` in `openjournals/joss`, retrieved 27 September 2026).

## Current state

| Item | Status and evidence |
|---|---|
| Version | `main` is **1.1.0, unreleased** (`pyproject.toml`, `CITATION.cff`, `CHANGELOG.md`, `quantum_group.__version__`). |
| Releases | Tag/release `v1.0.0` → commit `8dcfe99` (27 Sep 2026). Zenodo version DOI 10.5281/zenodo.22997681 (recorded by the author in `855cade`) archives **v1.0.0 only**. The Zenodo record itself could not be retrieved from the checking environment (zenodo.org blocked). |
| Release vs paper | The paper describes 1.1.0 behaviour (coproduct-compatible R APIs, exact integer handling, validation, CI matrix). None of this is in v1.0.0: `git diff v1.0.0` changes all 13 package modules that v1.0.0 contained and adds two. JOSS asks for the tagged release and archive DOI when review is complete, so an archive is not needed to submit; what must not happen is presenting the v1.0.0 DOI as the archive of this code. `CITATION.cff` therefore lists no DOI for 1.1.0. |
| Validation command | `python -m pytest` (tests + doctests, configured in `pyproject.toml`); identical in CI, README, CONTRIBUTING and `make check`. |
| Local result | **202 passed** = 198 test cases + 4 doctests, Python 3.12.3/SymPy 1.14.0/NetworkX 3.7/Matplotlib 3.11.2, ~13 s. Also 202 passed on Python 3.10, 3.11 and 3.13 with current dependencies, and on Python 3.10 with SymPy 1.10.1, NetworkX 2.6.3, Matplotlib 3.5.3, numpy<2 (the declared lower bounds). |
| CI | Workflow: Python 3.10–3.13, a minimum-dependency job, and a wheel install that runs `examples/quickstart.py` outside the source tree. The previous commit `bc5c370` passed CI (run 24, Python 3.10–3.12). The result for this commit is on the Actions page. |
| Packaging | `python -m build` produces `quantum_group-1.1.0` wheel and sdist; the wheel installs into a clean environment and the quickstart passes from a directory outside the repository. |
| Other entry points | `main.py`, `thesis/figures/generate_figures.py`, `benchmarks/benchmark.py --max-n 4` (written to a scratch directory; `benchmarks/results.*` unchanged) and `notebooks/exploration.ipynb` (executed with nbclient) all run. |
| Static checks | `git diff --check` clean; `compileall` clean; `ruff --select F,E9` reports only pre-existing unused imports in untouched lines. |
| Paper build | Built with the official `openjournals/inara` Docker image (`make joss-pdf`): no citeproc warnings, all 12 keys resolve, no unused entries. Body ≈ 1,545 words as rendered to plain text (including the table), within JOSS's 750–1,750 range. |
| Historical article | `make historical-article-pdf` could not be verified: Tectonic's bundle host is blocked here and Inara's TeX Live lacks `mathrsfs.sty`. |
| Bibliography | Entries re-checked where sources were reachable (GAP CHANGES.md, Sage CITATION.cff/VERSION.txt, QuaGroup PackageInfo.g). Çelik–Çelik pages 259–269: from the original PDF (AUDIT.md §11) and the ScienceDirect listing. de Graaf (2001) DOI 10.1006/jsco.2001.0479 added after the author confirmed it against the ScienceDirect record (not resolvable from the automated environment). |

## Actions required from the author before submission

1. **Review the full diff since `v1.0.0`.** A v1.1.0 release is optional
   before submission. JOSS requests the tagged release and archive DOI at
   the end of a successful review, so the archive to give JOSS is the
   release that includes any reviewer-requested changes (steps in
   `README.md` in this directory). Never present the v1.0.0 DOI as the
   archive of the code the paper describes.
2. **AI disclosure.** The paper's disclosure is based on the Git record
   (commits authored/co-authored by "Claude"). The author confirmed on
   28 September 2026 that Codex (OpenAI) was never used at any stage; an
   earlier revision of this disclosure and of `AUDIT.md` incorrectly
   attributed part of the translation/audit work to Codex, and that
   attribution has been corrected to Claude Code throughout `paper.md`,
   `AUDIT.md` and the `jors/` submission materials. Before submitting:
   (a) insert the exact model name(s) and version(s) for every Claude Code
   session actually used (JOSS asks for them; the model is in the
   `Co-Authored-By` trailers of the Claude commits, and one Claude-authored
   commit, `aed9cc8`, has no trailer — fill it in from memory or mark it
   unknown rather than guessing); (b) state whether any AI tools were
   used during the April–June 2026 development and thesis work, and extend
   the disclosure if so; (c) only keep the sentence "The author reviewed,
   edited and validated all AI-assisted outputs…" once that review has
   actually been done for all AI-assisted changes, including this revision.
   (d) Once review starts, JOSS does not allow generative AI for
   conversational interactions with editors or reviewers, except for
   translation: write review replies yourself.
3. **Funding.** JOSS asks for acknowledgement of financial support. State
   in the Acknowledgements whether the work received any funding (for
   example "This work received no external funding.", only if true).
4. Confirm the date since which the repository has been **public** (GitHub
   shows only its creation date, 24 March 2026).

## JOSS gate assessment (current rules)

Development-history facts from `git log origin/main` (non-merge commits):
28 Apr 2026 (3), 30 Apr (1), 30 May (4), 1 Jun (5), 14 Jun (1), then none
until 27 Sep 2026 (16 before this revision, merged through pull requests
#1–#6, all opened and merged the same day; this revision adds more). That is six
active days in five months, a 105-day gap, and all publication work
concentrated on one day. The repository was created on 24 March 2026; it has
no issues, no external contributors, and one release.

| Requirement | Status |
|---|---|
| OSI licence, browsable repo, open issue tracker, `pip`-installable package | **Satisfied now** |
| Tests with CI; documentation; CONTRIBUTING with support statement; changelog; tagged release | **Satisfied now** |
| Paper sections (Summary, Statement of need, State of the field with build-vs-contribute, Software design, Research impact, AI disclosure), length, references | **Satisfied now**, subject to author actions 2–3 |
| Software archive DOI matching the reviewed version | **Due at the end of review**; the metadata no longer attach the v1.0.0 DOI to 1.1.0 |
| Demonstrated research impact | **Evidence-dependent.** Documented use in the author's own thesis and the thesis audit, which JOSS names as the minimum ("at minimum by the developers themselves"). No publication, preprint or external user cites or uses it yet; editors may judge this insufficient. |
| Public for more than six months, with active development spanning that period | **Cannot honestly be satisfied today.** Even if the repository was public from creation (24 Mar 2026, six months ago on 24 Sep), development does not span the period: there were no commits for 105 days, and most publication work happened on a single day. |
| Iterative development over time; not a concentrated window | **Cannot honestly be satisfied today.** The history shows three short bursts, the last concentrated in one day; JOSS states that it runs automated checks on commit distribution. |
| Open-source workflow signals beyond the author (issues, reviewed PRs, discussion) | **Not met; not a hard gate for a solo project**, but the existing PRs were self-merged without review, and there are no issues. Only genuine future use can change this. |

**Conclusion.** The technical and documentation items that can be completed
now are complete, apart from the author actions above. The submission is not
yet eligible under the history and iteration gates, and these can only be met
through genuine public development and use over time; no fabricated
activity can or should substitute for them. The rules give no mechanical
date. Two facts bound it. The screening gate asks for more than six months
of public history with active development spanning it, and the first
substantive commit is dated 28 April 2026, so the span cannot cover six
months before **28 October 2026**. That date is a lower bound, not a
sufficient condition. The review criteria rate development "spanning 6+
months but with sporadic or bursty activity" as OK, and a history with all or
most commits in the weeks before submission as not acceptable. Whether the
history qualifies therefore depends on development continuing naturally
through October and beyond, ideally refinements driven by real use (for
example a colleague installing the package and reporting issues, which the
JOSS guidelines explicitly recommend). A further burst of generated commits
would weaken rather than strengthen the record.

## Reproducing this record

```sh
python -m pytest                          # 202 passed
python examples/quickstart.py
make joss-pdf                             # Docker, openjournals/inara
python benchmarks/benchmark.py --repeats 1 --max-n 4 --out-dir build/benchmarks
git log origin/main --no-merges --format=%ad --date=short | sort | uniq -c
```
