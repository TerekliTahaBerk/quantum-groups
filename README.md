# quantum-group: A lightweight SymPy package for verifying U_q(sl_2) and GL_q(2|1) structures

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.22997681.svg)](https://doi.org/10.5281/zenodo.22997681)

This repository contains SymPy-based symbolic modelling and verification code
for `U_q(sl_2)` and `GL_q(2|1)`. It connects the manuscript's explicit
finite-dimensional representations, residual matrices, Yang-Baxter checks and
related figures to reproducible tests. It is not a general theorem prover.

## Main Features

- Helpers for `q`-integers, `q`-factorials, `q`-binomial coefficients and classical limits.
- Explicit `E`, `F`, `K`, `K_inv` matrices for finite-dimensional `U_q(sl_2)` representations `V_n`.
- Representation-level verification of defining relations by zero residuals.
- Hopf structure: coproduct, counit, antipode and axiom checks.
- Tensor products, Clebsch-Gordan examples and highest-weight vectors.
- The `V_1 \otimes V_1` R-matrix, QYBE, braid relation and Hecke/skein check.
- The 9x9 R-matrix for `GL_q(2|1)`, super-permutation and 27x27 graded YBE verification.
- `R_{ij}` embeddings in `V^{\otimes n}`, far commutativity and local YBE checks.
- The crystal graph `B(n)` and basic visualization functions.
- A reproducible `pytest` test suite.

## Mathematical Background

`R_matrix_V1()` is the Drinfeld-Jimbo R-matrix of `U_q(sl_2)` on
`V_1 \otimes V_1`. The universal R-matrix
`q^{H⊗H/2}(1 + (q - q^{-1}) E⊗F + ...)` (Drinfeld 1987; see Kassel 1995 for
the full series) truncates after two terms on `V_1`, because `E^2 = F^2 = 0`
there. Its image, rescaled by `q^{1/2}` to remove fractional powers, is the
4x4 matrix `diag(q, 1, 1, q)` plus a single off-diagonal entry `q - q^{-1}`.
The normalization is derived from Drinfeld §13, pp. 816–817 in `AUDIT.md`.

The historical `R_matrix_V1()` uses the opposite of the package coproduct.
For `hopf.coproduct` and the tensor-product submodules, use
`R_matrix_V1_coproduct()` (equal to `R.T`) and
`R_check_V1_coproduct()` (equal to `R * swap_matrix(2)`).
`intertwining_residual_V1("E")` exposes the coproduct-compatibility check;
`intertwining_holds_V1` also accepts `F`, `K` and `K_inv`.
Both R conventions satisfy QYBE and their braided forms satisfy the Hecke
relation, but their eigenspaces must not be identified across conventions.

Exact Python integer parameters are sympified before negative powers;
floats remain approximate. The default domain is generic nonzero q.
Laurent-polynomial q-arithmetic supports removable-singularity specializations,
while the defining commutator quotient itself excludes q = ±1.
At roots of unity the modules need not be irreducible or semisimple.
The generic CG algorithm is not a root-of-unity decomposition algorithm.

The GL matrix matches the unnumbered display on printed page 261 of
Çelik and Çelik, *Reports on Mathematical Physics* 88 (2021), **259–269**.
All twelve nonzero entries, the graded signs and all six four-factor
placements are independently checked. General embeddings accept even
operators only. See [audit](AUDIT.md) and [thesis errata](thesis/ERRATA.md).

- M. Jimbo, Lett. Math. Phys. 10 (1985) 63-69, doi:10.1007/BF00704588.
- M. Jimbo, Lett. Math. Phys. 11 (1986) 247-252, doi:10.1007/BF00400222.
- V. G. Drinfeld, "Quantum groups", Proc. ICM Berkeley 1986, Vol. 1, AMS
  (1987) 798-820.
- C. Kassel, *Quantum Groups*, GTM 155, Springer (1995),
  doi:10.1007/978-1-4612-0783-2.

## Related Work

The main existing tools for computing with quantized enveloping algebras are
the GAP package [QuaGroup](https://github.com/gap-packages/quagroup)
(W. A. de Graaf) and SageMath's `QuantumGroup` class, which is an interface to
QuaGroup. Both are far more general than this package: they handle `U_q(g)`
for semisimple Lie types, subject to computational limits, including
R-matrices, crystal and canonical bases, and the Hopf structure. SageMath also
has combinatorial crystals for the general linear Lie *super*algebra
(Benkart-Kang-Kashiwara crystals of type `A(m|n)`).

| | quantum-group (this package) | GAP QuaGroup 1.8.4 | SageMath `QuantumGroup` |
| --- | --- | --- | --- |
| Scope | `U_q(sl_2)` and one quantum supergroup example, `GL_q(2\|1)` | `U_q(g)`, `g` finite-dimensional semisimple | Same as QuaGroup (wraps it) |
| R-matrix | `V_1⊗V_1` (4x4); `GL_q(2\|1)` (9x9) | `RMatrix` for modules with computable weights | `R_matrix()` via QuaGroup |
| Super / graded structures | Graded (super) YBE for `GL_q(2\|1)`, including `R_ij` on `V^{⊗n}` | This specific graded YBE example is not documented | This example is not documented in `QuantumGroup`; gl(m\|n) crystals exist separately |
| Crystals | Combinatorial `B(n)` for `sl_2` only | Crystal bases, crystal graphs (LS paths) | Extensive crystal library |
| Treatment of `q` | SymPy symbol; substitution helpers for classical and root-of-unity limits | Indeterminate `q` over `Q` | Generic `q` or a specialization, e.g. a root of unity |
| Verification style | Explicit residual matrices checked entrywise to be zero, wired to `pytest` | Algebraic computation | Algebraic computation |
| Installation / dependencies | `pip install` from the Git repository (not on PyPI); SymPy, NetworkX, Matplotlib | GAP >= 4.8 | Full SageMath plus the optional `gap_package_quagroup` |
| License | MIT | GPL-2.0-or-later | Library code GPL-2.0-or-later; the Sage distribution as a whole is GPL-3.0 |

This package does not try to replace these systems. It aims to be a small,
pip-installable, pure-Python reference implementation. It makes the concrete
matrices behind the manuscript's claims explicit, including the graded
Yang-Baxter equation for `GL_q(2|1)`, and checks them in CI.

The comparison concerns the documented
[QuaGroup](https://gap-packages.github.io/quagroup/doc/chap1.html) and
[Sage QuantumGroup](https://doc.sagemath.org/html/en/reference/algebras/sage/algebras/quantum_groups/quantum_group_gap.html)
interfaces, not all software or all superalgebra functionality. Historical
commit-level search claims are not needed to establish this package's scope.

## Installation

Python 3.10 or newer is required. The package is defined in `pyproject.toml`
(distribution name `quantum-group`, import name `quantum_group`).

The package is not yet published on PyPI; install it directly from this repository:

```bash
git clone https://github.com/TerekliTahaBerk/quantum-groups.git
cd quantum-groups
python3 -m venv .venv
source .venv/bin/activate
python3 -m pip install -e ".[test]"
```

To install without cloning:
`python3 -m pip install "git+https://github.com/TerekliTahaBerk/quantum-groups"`.
Runtime dependencies are SymPy, NetworkX and Matplotlib; pytest (`[test]`)
and Jupyter (`[notebooks]`) are optional.

To run the notebooks, use `".[test,notebooks]"`
(equivalent to `pip install -r requirements.txt`).

## Quickstart

```python
from quantum_group import (
    build_representation,
    verify_on_representation,
    R_matrix_V1,
    qybe_holds,
    graded_yang_baxter_holds_GLq21,
)

rep = build_representation(2)
checks = verify_on_representation(rep.E, rep.F, rep.K, rep.K_inv)
assert all(check.holds for check in checks.values())

assert qybe_holds(R_matrix_V1())
assert graded_yang_baxter_holds_GLq21()
```

Compatibility names used by manuscript drafts are also available:
`build_representation_core(...)` and `verify_relations_core(...)`.

## Tests

Run the full reproducibility suite:

```bash
python3 -m pytest -q
```

Useful targeted runs:

```bash
python3 -m pytest tests/test_r_matrix.py -q
python3 -m pytest tests/test_supergroup_gl21.py -q
python3 -m pytest tests/test_tensor.py -q
```

The `GL_q(2|1)` tensor-power checks use symbolic `81x81` matrices. On the
reference machine in `benchmarks/results.md`, `tests/test_supergroup_gl21.py`
takes about 5 s and the full suite about 13 s.

## Repository Structure

```text
quantum-groups/
├── quantum_group/
│   ├── utils.py                 # q-arithmetic and classical limits
│   ├── generators.py            # symbolic E, F, K, K_inv
│   ├── representations.py       # V_n construction
│   ├── relations.py             # U_q(sl_2) relation checks
│   ├── quantum_group_sl2.py     # facade class
│   ├── hopf.py                  # coproduct, counit, antipode
│   ├── tensor.py                # tensor products and CG examples
│   ├── r_matrix.py              # R, R_check, QYBE, braid and Hecke checks
│   ├── supergroup_gl21.py       # GL_q(2|1), graded YBE, R_ij embeddings
│   ├── limits.py                # classical/root-of-unity/crystal-limit helpers
│   ├── crystal.py               # combinatorial crystal graph B(n)
│   └── visualization.py         # weight and crystal diagrams
├── tests/
│   ├── test_relations.py
│   ├── test_representations.py
│   ├── test_hopf.py
│   ├── test_tensor.py
│   ├── test_r_matrix.py
│   ├── test_supergroup_gl21.py
│   ├── test_limits.py
│   └── test_visualization.py
├── thesis/
│   ├── thesis.tex
│   ├── thesis_ytu.tex
│   ├── Lisans Bitirme Tezi.pdf
│   └── figures/
│       ├── generate_figures.py
│       ├── R_sl2_V1.pdf
│       ├── R_gl21_structure.pdf
│       └── ybe_products_27.pdf
├── benchmarks/
│   ├── benchmark.py             # timing script
│   ├── results.csv
│   └── results.md
├── notebooks/exploration.ipynb
├── MANUSCRIPT_CODE_MAPPING.md
├── main.py
├── Makefile
├── requirements.txt
└── README.md
```

## Reproducing Manuscript Results

| Section | Claim | Module | Test |
| --- | --- | --- | --- |
| `q` arithmetic | `[n]_q`, factorials, binomials, classical limits | `quantum_group/utils.py` | `tests/test_relations.py` |
| `U_q(sl_2)` relations | R1-R4 hold on explicit `V_n` matrices | `quantum_group/relations.py` | `tests/test_relations.py` |
| Representations | `V_n` dimensions, weights, highest/lowest vectors | `quantum_group/representations.py` | `tests/test_representations.py` |
| Hopf structure | coproduct, counit, antipode checks | `quantum_group/hopf.py` | `tests/test_hopf.py` |
| Tensor products | coproduct action and CG highest-weight vectors | `quantum_group/tensor.py` | `tests/test_tensor.py` |
| R-matrix/QYBE | `R_{12}R_{13}R_{23}=R_{23}R_{13}R_{12}` | `quantum_group/r_matrix.py` | `tests/test_r_matrix.py` |
| `GL_q(2|1)` graded YBE | 27x27 residual is zero | `quantum_group/supergroup_gl21.py` | `tests/test_supergroup_gl21.py` |
| Limits and crystals | classical/root-of-unity helpers and `B(n)` graph | `quantum_group/limits.py`, `quantum_group/crystal.py` | `tests/test_limits.py`, `tests/test_representations.py` |
| Figures | PDF figures generated from package outputs | `thesis/figures/generate_figures.py` | smoke-checked by running the script |

For a fuller listing, see `MANUSCRIPT_CODE_MAPPING.md`.

## Figures

Regenerate manuscript figures:

```bash
python3 thesis/figures/generate_figures.py
```

The script writes:

- `thesis/figures/R_sl2_V1.pdf`
- `thesis/figures/R_gl21_structure.pdf`
- `thesis/figures/ybe_products_27.pdf`

The general visualization helpers in `quantum_group/visualization.py` return
Matplotlib `Figure` objects and leave saving/display to the caller.

## Manuscript and PDF

The submitted thesis (in Turkish) is `thesis/Lisans Bitirme Tezi.pdf`. The thesis LaTeX
build source is `thesis/thesis_ytu.tex`; the JOSS manuscript source is `thesis/thesis.tex`.
The active JOSS manuscript is `paper/paper.md`; its local reading copy and
rendering command are in `output/pdf/`. Official JOSS typesetting remains a
separate journal build. `make pdf` instead rebuilds the **historical Turkish
article**, whose corrections are recorded in `thesis/ERRATA.md`. With Tectonic:

```bash
make pdf
```

The Makefile also contains convenience targets:

```bash
make test
make figures
make pdf
make demo
```

## Limitations

- Cost grows quickly with the tensor power. On a 2.1 GHz Xeon (Python 3.11,
  SymPy 1.14; mean of 3 runs, see `benchmarks/results.md`):

  | Check | n | Matrix size | Mean time |
  | --- | --- | --- | ---: |
  | `graded_yang_baxter_holds_GLq21` | 3 | 27x27 | 0.06 s |
  | `all_Rij_GLq21` | 4 | 81x81 | 0.98 s |
  | `local_ybe_on_four_tensor_GLq21` | 4 | 81x81 | 1.56 s |
  | `all_Rij_GLq21` | 5 | 243x243 | 14.6 s |
  | graded YBE on one triple, incl. embedding | 5 | 243x243 | 15.2 s |

  These are historical measurements of the benchmarked functions, not a
  timing guarantee for the current expanded test suite. At n = 5
  the time is dominated by building the dense symbolic `R_ij` embeddings
  (about 14.6 s), not by simplifying the Yang-Baxter residual. n >= 6
  (729x729) has not been benchmarked. Reproduce with
  `python benchmarks/benchmark.py`.
- Most checks are explicit finite-dimensional representation-level
  verifications, not general formal proofs inside an abstract proof assistant.
- Root-of-unity behavior is exploratory; the package does not implement the
  full small quantum group theory.
- `crystal.py` implements the combinatorial crystal graph `B(n)`; it does not
  construct a full Kashiwara global basis.
- The Hecke/skein relation and braid representation are checked, but the Jones
  polynomial and Markov trace are not implemented.

## Citation

If you use this software, please cite it using the metadata in
[`CITATION.cff`](CITATION.cff). On GitHub, the **"Cite this repository"**
button in the sidebar exports it as APA or BibTeX, for example:

```bibtex
@software{Terekli_quantum-group,
  author  = {Terekli, Taha Berk},
  title   = {{quantum-group: Symbolic modelling and verification of U_q(sl_2) and GL_q(2|1) quantum group structures in Python}},
  version = {1.0.0},
  license = {MIT},
  url     = {https://github.com/TerekliTahaBerk/quantum-groups}
}
```
