# Quantum Grup Yapılarının Python Ortamında Modellenmesi

Bu depo, `U_q(sl_2)` ve `GL_q(2|1)` yapıları için SymPy tabanlı sembolik
modelleme ve doğrulama kodlarını içerir. Amaç genel bir teorem ispatlayıcı
oluşturmak değil; makaledeki açık sonlu boyutlu temsiller, kalıntı matrisleri,
Yang-Baxter kontrolleri ve ilgili şekilleri yeniden üretilebilir testlere
bağlamaktır.

## Main Features

- `q`-tamsayı, `q`-faktöriyel, `q`-binom ve klasik limit yardımcıları.
- `U_q(sl_2)` sonlu boyutlu `V_n` temsilleri için açık `E`, `F`, `K`, `K_inv`
  matrisleri.
- Tanımlayıcı bağıntıların temsil düzeyinde sıfır-kalıntı doğrulaması.
- Hopf yapısı: eş-çarpım, eş-birim, antipod ve aksiyom kontrolleri.
- Tensör çarpımı, Clebsch-Gordan örnekleri ve en yüksek ağırlık vektörleri.
- `V_1 \otimes V_1` R-matrisi, QYBE, örgü bağıntısı, Hecke/skein kontrolü.
- `GL_q(2|1)` için 9x9 R-matrisi, süper permütasyon ve 27x27 graded YBE
  doğrulaması.
- `V^{\otimes n}` içinde `R_{ij}` yerleşimleri, uzak komütativite ve lokal YBE
  kontrolleri.
- Kristal grafiği `B(n)` ve temel görselleştirme fonksiyonları.
- `pytest` tabanlı yeniden üretilebilir test paketi.

## Installation

Python 3.10+ önerilir. Bu depoda şu an `pyproject.toml` veya `setup.py`
bulunmadığı için kurulum `requirements.txt` üzerinden yapılır.

```bash
python3 -m venv .venv
source .venv/bin/activate
python3 -m pip install -r requirements.txt
```

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

The `GL_q(2|1)` tensor-power checks use symbolic `81x81` matrices and may be
the slowest part of the suite.

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
│   ├── Quantum Grup Yapılarının Python Ortamında Modellenmesi.pdf
│   └── figures/
│       ├── generate_figures.py
│       ├── R_sl2_V1.pdf
│       ├── R_gl21_structure.pdf
│       └── ybe_products_27.pdf
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

The LaTeX source is `thesis/thesis.tex`. If Tectonic is installed, rebuild the
main manuscript PDF with:

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

- Symbolic simplification can be expensive for larger tensor powers.
- Most checks are explicit finite-dimensional representation-level
  verifications, not general formal proofs inside an abstract proof assistant.
- Root-of-unity behavior is exploratory; the package does not implement the
  full small quantum group theory.
- `crystal.py` implements the combinatorial crystal graph `B(n)`; it does not
  construct a full Kashiwara global basis.
- The Hecke/skein relation and braid representation are checked, but the Jones
  polynomial and Markov trace are not implemented.

## Citation

If you use this repository, please cite:

```text
[manuscript citation to be added]
```
