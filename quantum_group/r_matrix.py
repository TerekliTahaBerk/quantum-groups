"""
r_matrix.py
===========

U_q(sl_2) için R-matris ve Yang–Baxter / örgü ilişkilerinin sembolik
doğrulanması.

Konvansiyon
-----------
İki ilgili matris vardır:

    R   :  V ⊗ V -> V ⊗ V    (Drinfeld universal R)
    Ř   :  V ⊗ V -> V ⊗ V    (örgülü R; Ř = τ ∘ R, τ tensör değiştirme)

Drinfeld R kuantum Yang–Baxter denklemini sağlar:

        R_{12} R_{13} R_{23} = R_{23} R_{13} R_{12}              (QYBE)

Ř ise örgü grup B_n'nin temsilini verir; **örgü bağıntısı**:

        Ř_{12} Ř_{23} Ř_{12} = Ř_{23} Ř_{12} Ř_{23}              (BRAID)

Bu modül her iki yapıyı da V_1 ⊗ V_1 üzerinde inşa eder ve doğrular.
Örgü bağıntısı düğüm değişmezleriyle (Jones polinomu) doğrudan ilişkili
olduğu için fiziksel olarak ana sonuçtur.

V_1 ⊗ V_1 üzerinde R-matrisi (renormalize, fraksiyonel q-üssü yok):

                | q   0      0       0 |
        R  =    | 0   1      q-q^-1  0 |
                | 0   0      1       0 |
                | 0   0      0       q |

Baz sıralaması: v_0⊗v_0, v_0⊗v_1, v_1⊗v_0, v_1⊗v_1.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Dict

import sympy as sp

from .representations import Representation
from .hopf import _kron
from .utils import q as default_q


# ---------------------------------------------------------------------------
# R-matris ve örgülü versiyonu
# ---------------------------------------------------------------------------

def R_matrix_V1(q_sym: sp.Expr = default_q) -> sp.Matrix:
    """V_1 ⊗ V_1 üzerinde Drinfeld R-matrisi (4×4)."""
    qi = q_sym**(-1)
    return sp.Matrix([
        [q_sym, 0,         0,             0],
        [0,    1,          q_sym - qi,    0],
        [0,    0,          1,             0],
        [0,    0,          0,             q_sym],
    ])


def swap_matrix(d: int) -> sp.Matrix:
    """τ: V ⊗ V -> V ⊗ V, e_{ij} -> e_{ji}, V boyutu d."""
    P = sp.zeros(d * d, d * d)
    for i in range(d):
        for j in range(d):
            P[j * d + i, i * d + j] = 1
    return P


def R_check_V1(q_sym: sp.Expr = default_q) -> sp.Matrix:
    """Örgülü R-matris Ř = τ ∘ R."""
    return sp.simplify(swap_matrix(2) * R_matrix_V1(q_sym))


# ---------------------------------------------------------------------------
# QYBE ve örgü bağıntısının doğrulanması
# ---------------------------------------------------------------------------

@dataclass
class RelationStatus:
    name: str
    holds: bool


def _is_zero(M: sp.Matrix) -> bool:
    return all(sp.simplify(e) == 0 for e in sp.simplify(M))


def braid_relation_residual(R: sp.Matrix) -> sp.Matrix:
    """V ⊗ V ⊗ V üzerinde örgü bağıntısının kalıntısı.

    R 4×4 ise sonuç 8×8 olur. Eşitlik R sağlıyorsa kalıntı sıfırdır.
    """
    d = int(sp.sqrt(R.rows))
    if d * d != R.rows:
        raise ValueError("R kare olmalı ve boyutu d² olmalı.")
    I = sp.eye(d)
    R12 = _kron(R, I)
    R23 = _kron(I, R)
    return sp.simplify(R12 * R23 * R12 - R23 * R12 * R23)


def qybe_residual(R: sp.Matrix) -> sp.Matrix:
    """Kuantum Yang–Baxter denkleminin V ⊗ V ⊗ V üzerindeki kalıntısı:

        R_{12} R_{13} R_{23} - R_{23} R_{13} R_{12}.

    R_{13}: 1. ve 3. faktörlere etki, 2. faktörde özdeşlik.
    """
    d = int(sp.sqrt(R.rows))
    if d * d != R.rows:
        raise ValueError("R kare olmalı ve boyutu d² olmalı.")
    I = sp.eye(d)
    R12 = _kron(R, I)
    R23 = _kron(I, R)
    # R13 = (id ⊗ τ) (R ⊗ id) (id ⊗ τ)
    P23 = _kron(I, swap_matrix(d))
    R13 = sp.simplify(P23 * R12 * P23)
    return sp.simplify(R12 * R13 * R23 - R23 * R13 * R12)


def braid_relation_holds(R: sp.Matrix) -> bool:
    return _is_zero(braid_relation_residual(R))


def qybe_holds(R: sp.Matrix) -> bool:
    return _is_zero(qybe_residual(R))


# ---------------------------------------------------------------------------
# Spektral ayrışma
# ---------------------------------------------------------------------------

def R_check_eigenvalues(q_sym: sp.Expr = default_q) -> Dict[sp.Expr, int]:
    """Ř'nin V_1 ⊗ V_1 üzerindeki özdeğerlerini ve çokluklarını döndürür.

    Beklenen: q (3-katlı, V_2 simetrik kanat) ve −q^{-1} (1-katlı, V_0).
    Bu spektrum, V_1 ⊗ V_1 = V_2 ⊕ V_0 Clebsch–Gordan ayrışımının
    örgülü versiyonudur ve Jones polinomu için temel girdidir.
    """
    Rv = R_check_V1(q_sym)
    raw = Rv.eigenvals()
    return {sp.simplify(k): v for k, v in raw.items()}


def jones_skein_relation_check(q_sym: sp.Expr = default_q) -> Dict[str, bool]:
    """Jones tipi skein bağıntısının kontrolü.

    Ř ve Ř^{-1} arasında Hecke benzeri kuadratik bağıntı:
        Ř - Ř^{-1} = (q - q^{-1}) · I
    Bu bağıntı, U_q(sl_2)'nin V_1 üzerindeki örgü temsilinin Hecke
    cebirinin H_n(q) niceliği üzerinden faktör olduğunu gösterir.
    """
    Rv = R_check_V1(q_sym)
    Rv_inv = sp.simplify(Rv.inv())
    diff = sp.simplify(Rv - Rv_inv - (q_sym - q_sym**(-1)) * sp.eye(4))
    return {
        "Ř - Ř^{-1} = (q - q^{-1}) I": _is_zero(diff),
    }
