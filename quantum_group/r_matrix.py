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

import math
import warnings
from dataclasses import dataclass
from typing import Dict

import sympy as sp

from .representations import Representation
from ._validation import as_int, check_square
from .linalg import is_zero_matrix, kron
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

    is exactly the matrix returned by this function. See Drinfeld §13,
    pp. 816–817, with q = exp(h/2); the higher nilpotent terms vanish. The factor q^{1/2}
    normalizes away fractional powers q^{±1/2}. The source normalization
    is evaluated explicitly in AUDIT.md.

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
    q_sym = sp.sympify(q_sym)
    if q_sym == 0:
        raise ValueError("q must be nonzero.")
    qi = q_sym**(-1)
    return sp.Matrix([
        [q_sym, 0,         0,             0],
        [0,    1,          q_sym - qi,    0],
        [0,    0,          1,             0],
        [0,    0,          0,             q_sym],
    ])


def swap_matrix(d: int) -> sp.Matrix:
    """τ: V ⊗ V -> V ⊗ V, e_{ij} -> e_{ji}, where V has dimension d."""
    d = as_int(d, "d", minimum=1)
    P = sp.zeros(d * d, d * d)
    for i in range(d):
        for j in range(d):
            P[j * d + i, i * d + j] = 1
    return P


def R_check_V1(q_sym: sp.Expr = default_q) -> sp.Matrix:
    """Return the braided R-matrix Ř = τ ∘ R."""
    return sp.simplify(swap_matrix(2) * R_matrix_V1(q_sym))


def R_matrix_V1_coproduct(q_sym: sp.Expr = default_q) -> sp.Matrix:
    """Return R_21 = P R P, compatible with ``hopf.coproduct``.

    R_21 Δ(X) = Δ^op(X) R_21 for E, F, K, K_inv. The historical
    ``R_matrix_V1`` keeps its upper-triangular convention for compatibility.
    """
    return R_matrix_V1(q_sym).T


def R_check_V1_coproduct(q_sym: sp.Expr = default_q) -> sp.Matrix:
    """Return P R_21 = R P, commuting with the package coproduct action."""
    return swap_matrix(2) * R_matrix_V1_coproduct(q_sym)


def intertwining_residual_V1(
    generator: str, q_sym: sp.Expr = default_q
) -> sp.Matrix:
    """Return R_21 Δ(X) − Δ^op(X) R_21 on V_1 ⊗ V_1.

    ``generator`` is E, F, K or K_inv; other names raise ValueError.
    """
    from .hopf import coproduct
    from .representations import build_representation

    actions = coproduct(build_representation(1, q_sym))
    if generator not in actions:
        raise ValueError("generator must be E, F, K or K_inv.")
    action = actions[generator]
    P = swap_matrix(2)
    R = R_matrix_V1_coproduct(q_sym)
    return (R * action - P * action * P * R).applyfunc(sp.cancel)


def intertwining_holds_V1(generator: str, q_sym: sp.Expr = default_q) -> bool:
    """Whether the fundamental coproduct-intertwining residual is zero."""
    return is_zero_matrix(intertwining_residual_V1(generator, q_sym))


# ---------------------------------------------------------------------------
# Verification of the QYBE and braid relation
# ---------------------------------------------------------------------------

@dataclass
class RelationStatus:
    name: str
    holds: bool


# Backward-compatible private alias; the helper now lives in ``linalg``.
_is_zero = is_zero_matrix


def _tensor_square_dim(R: sp.Matrix) -> int:
    """Return d for a square d²×d² matrix R, or raise ValueError."""
    rows, _ = check_square(R, "R")
    d = math.isqrt(rows)
    if d == 0 or d * d != rows:
        raise ValueError(f"R must be square with dimension d²; got shape {R.shape}.")
    return d


def braid_relation_residual(R: sp.Matrix) -> sp.Matrix:
    """Residual of the braid relation on V ⊗ V ⊗ V.

    For 4×4 R, the result is 8×8. The residual is zero if R satisfies
    the relation.
    """
    d = _tensor_square_dim(R)
    I = sp.eye(d)
    R12 = kron(R, I)
    R23 = kron(I, R)
    return sp.simplify(R12 * R23 * R12 - R23 * R12 * R23)


def qybe_residual(R: sp.Matrix) -> sp.Matrix:
    """Residual of the quantum Yang–Baxter equation on V ⊗ V ⊗ V:

        R_{12} R_{13} R_{23} - R_{23} R_{13} R_{12}.

    R_{13} acts on factors 1 and 3, with identity on factor 2.
    """
    d = _tensor_square_dim(R)
    I = sp.eye(d)
    R12 = kron(R, I)
    R23 = kron(I, R)
    # R13 = (id ⊗ τ) (R ⊗ id) (id ⊗ τ)
    P23 = kron(I, swap_matrix(d))
    R13 = sp.simplify(P23 * R12 * P23)
    return sp.simplify(R12 * R13 * R23 - R23 * R13 * R12)


def braid_relation_holds(R: sp.Matrix) -> bool:
    return is_zero_matrix(braid_relation_residual(R))


def qybe_holds(R: sp.Matrix) -> bool:
    return is_zero_matrix(qybe_residual(R))


# ---------------------------------------------------------------------------
# Spectral decomposition
# ---------------------------------------------------------------------------

def R_check_eigenvalues(q_sym: sp.Expr = default_q) -> Dict[sp.Expr, int]:
    """Return eigenvalues and multiplicities of Ř on V_1 ⊗ V_1.

    Generically q has multiplicity 3 and −q^{-1} multiplicity 1. These
    sectors use the opposite coproduct, not ``hopf.coproduct``. Use
    ``R_check_V1_coproduct`` for the package tensor-product submodules.
    At q² = −1 the eigenvalues merge and the matrix is not diagonalizable.
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
    q_sym = sp.sympify(q_sym)
    Rv = R_check_V1(q_sym)
    Rv_inv = sp.simplify(Rv.inv())
    diff = sp.simplify(Rv - Rv_inv - (q_sym - q_sym**(-1)) * sp.eye(4))
    return {
        "Ř - Ř^{-1} = (q - q^{-1}) I": is_zero_matrix(diff),
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
