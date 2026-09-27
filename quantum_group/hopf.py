"""
hopf.py
=======

Hopf algebra structure of U_q(sl_2): coproduct Δ, counit ε, antipode S.

Definitions (on generators)
---------------------------
    Δ(E) = E ⊗ 1 + K ⊗ E
    Δ(F) = F ⊗ K^{-1} + 1 ⊗ F
    Δ(K) = K ⊗ K
    Δ(K^{-1}) = K^{-1} ⊗ K^{-1}

    ε(E) = 0,  ε(F) = 0,  ε(K) = 1,  ε(K^{-1}) = 1

    S(E) = -K^{-1} E
    S(F) = -F K
    S(K) = K^{-1}
    S(K^{-1}) = K

Hopf axioms (checkable as matrices on a representation V):

    (H1)  Coassociativity: (Δ ⊗ id) Δ(X) = (id ⊗ Δ) Δ(X)
    (H2)  Counit: (ε ⊗ id) Δ(X) = X = (id ⊗ ε) Δ(X)
    (H3)  Antipode: μ ∘ (S ⊗ id) ∘ Δ(X) = ε(X) · 1 = μ ∘ (id ⊗ S) ∘ Δ(X)

Here μ denotes matrix multiplication (algebra multiplication).

Given a Representation object, this module checks the three axioms for each
generator using Kronecker products (matrix tensor products).
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Dict, Tuple

import sympy as sp

from .representations import Representation
from .utils import q as default_q


# ---------------------------------------------------------------------------
# Hopf structure maps at the matrix level
# ---------------------------------------------------------------------------

def coproduct(rep: Representation) -> Dict[str, sp.Matrix]:
    """Return the matrix representation of Δ(X) on V ⊗ V.

    For a representation V, compute the matrix from the formulas using the
    standard Kronecker basis order: the first V index changes slowly and the
    second changes quickly.
    """
    I = sp.eye(rep.dim)

    return {
        "E": _kron(rep.E, I) + _kron(rep.K, rep.E),
        "F": _kron(rep.F, rep.K_inv) + _kron(I, rep.F),
        "K": _kron(rep.K, rep.K),
        "K_inv": _kron(rep.K_inv, rep.K_inv),
    }


def counit() -> Dict[str, sp.Expr]:
    """Return the counit ε: U_q(sl_2) -> Q(q) on generators."""
    return {
        "E": sp.Integer(0),
        "F": sp.Integer(0),
        "K": sp.Integer(1),
        "K_inv": sp.Integer(1),
    }


def antipode(rep: Representation) -> Dict[str, sp.Matrix]:
    """Return the matrix representation of S(X) on V."""
    return {
        "E": -rep.K_inv * rep.E,
        "F": -rep.F * rep.K,
        "K": rep.K_inv,
        "K_inv": rep.K,
    }


def _kron(A: sp.Matrix, B: sp.Matrix) -> sp.Matrix:
    """Kronecker (tensor) product of SymPy matrices."""
    m, n = A.shape
    p, qd = B.shape
    out = sp.zeros(m * p, n * qd)
    for i in range(m):
        for j in range(n):
            block = A[i, j] * B
            out[i * p:(i + 1) * p, j * qd:(j + 1) * qd] = block
    return out


def kron_list(mats: Tuple[sp.Matrix, ...] | list[sp.Matrix]) -> sp.Matrix:
    """Return the left-to-right Kronecker product of the given matrices."""
    if not mats:
        raise ValueError("kron_list requires at least one matrix.")
    result = mats[0]
    for M in mats[1:]:
        result = _kron(result, M)
    return result


# ---------------------------------------------------------------------------
# Verification of Hopf axioms
# ---------------------------------------------------------------------------

@dataclass
class HopfAxiomCheck:
    name: str
    holds: bool
    detail: str = ""

    def __repr__(self) -> str:  # pragma: no cover
        return f"<{self.name}: {'OK' if self.holds else 'FAILED'}>"


def verify_counit(rep: Representation) -> Dict[str, HopfAxiomCheck]:
    """Check (ε ⊗ id) Δ(X) = X = (id ⊗ ε) Δ(X).

    The counit ε is scalar-valued, and ε ⊗ id contracts a tensor from
    V ⊗ V to V. For n-dimensional V, Δ(X) is an n²×n² matrix. To apply
    ε ⊗ id, we need a decomposition Δ(X) = Σ X_(1) ⊗ X_(2), rather than
    just its matrix. The construction uses the known formula for each
    generator, Δ(X) = Σ A_i ⊗ B_i.
    """
    return _verify_counit_via_labels(rep)


def _verify_counit_via_labels(rep: Representation) -> Dict[str, HopfAxiomCheck]:
    """Check the counit axiom using a labelled decomposition of Δ."""
    n = rep.dim
    I = sp.eye(n)
    eps = counit()

    # Labelled decomposition: Δ(X) = Σ X1_i ⊗ X2_i for each generator X.
    # X1_i and X2_i are labels from {E, F, K, K_inv, 1}.
    # ε maps E and F to zero, and K and K_inv to one.
    decompositions = {
        "E": [("E", "1"), ("K", "E")],
        "F": [("F", "K_inv"), ("1", "F")],
        "K": [("K", "K")],
        "K_inv": [("K_inv", "K_inv")],
    }
    label_to_mat = {"E": rep.E, "F": rep.F, "K": rep.K,
                    "K_inv": rep.K_inv, "1": I}
    label_to_eps = {**eps, "1": sp.S.One}
    target = {"E": rep.E, "F": rep.F, "K": rep.K, "K_inv": rep.K_inv}

    results: Dict[str, HopfAxiomCheck] = {}
    for X, terms in decompositions.items():
        # Left application: (ε ⊗ id) Δ(X) = Σ ε(X1_i) · X2_i
        left = sum((sp.Integer(label_to_eps[a]) * label_to_mat[b]
                    for (a, b) in terms), sp.zeros(n, n))
        # Right application: (id ⊗ ε) Δ(X) = Σ X1_i · ε(X2_i)
        right = sum((label_to_mat[a] * sp.Integer(label_to_eps[b])
                     for (a, b) in terms), sp.zeros(n, n))
        ok_left = sp.simplify(left - target[X]) == sp.zeros(n, n)
        ok_right = sp.simplify(right - target[X]) == sp.zeros(n, n)
        results[X] = HopfAxiomCheck(
            name=f"Counit ({X})",
            holds=bool(ok_left and ok_right),
        )
    return results


def verify_antipode(rep: Representation) -> Dict[str, HopfAxiomCheck]:
    """Check μ ∘ (S ⊗ id) ∘ Δ(X) = ε(X) · I = μ ∘ (id ⊗ S) ∘ Δ(X).

    The results are n×n matrix equations on V.
    """
    n = rep.dim
    I = sp.eye(n)
    eps = counit()
    S = antipode(rep)
    label_to_mat = {"E": rep.E, "F": rep.F, "K": rep.K,
                    "K_inv": rep.K_inv, "1": I}
    label_to_S = {"E": S["E"], "F": S["F"], "K": S["K"],
                  "K_inv": S["K_inv"], "1": I}

    decompositions = {
        "E": [("E", "1"), ("K", "E")],
        "F": [("F", "K_inv"), ("1", "F")],
        "K": [("K", "K")],
        "K_inv": [("K_inv", "K_inv")],
    }

    results: Dict[str, HopfAxiomCheck] = {}
    for X, terms in decompositions.items():
        # μ ∘ (S ⊗ id) ∘ Δ(X) = Σ S(X1_i) · X2_i
        left = sum((label_to_S[a] * label_to_mat[b]
                    for (a, b) in terms), sp.zeros(n, n))
        # μ ∘ (id ⊗ S) ∘ Δ(X) = Σ X1_i · S(X2_i)
        right = sum((label_to_mat[a] * label_to_S[b]
                     for (a, b) in terms), sp.zeros(n, n))
        target = sp.Integer(eps[X]) * I
        ok_left = sp.simplify(left - target) == sp.zeros(n, n)
        ok_right = sp.simplify(right - target) == sp.zeros(n, n)
        results[X] = HopfAxiomCheck(
            name=f"Antipode ({X})",
            holds=bool(ok_left and ok_right),
        )
    return results


def verify_coassociativity(rep: Representation) -> Dict[str, HopfAxiomCheck]:
    """Check (Δ ⊗ id) Δ(X) = (id ⊗ Δ) Δ(X) on V ⊗ V ⊗ V.

    This follows from the definition of Δ, but gives an explicit matrix-level
    verification.
    """
    n = rep.dim
    I = sp.eye(n)
    Delta = coproduct(rep)

    # (Δ ⊗ id) Δ(X): apply Δ to the left factor of the n² x n² matrix Δ(X).
    # Use the labelled decomposition Δ(X) = Σ A_i ⊗ B_i, then apply Δ to A_i.

    decompositions = {
        "E": [("E", "1"), ("K", "E")],
        "F": [("F", "K_inv"), ("1", "F")],
        "K": [("K", "K")],
        "K_inv": [("K_inv", "K_inv")],
    }
    label_to_mat = {"E": rep.E, "F": rep.F, "K": rep.K,
                    "K_inv": rep.K_inv, "1": I}
    label_to_Delta = {
        "E": Delta["E"],
        "F": Delta["F"],
        "K": Delta["K"],
        "K_inv": Delta["K_inv"],
        "1": _kron(I, I),
    }

    results: Dict[str, HopfAxiomCheck] = {}
    for X, terms in decompositions.items():
        # Left: Σ Δ(A_i) ⊗ B_i  (n^3 x n^3)
        left = sum((_kron(label_to_Delta[a], label_to_mat[b])
                    for (a, b) in terms), sp.zeros(n**3, n**3))
        # Right: Σ A_i ⊗ Δ(B_i)
        right = sum((_kron(label_to_mat[a], label_to_Delta[b])
                     for (a, b) in terms), sp.zeros(n**3, n**3))
        diff = sp.simplify(left - right)
        ok = diff == sp.zeros(n**3, n**3)
        results[X] = HopfAxiomCheck(
            name=f"Coassociativity ({X})",
            holds=bool(ok),
        )
    return results


def verify_all_hopf_axioms(rep: Representation) -> Dict[str, Dict[str, HopfAxiomCheck]]:
    """Check all Hopf axioms on V and return grouped results."""
    return {
        "coassociativity": verify_coassociativity(rep),
        "counit": _verify_counit_via_labels(rep),
        "antipode": verify_antipode(rep),
    }
