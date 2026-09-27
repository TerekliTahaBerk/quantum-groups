# quantum-group: exact SymPy verification of explicit U_q(sl_2) and GL_q(2|1) matrix identities

[![tests](https://github.com/TerekliTahaBerk/quantum-groups/actions/workflows/tests.yml/badge.svg)](https://github.com/TerekliTahaBerk/quantum-groups/actions/workflows/tests.yml)

`quantum-group` builds the explicit matrices behind concrete quantum-group
calculations with SymPy, forms the difference between the two sides of an
identity, and checks that every entry of this residual simplifies exactly to
zero. It covers finite-dimensional `U_q(sl_2)` representations and the graded
`GL_q(2|1)` R-matrix of Çelik and Çelik (2021). It verifies identities on
concrete representations; it is not a general quantum-group computer algebra
system and not a theorem prover.

## Main features

- `q`-integers, `q`-factorials and `q`-binomials as Laurent polynomials, and classical limits.
- Explicit `E`, `F`, `K`, `K_inv` matrices for the modules `V_n` of `U_q(sl_2)`.
- Defining relations checked as exact residual matrices.
- Coproduct, counit and antipode, with generator-level Hopf identities.
- Tensor products, Clebsch–Gordan highest-weight vectors.
- The fundamental R-matrix on `V_1 ⊗ V_1`: QYBE, braid and Hecke relations,
  coproduct intertwining, in both the historical and the coproduct-compatible
  convention (see below).
- The 9x9 `GL_q(2|1)` R-matrix, super-permutation, the 27x27 graded
  Yang–Baxter residual, and `R_ij` placements on `V^{⊗n}` via graded swaps.
- The combinatorial crystal graph `B(n)` and simple weight/crystal plots.

## Installation

Python 3.10–3.13. Runtime dependencies: SymPy ≥ 1.10, NetworkX ≥ 2.6,
Matplotlib ≥ 3.5 (installed automatically). The package is not on PyPI;
install it from this repository (distribution name `quantum-group`, import
name `quantum_group`):

```bash
git clone https://github.com/TerekliTahaBerk/quantum-groups.git
cd quantum-groups
python3 -m venv .venv
source .venv/bin/activate
python3 -m pip install -e ".[test]"
```

Without cloning:
`python3 -m pip install "git+https://github.com/TerekliTahaBerk/quantum-groups"`.
For the notebook in `notebooks/`, install `".[test,notebooks]"` (equivalent
to `pip install -r requirements.txt`).

## Quickstart

This is `examples/quickstart.py`; CI runs it from outside the source tree
against an installed wheel.

```python
from quantum_group import (
    build_representation,
    verify_on_representation,
    R_matrix_V1_coproduct,
    intertwining_holds_V1,
    qybe_holds,
    graded_yang_baxter_residual_GLq21,
    is_zero_matrix,
)

# U_q(sl_2): the 3-dimensional module V_2 satisfies the defining relations.
rep = build_representation(2)
checks = verify_on_representation(rep.E, rep.F, rep.K, rep.K_inv)
assert all(check.holds for check in checks.values())

# The fundamental R-matrix compatible with the package coproduct satisfies
# the QYBE and intertwines the coproduct for every generator.
assert qybe_holds(R_matrix_V1_coproduct())
assert all(intertwining_holds_V1(X) for X in ("E", "F", "K", "K_inv"))

# GL_q(2|1): the graded Yang-Baxter residual is an exact 27x27 zero matrix.
residual = graded_yang_baxter_residual_GLq21()
assert residual.shape == (27, 27) and is_zero_matrix(residual)

print("quickstart: all checks passed")
```

`examples/sample_verification.py` is a slightly longer example that prints
each result, including a negative control; its expected output is
`examples/sample_verification_expected.txt`, and CI checks that the two agree.

Every `*_residual` function returns the exact SymPy difference matrix, so a
failing identity can be inspected entry by entry. Draft names used in the
thesis, `build_representation_core` and `verify_relations_core`, remain
available as wrappers.

## Validation

One command runs the complete test suite and the package doctests; it is
what CI runs on Python 3.10–3.13 and with the oldest supported dependency
versions:

```bash
python3 -m pytest          # or: make check
```

Plots use Matplotlib's noninteractive `Agg` backend in the tests. The
`GL_q(2|1)` checks use symbolic 81x81 matrices; the full suite took about
15 s when prepared for 1.1.0 (Python 3.12, SymPy 1.14, x86-64 Linux). Targeted runs, e.g.
`python3 -m pytest tests/test_supergroup_gl21.py`, also work.

## Conventions and mathematical background

The coproduct is `Δ(E) = E⊗1 + K⊗E`, `Δ(F) = F⊗K^{-1} + 1⊗F`, `Δ(K) = K⊗K`.

`R_matrix_V1()` is the historical upper-triangular matrix
`diag(q, 1, 1, q)` plus the entry `q - q^{-1}`: the image of Drinfeld's
universal R-matrix on `V_1 ⊗ V_1` multiplied by `q^{1/2}` (Drinfeld 1987,
§13, pp. 816–817; derivation in [`AUDIT.md`](AUDIT.md) §4). It intertwines
the **opposite** of the package coproduct. For the package coproduct and its
tensor-product submodules use `R_matrix_V1_coproduct()` (`= R_21 = P R P`)
and `R_check_V1_coproduct()` (`= R P`); `intertwining_residual_V1(X)` exposes
the check for `X` in `E, F, K, K_inv`. Both conventions satisfy the QYBE and
the Hecke relation, but their braid eigenspaces differ. The historical
function is kept unchanged so that earlier results remain reproducible.

Exact Python integers are converted to SymPy integers; floats remain
approximate. The default parameter is a generic nonzero symbol `q`;
identities are rational in `q` and hold where denominators are defined. The
defining commutator quotient excludes `q = ±1` (use the classical-limit
helpers there). At roots of unity the modules need not be irreducible or
semisimple, and the Clebsch–Gordan routine assumes generic `q`.

For `GL_q(2|1)` the basis parities are `(0, 0, 1)`. The matrix matches the
unnumbered display on printed page 261 of Çelik and Çelik, *Reports on
Mathematical Physics* 88 (2021) 259–269; every entry is fixed by a test.
General placements accept even (parity-preserving) operators only.

## Scope and limitations

- Checks run on explicit finite-dimensional representations; they do not
  prove identities in the abstract Hopf algebra or classify representations.
- A residual that SymPy does not simplify to zero is not by itself a proof of
  inequality (`simplify` is not a decision procedure).
- Root-of-unity helpers are examples; the small quantum group is not
  implemented. `B(n)` is a combinatorial model, not a crystal-basis algorithm.
- The RTT relations, Hopf superalgebra and Gauss decomposition of
  `GL_q(2|1)`, Markov traces and the Jones polynomial are not implemented.
- Dense symbolic matrices grow as `3^n`. Recorded timings
  (`benchmarks/results.md`; Python 3.11, SymPy 1.14, 2.1 GHz Xeon, mean of 3):

  | Check | n | Matrix size | Mean time |
  | --- | --- | --- | ---: |
  | `graded_yang_baxter_holds_GLq21` | 3 | 27x27 | 0.06 s |
  | `all_Rij_GLq21` | 4 | 81x81 | 0.98 s |
  | `local_ybe_on_four_tensor_GLq21` | 4 | 81x81 | 1.56 s |
  | `all_Rij_GLq21` | 5 | 243x243 | 14.6 s |
  | graded YBE on one triple, incl. embedding | 5 | 243x243 | 15.2 s |

  At n = 5 building the embeddings dominates. n ≥ 6 has not been
  benchmarked. Rerun with `python benchmarks/benchmark.py` (overwrites the
  recorded table) or `make benchmark-smoke` (writes to `build/`).

## Related software

GAP's [QuaGroup](https://github.com/gap-packages/quagroup) (W. A. de Graaf)
and SageMath's `QuantumGroup` interface to it are far more general: they
compute with `U_q(g)` for semisimple `g`, including highest-weight modules,
R-matrices and canonical/crystal bases; SageMath also has crystals for
`gl(m|n)`. This package does not replace them. It is a small pure-Python
layer for checking the explicit matrices of a particular text, in its basis
order and conventions, including the graded `GL_q(2|1)` example, which lies
outside QuaGroup's documented `U_q(g)` scope. For general `U_q(g)`
computations, use those systems. See `paper/paper.md` for a fuller
comparison.

## Reproducing the paper's calculations

The JOSS manuscript is [`paper/paper.md`](paper/paper.md). Each
computational claim is mapped to code and tests in
[`MANUSCRIPT_CODE_MAPPING.md`](MANUSCRIPT_CODE_MAPPING.md). The main ones:

| Claim | Command |
| --- | --- |
| Graded YBE: all 729 residual entries vanish; ordinary flip fails in exactly two entries | `python3 -m pytest tests/test_supergroup_gl21.py tests/test_audit_regressions.py -k "yang_baxter or swap"` |
| Six `V^{⊗4}` placements match an independent signed formula; four local triples | `python3 -m pytest tests/test_audit_regressions.py tests/test_supergroup_gl21.py -k "embeddings or local"` |
| Every entry of the 9x9 matrix equals Çelik–Çelik p. 261 | `python3 -m pytest tests/test_audit_regressions.py -k primary_source` |
| `R_21` intertwines the coproduct for all four generators; braid sectors `q`, `-q^{-1}` | `python3 -m pytest tests/test_audit_regressions.py -k "intertwining or sectors"` |
| Full Clebsch–Gordan change of basis for `(1,1)`, `(2,2)`, `(3,2)` | `python3 -m pytest tests/test_audit_regressions.py -k cg` |
| Thesis figures regenerated from package output | `make figures` |

## Repository layout

```text
quantum_group/        the package (linalg.py holds the shared kron/zero-test helpers)
tests/                pytest suite; doctests in quantum_group/ run with it
examples/             quickstart.py, sample_verification.py (+ expected output)
benchmarks/           timing script and recorded results
notebooks/            exploratory notebook
paper/                JOSS manuscript (paper.md, paper.bib) and maintainer records
jors/                 JORS software metapaper and submission records (see jors/README.md)
thesis/, poster/      historical thesis material (Turkish); see thesis/README.md
AUDIT.md              mathematical/technical audit (September 2026)
MANUSCRIPT_CODE_MAPPING.md
main.py               demo script (writes outputs/V4_combined.png)
```

Makefile targets: `make check`, `make quickstart`, `make demo`,
`make figures`, `make benchmark-smoke`, `make joss-pdf` (official JOSS Inara
Docker image), and `make historical-article-pdf`, which builds the earlier
Turkish article `thesis/thesis.tex` — not the JOSS paper and not the
submitted thesis (`thesis/Lisans Bitirme Tezi.pdf`). Corrections to the
archived thesis are listed in [`thesis/ERRATA.md`](thesis/ERRATA.md).

## Contributing and support

Bug reports, questions and suggestions are welcome through
[GitHub issues](https://github.com/TerekliTahaBerk/quantum-groups/issues);
see [`CONTRIBUTING.md`](CONTRIBUTING.md). The package is maintained by its
author on a best-effort basis. Changes are listed in
[`CHANGELOG.md`](CHANGELOG.md).

## Citation

Please cite the software using [`CITATION.cff`](CITATION.cff) (GitHub's
"Cite this repository" button exports it). Version 1.0.0 is archived on
Zenodo as [10.5281/zenodo.22997681](https://doi.org/10.5281/zenodo.22997681);
that archive does **not** contain the changes listed for 1.1.0 in the
changelog.

## License

MIT; see [`LICENSE`](LICENSE).
