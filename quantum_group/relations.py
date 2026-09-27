"""
relations.py
============

Defining relations of U_q(sl_2) and their verification.

Defining relations
------------------
    (R1)  K K^{-1} = K^{-1} K = 1
    (R2)  K E K^{-1} = q^{ 2} E
    (R3)  K F K^{-1} = q^{-2} F
    (R4)  [E, F] = (K - K^{-1}) / (q - q^{-1})

At the symbolic level these relations can only be stated as definitions; a
concrete matrix representation is used to check them. The
`verify_on_representation` function tests whether a representation satisfies
all four relations by checking that their residual matrices are zero.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Dict, List, Tuple

import sympy as sp

from .generators import E, F, K, K_inv, commutator
from .utils import q


# ---------------------------------------------------------------------------
# Symbolic relation list (for reference documentation)
# ---------------------------------------------------------------------------

def symbolic_relations() -> List[Tuple[str, sp.Expr, sp.Expr]]:
    """Return the four defining U_q(sl_2) relations as (LHS, RHS) pairs.

    At the symbolic level, these pairs only name the relations.
    """
    return [
        ("R1: KK^{-1} = 1", K * K_inv, sp.Integer(1)),
        ("R2: KEK^{-1} = q^2 E", K * E * K_inv, q**2 * E),
        ("R3: KFK^{-1} = q^-2 F", K * F * K_inv, q**(-2) * F),
        ("R4: [E,F] = (K - K^-1)/(q - q^-1)",
         commutator(E, F),
         (K - K_inv) / (q - q**(-1))),
    ]


def pretty_print_relations() -> str:
    """Return a readable rendering of the relations."""
    out = ["Defining relations of U_q(sl_2):"]
    for name, lhs, rhs in symbolic_relations():
        out.append(f"  {name}:  {lhs}  =  {rhs}")
    return "\n".join(out)


# ---------------------------------------------------------------------------
# Matrix verification
# ---------------------------------------------------------------------------

@dataclass
class RelationCheck:
    """Result of checking one relation with matrices."""
    name: str
    holds: bool
    residual: sp.Matrix  # LHS - RHS; zero matrix if the relation holds

    def __repr__(self) -> str:  # pragma: no cover - cosmetic
        status = "OK" if self.holds else "FAILED"
        return f"<{self.name}: {status}>"


def is_zero_matrix(M: sp.Matrix) -> bool:
    """Test whether a SymPy matrix is symbolically zero.

    The check applies ``sympy.simplify`` both to the matrix and to each entry.
    This public helper implements the paper's zero-residual verification pattern.
    """
    M_simplified = sp.simplify(M)
    return all(sp.simplify(entry) == 0 for entry in M_simplified)


def _is_zero_matrix(M: sp.Matrix) -> bool:
    """Backward-compatible private alias; use ``is_zero_matrix`` publicly."""
    return is_zero_matrix(M)


def verify_on_representation(
    E_mat: sp.Matrix,
    F_mat: sp.Matrix,
    K_mat: sp.Matrix,
    Kinv_mat: sp.Matrix,
    q_sym: sp.Expr = q,
) -> Dict[str, RelationCheck]:
    """Check the U_q(sl_2) relations for matrices E, F, K, K^{-1}.

    Parameters
    ----------
    E_mat, F_mat, K_mat, Kinv_mat : sympy.Matrix
        Concrete matrix representations of the generators. All must have
        the same (n+1) x (n+1) shape.
    q_sym : sympy expression
        The q parameter used in the relations.

    Returns
    -------
    A dictionary mapping relation names to RelationCheck objects.
    """
    q_sym = sp.sympify(q_sym)
    if q_sym in (0, 1, -1):
        raise ValueError("The defining commutator quotient requires q != 0, 1, -1; use classical limits separately.")
    n = E_mat.rows
    I = sp.eye(n)

    checks: Dict[str, RelationCheck] = {}

    # R1: K K^{-1} = I
    res = K_mat * Kinv_mat - I
    checks["R1"] = RelationCheck("R1: KK^{-1} = 1", is_zero_matrix(res), res)

    # R2: K E K^{-1} = q^2 E
    res = K_mat * E_mat * Kinv_mat - q_sym**2 * E_mat
    checks["R2"] = RelationCheck("R2: KEK^{-1} = q^2 E", is_zero_matrix(res), res)

    # R3: K F K^{-1} = q^{-2} F
    res = K_mat * F_mat * Kinv_mat - q_sym**(-2) * F_mat
    checks["R3"] = RelationCheck("R3: KFK^{-1} = q^{-2} F", is_zero_matrix(res), res)

    # R4: [E, F] = (K - K^{-1}) / (q - q^{-1})
    res = (E_mat * F_mat - F_mat * E_mat) - (K_mat - Kinv_mat) / (q_sym - q_sym**(-1))
    checks["R4"] = RelationCheck(
        "R4: [E,F] = (K - K^{-1})/(q - q^{-1})",
        is_zero_matrix(res),
        res,
    )

    return checks


def verify_relations_core(
    E: sp.Matrix,
    F: sp.Matrix,
    K: sp.Matrix,
    K_inv: sp.Matrix,
    q_sym: sp.Expr = q,
) -> Dict[str, RelationCheck]:
    """Manuscript-compatible wrapper for ``verify_on_representation``.

    The repository's stable API is ``verify_on_representation``. The manuscript
    and older notes sometimes use ``verify_relations_core`` for the same
    matrix-level relation check, so this wrapper preserves that name without
    duplicating logic.
    """
    return verify_on_representation(E, F, K, K_inv, q_sym=q_sym)


def all_relations_hold(checks: Dict[str, RelationCheck]) -> bool:
    """Return whether all relations hold (convenience function)."""
    return all(c.holds for c in checks.values())
