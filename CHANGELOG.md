# Changelog

All notable changes to this project are documented in this file.
The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project follows [Semantic Versioning](https://semver.org/).

## [Unreleased]

### Fixed

- Preserve exact Python integer parameters in representations, R matrices,
  relation checks and the public facade; reject singular defining-relation
  parameters with an explanatory error.
- Evaluate q-integers and q-binomials as Laurent polynomials, including
  removable-singularity specializations at q = ±1 and roots of unity.
- Return actual leading terms for E asymptotics; validate root orders N>2.
- Check counit identities using the public counit values.
- Require even operators and compatible dimensions for graded embeddings.
- Correct coproduct/spectral interpretation, source pagination and manuscript
  scope. Record corrections to archived thesis artifacts in `thesis/ERRATA.md`.

### Added

- Explicit coproduct-compatible fundamental R and braid matrices, plus
  intertwining residual/Boolean APIs; historical R outputs are unchanged.
- Independent regressions for full CG basis changes, source matrix entries,
  graded component embeddings, wrong-sign controls and exact specializations.
- `AUDIT.md` with derivations, source limitations and novelty assessment.

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

[1.0.0]: https://github.com/TerekliTahaBerk/quantum-groups/releases/tag/v1.0.0
