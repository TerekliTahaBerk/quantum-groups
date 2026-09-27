"""
r_matrix.py
===========

Symbolic verification of the R-matrix and Yang–Baxter / braid relations
for U_q(sl_2).

Convention
----------
There are two related matrices:

    R   :  V ⊗ V -> V ⊗ V    (Drinfeld universal R)
    Ř   :  V ⊗ V -> V ⊗ V    (braided R; Ř = τ ∘ R, τ swaps tensor factors)

Drinfeld's R satisfies the quantum Yang–Baxter equation:

        R_{12} R_{13} R_{23} = R_{23} R_{13} R_{12}              (QYBE)

Ř gives a representation of the braid group B_n; its **braid relation** is:

        Ř_{12} Ř_{23} Ř_{12} = Ř_{23} Ř_{12} Ř_{23}              (BRAID)

This module constructs and checks both structures on V_1 ⊗ V_1. The braid
relation is directly related to knot invariants such as the Jones polynomial.

R-matrix on V_1 ⊗ V_1 (rescaled, without fractional powers of q):

                | q   0      0       0 |
        R  =    | 0   1      q-q^-1  0 |
                | 0   0      1       0 |
                | 0   0      0       q |

Basis order: v_0⊗v_0, v_0⊗v_1, v_1⊗v_0, v_1⊗v_1.
"""

from __future__ import annotations

import warnings
from dataclasses import dataclass
from typing import Dict

import sympy as sp

from .representations import Representation
from .hopf import _kron
from .utils import q as default_q


# ---------------------------------------------------------------------------
# R-matrix and its braided version
# ---------------------------------------------------------------------------

def R_matrix_V1(q_sym: sp.Expr = default_q) -> sp.Matrix:
    """Drinfeld–Jimbo R-matrix on V_1 ⊗ V_1 (4×4).

    Derivation
    ----------
    The universal R-matrix of U_q(sl_2) (Drinfeld 1987) has the form

        𝓡 = q^{H⊗H/2} · (1 + (q - q^{-1}) E⊗F + ...)

    where K = q^H and "..." denotes terms E^n ⊗ F^n (n ≥ 2)
    (see Kassel 1995 for the full series). On V_1, E² = F² = 0, so the
    series truncates after two terms. With H = diag(1, -1),

        R = q^{1/2} · (ρ_1 ⊗ ρ_1)(𝓡)

    is exactly the matrix returned by this function. The factor q^{1/2}
    normalizes away fractional powers q^{±1/2}. This 4×4 matrix is the
    N = 1 case of Jimbo's vector-representation R-matrix for U_q(gl(N+1))
    (Jimbo 1985, 1986).

    Convention note
    ---------------
    The 𝓡 above satisfies Δ^op(x) 𝓡 = 𝓡 Δ(x) for the coproduct
    Δ(E) = E⊗K + 1⊗E, Δ(F) = F⊗1 + K^{-1}⊗F. This package's
    ``hopf.coproduct`` instead uses Δ(E) = E⊗1 + K⊗E,
    Δ(F) = F⊗K^{-1} + 1⊗F. For this coproduct, R_21 = τ R τ = R^T,
    rather than R, satisfies the same intertwining relation. Both R and
    R_21 satisfy the QYBE; this difference does not affect the QYBE,
    braid or Hecke checks in this module.

    References
    ----------
    * M. Jimbo, "A q-difference analogue of U(g) and the Yang–Baxter
      equation", Lett. Math. Phys. 10 (1985) 63–69,
      doi:10.1007/BF00704588.
    * M. Jimbo, "A q-analogue of U(gl(N+1)), Hecke algebra, and the
      Yang–Baxter equation", Lett. Math. Phys. 11 (1986) 247–252,
      doi:10.1007/BF00400222.
    * V. G. Drinfeld, "Quantum groups", Proc. ICM (Berkeley, 1986),
      Vol. 1, Amer. Math. Soc., 1987, 798–820.
    * C. Kassel, Quantum Groups, GTM 155, Springer, 1995,
      doi:10.1007/978-1-4612-0783-2.
    """
    qi = q_sym**(-1)
    return sp.Matrix([
        [q_sym, 0,         0,             0],
        [0,    1,          q_sym - qi,    0],
        [0,    0,          1,             0],
        [0,    0,          0,             q_sym],
    ])


def swap_matrix(d: int) -> sp.Matrix:
    """τ: V ⊗ V -> V ⊗ V, e_{ij} -> e_{ji}, where V has dimension d."""
    P = sp.zeros(d * d, d * d)
    for i in range(d):
        for j in range(d):
            P[j * d + i, i * d + j] = 1
    return P


def R_check_V1(q_sym: sp.Expr = default_q) -> sp.Matrix:
    """Return the braided R-matrix Ř = τ ∘ R."""
    return sp.simplify(swap_matrix(2) * R_matrix_V1(q_sym))


# ---------------------------------------------------------------------------
# Verification of the QYBE and braid relation
# ---------------------------------------------------------------------------

@dataclass
class RelationStatus:
    name: str
    holds: bool


def _is_zero(M: sp.Matrix) -> bool:
    return all(sp.simplify(e) == 0 for e in sp.simplify(M))


def braid_relation_residual(R: sp.Matrix) -> sp.Matrix:
    """Residual of the braid relation on V ⊗ V ⊗ V.

    For 4×4 R, the result is 8×8. The residual is zero if R satisfies
    the relation.
    """
    d = int(sp.sqrt(R.rows))
    if d * d != R.rows:
        raise ValueError("R must be square with dimension d².")
    I = sp.eye(d)
    R12 = _kron(R, I)
    R23 = _kron(I, R)
    return sp.simplify(R12 * R23 * R12 - R23 * R12 * R23)


def qybe_residual(R: sp.Matrix) -> sp.Matrix:
    """Residual of the quantum Yang–Baxter equation on V ⊗ V ⊗ V:

        R_{12} R_{13} R_{23} - R_{23} R_{13} R_{12}.

    R_{13} acts on factors 1 and 3, with identity on factor 2.
    """
    d = int(sp.sqrt(R.rows))
    if d * d != R.rows:
        raise ValueError("R must be square with dimension d².")
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
# Spectral decomposition
# ---------------------------------------------------------------------------

def R_check_eigenvalues(q_sym: sp.Expr = default_q) -> Dict[sp.Expr, int]:
    """Return eigenvalues and multiplicities of Ř on V_1 ⊗ V_1.

    Expected: q (multiplicity 3, symmetric V_2 sector) and −q^{-1}
    (multiplicity 1, V_0). This spectrum is the braided counterpart of
    V_1 ⊗ V_1 = V_2 ⊕ V_0 and is an input to the Jones polynomial.
    """
    Rv = R_check_V1(q_sym)
    raw = Rv.eigenvals()
    return {sp.simplify(k): v for k, v in raw.items()}


def hecke_skein_relation_check(q_sym: sp.Expr = default_q) -> Dict[str, bool]:
    """Check the Hecke (skein) relation.

    The quadratic Hecke relation between Ř and Ř^{-1} is:
        Ř - Ř^{-1} = (q - q^{-1}) · I
    This shows that the braid representation of U_q(sl_2) on V_1
    factors through the Hecke algebra H_n(q).

    Only the Hecke relation is checked; the Jones polynomial and Markov
    trace are not computed.
    """
    Rv = R_check_V1(q_sym)
    Rv_inv = sp.simplify(Rv.inv())
    diff = sp.simplify(Rv - Rv_inv - (q_sym - q_sym**(-1)) * sp.eye(4))
    return {
        "Ř - Ř^{-1} = (q - q^{-1}) I": _is_zero(diff),
    }


def jones_skein_relation_check(q_sym: sp.Expr = default_q) -> Dict[str, bool]:
    """Deprecated: use ``hecke_skein_relation_check``.

    The old name was misleading: this verifies the Hecke relation, not a
    Jones polynomial. The alias remains for backward compatibility.
    """
    warnings.warn(
        "jones_skein_relation_check is deprecated; "
        "use hecke_skein_relation_check instead",
        DeprecationWarning,
        stacklevel=2,
    )
    return hecke_skein_relation_check(q_sym)
