# Changelog

All notable changes to this project are documented in this file.
The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project follows [Semantic Versioning](https://semver.org/).

## [1.1.1] - 2026-09-29

Tagged as GitHub Release `v1.1.1` (commit
`7cb3877a5400c30ada625d9f577d78bf355e24a2`), published on PyPI as
[quantum-group 1.1.1](https://pypi.org/project/quantum-group/1.1.1/) and
archived on Zenodo as
[10.5281/zenodo.23039671](https://doi.org/10.5281/zenodo.23039671).
Documentation and packaging release. The package code (`quantum_group/`) and
the test suite (`tests/`) are unchanged from 1.1.0; results computed with
1.1.0 are reproduced exactly.

### Added

- `scipost/`: the userguide prepared for *SciPost Physics Codebases*, with
  its worked examples (`scipost/examples/`, Listings 2–5) and a cross-check
  against data exported from GAP's QuaGroup 1.8.4 (`scipost/crosscheck/`,
  Listing 6), each with its expected output; `make -C scipost check`
  verifies listings, outputs, references and the LaTeX build.
- `arxiv/`: the same text as a preprint in the AMS `amsart` layout,
  generated from `scipost/paper.tex` by `arxiv/build.py` (`make -C arxiv
  check`, `make -C arxiv bundle`).
- CI runs Listings 2–6 against the installed wheel and compares each output
  with its stored copy; `make listings` does the same locally, and
  `make paper` builds and checks the userguide.
- `.zenodo.json`: complete metadata for the Zenodo record made from each
  GitHub Release.
- `RELEASING.md`: release checklist (PyPI, GitHub Release, Zenodo).

### Changed

- Makefile: `joss-pdf` and `historical-article-pdf` removed; `listings` and
  `paper` added. README, `AUDIT.md`, `MANUSCRIPT_CODE_MAPPING.md` and the
  thesis notes point to the userguide in `scipost/`.
- The TikZ source of Figure 1 is now `scipost/figures/figure1_workflow.tex`.

### Removed

- Material not needed for the software or the userguide; all of it remains
  in the Git history (last present in commit `7aafa2c`, the journal records
  there under `archive/jors/` and `archive/joss/`): the JORS submission
  records (`jors/`; submission #798 was withdrawn on 29 September 2026), the
  never-submitted JOSS draft (`paper/`), `.gitattributes` (its only rule
  excluded `jors/` from archives), the poster build (`poster/`; the
  final poster is kept as `thesis/poster.pdf`), and the thesis build
  pipeline, Word copies, pre-submission check notes, QA page renders and the
  earlier article drafts (`thesis.tex`, `thesis_revised.tex`). The thesis
  keeps its submitted PDF, its LaTeX source `thesis_ytu.tex`, the figures it
  uses, `figures/generate_figures.py` and `ERRATA.md`. The release archive
  shrinks from about 13 MB to about 3 MB.

## [1.1.0] - 2026-09-28

Tagged as GitHub Release `v1.1.0` (commit
`103d5384e70e8b0b746b296a0bdbd2d156ba8dde`), published on PyPI as
[quantum-group 1.1.0](https://pypi.org/project/quantum-group/1.1.0/) and
archived on Zenodo as
[10.5281/zenodo.23015576](https://doi.org/10.5281/zenodo.23015576)
(`jors/DISTRIBUTION.md`, removed in 1.1.1). The earlier Zenodo DOI
10.5281/zenodo.22997681 archives v1.0.0 only and does not contain these
changes. This is a minor release under Semantic Versioning because it adds
public functions; existing public functions keep their names and documented
outputs, except that invalid arguments (listed below) now raise errors.

### Fixed

- Preserve exact Python integer parameters in representations, R matrices,
  relation checks and the public facade; reject singular defining-relation
  parameters (q = 0, ±1) with an explanatory error.
- Evaluate q-integers and q-binomials as Laurent polynomials, including
  removable-singularity specializations at q = ±1 and roots of unity.
- Return actual leading terms for E asymptotics; validate root orders N > 2.
- Check counit identities using the public counit values.
- Require even operators and compatible dimensions for graded embeddings.
- Correct coproduct/spectral interpretation, source pagination and manuscript
  scope. Record corrections to archived thesis artifacts in `thesis/ERRATA.md`.

### Added

- Explicit coproduct-compatible fundamental R and braid matrices
  (`R_matrix_V1_coproduct`, `R_check_V1_coproduct`) and intertwining
  residual/Boolean APIs (`intertwining_residual_V1`, `intertwining_holds_V1`);
  historical R outputs are unchanged.
- `quantum_group.linalg` with the shared `kron`, `kron_list` and
  `is_zero_matrix` helpers; `quantum_group.__version__`.
- Clear `TypeError`/`ValueError` for invalid input: non-integral or negative
  highest weights, sizes and indices; mismatched or non-square generator
  matrices in `verify_on_representation`; non-`d²×d²` R-matrices; invalid
  tensor positions, tensor powers and parity lists; `q = 0` in
  `QuantumGroupSL2`.
- Regression tests for full CG basis changes, source matrix entries, graded
  component embeddings, wrong-sign controls, exact specializations, the
  shared helpers and every new validation path.
- `examples/quickstart.py` (the README quickstart, run by CI from outside the
  source tree against an installed wheel).
- `examples/sample_verification.py` with its expected output
  `examples/sample_verification_expected.txt`, including an ungraded-swap
  negative control; CI compares the output after installing the wheel.
- CI job installing the wheel and running the examples and the full test
  suite on Linux, macOS and Windows.
- `.github/workflows/publish.yml`: manual PyPI publication of an explicitly
  named commit with Trusted Publishing (no stored token, no GitHub Release);
  it checks the version, builds, runs `twine check`, installs the wheel in a
  clean environment and compares the sample output before uploading, and
  waits for approval of the `pypi` environment.
- `jors/`: Journal of Open Research Software metapaper and submission
  records (not part of the installed package).
- `AUDIT.md` with derivations, source limitations and novelty assessment.

### Changed

- `python -m pytest` now runs the tests and the package doctests (configured
  in `pyproject.toml`); CI, README, CONTRIBUTING and `make check` use it.
- CI tests Python 3.10–3.13, the oldest supported dependencies, and a wheel
  install. Dependency lower bounds: SymPy ≥ 1.10, NetworkX ≥ 2.6,
  Matplotlib ≥ 3.5.
- Packaging metadata uses an SPDX licence expression (`license = "MIT"`,
  `license-files`) instead of the deprecated table form and licence
  classifier; building requires setuptools ≥ 77.
- Trove classifier `Development Status :: 4 - Beta` (was 5 - Production/Stable),
  reflecting the convention corrections made after 1.0.0.
- Cross-module use of the private helpers `hopf._kron`, `r_matrix._is_zero`
  and `supergroup_gl21._is_zero_matrix_symbolic` replaced by
  `quantum_group.linalg`; the private names remain as aliases.
- Makefile: `make pdf` replaced by `make historical-article-pdf` (it builds the
  earlier Turkish article, not the JOSS paper); new `check`, `quickstart`,
  `benchmark-smoke` and `joss-pdf` targets.
- Documentation, docstrings and comments translated to English; JOSS paper
  revised to the current JOSS section structure.

### Removed

- Generated or redundant files: `outputs/V4_combined.png` (written by
  `main.py`), the stale local paper preview in `output/pdf/`, the unzipped
  poster build directory `poster/_ytu_build/` (identical to the committed
  `.pptx`), LaTeX list files `thesis/thesis_ytu.lof/.lot`, an unused ORCID
  icon, and redundant thesis draft/export variants. Thesis QA page renders
  moved from `qa_pdf_pages/` to `thesis/qa_pdf_pages/`.

## [1.0.0] - 2026-09-27

First release, prepared for submission to the Journal of Open Source Software.

### Added

- MIT `LICENSE`.
- `pyproject.toml`: the package installs as `quantum-group` with
  `pip install -e .`; test and notebook dependencies are the optional extras
  `[test]` and `[notebooks]`.
- GitHub Actions workflow running `pytest` on Python 3.10, 3.11 and 3.12.
- `CONTRIBUTING.md` and `CITATION.cff`.
- `benchmarks/benchmark.py` with recorded timings (`benchmarks/results.md`,
  `benchmarks/results.csv`) for the `GL_q(2|1)` checks up to 243x243 matrices.
- README sections "Mathematical Background" (derivation of the
  `U_q(sl_2)` R-matrix and its coproduct convention) and "Related Work"
  (comparison with GAP QuaGroup and SageMath).
- Derivation, convention note and references in the `R_matrix_V1` docstring.
- JOSS paper draft: `paper/paper.md` and `paper/paper.bib`.

### Changed

- `jones_skein_relation_check` renamed to `hecke_skein_relation_check`. The
  function verifies the Hecke relation, not a Jones polynomial.
- README performance notes now quote measured timings.
- `requirements.txt` now installs the package itself (`-e .[test,notebooks]`).

### Deprecated

- `jones_skein_relation_check`: still available, but emits a
  `DeprecationWarning`. Use `hecke_skein_relation_check`.

### Removed

- `poster/node_modules/` is no longer tracked by git.

## Pre-1.0 development (April-June 2026)

Initial implementation developed for the undergraduate thesis *Quantum Grup
Yapılarının Python Ortamında Modellenmesi* ("Modelling Quantum Group Structures
in Python"; thesis in Turkish):
- `U_q(sl_2)` representations, relations, Hopf structure, tensor products
  and R-matrix checks;
- `GL_q(2|1)` graded Yang-Baxter verification;
- limits, crystal graphs and visualization;
- the `pytest` suite.

[1.1.0]: https://github.com/TerekliTahaBerk/quantum-groups/compare/v1.0.0...main
[1.0.0]: https://github.com/TerekliTahaBerk/quantum-groups/releases/tag/v1.0.0
