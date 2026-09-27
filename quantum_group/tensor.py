"""
tensor.py
=========

Tensor products and Clebsch–Gordan decomposition of U_q(sl_2) representations.

The tensor product action is induced by the coproduct Δ:

    X . (v ⊗ w) = Δ(X) . (v ⊗ w)

Thus the generators act on V_m ⊗ V_n as follows:

    E . (v ⊗ w) = E v ⊗ w + K v ⊗ E w
    F . (v ⊗ w) = F v ⊗ K^{-1} w + v ⊗ F w
    K . (v ⊗ w) = K v ⊗ K w

Clebsch–Gordan decomposition (the same structure as in the classical case):

    V_m ⊗ V_n  ≅  V_{m+n}  ⊕  V_{m+n-2}  ⊕  ...  ⊕  V_{|m-n|}

This module constructs the action matrices on V_m ⊗ V_n and explicitly
computes a highest-weight vector for each direct-sum component.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import List, Tuple

import sympy as sp

from .representations import Representation, build_representation
from .hopf import _kron
from .utils import q as default_q


@dataclass
class TensorRepresentation:
    """Container for V_m ⊗ V_n."""
    m: int
    n: int
    dim: int
    E: sp.Matrix
    F: sp.Matrix
    K: sp.Matrix
    K_inv: sp.Matrix


def tensor_product(repA: Representation, repB: Representation) -> TensorRepresentation:
    """Construct the matrix action of generators on V_m ⊗ V_n via Δ.

    Basis order: e_{i,j} = v_i^A ⊗ v_j^B, lexicographic (first i, then j).
    """
    nA, nB = repA.dim, repB.dim
    IA = sp.eye(nA)
    IB = sp.eye(nB)

    E = _kron(repA.E, IB) + _kron(repA.K, repB.E)
    F = _kron(repA.F, repB.K_inv) + _kron(IA, repB.F)
    K = _kron(repA.K, repB.K)
    K_inv = _kron(repA.K_inv, repB.K_inv)

    return TensorRepresentation(
        m=repA.n, n=repB.n, dim=nA * nB,
        E=sp.simplify(E), F=sp.simplify(F),
        K=sp.simplify(K), K_inv=sp.simplify(K_inv),
    )


# ---------------------------------------------------------------------------
# Clebsch–Gordan decomposition
# ---------------------------------------------------------------------------

def cg_summands(m: int, n: int) -> List[int]:
    """List the k values appearing in V_m ⊗ V_n = ⊕ V_k.

    k = |m-n|, |m-n|+2, ..., m+n  (all have the parity of m+n).
    """
    lo = abs(m - n)
    hi = m + n
    return list(range(lo, hi + 1, 2))


def find_highest_weight_vectors(
    tensor_rep: TensorRepresentation,
    q_sym: sp.Expr = default_q,
) -> List[Tuple[int, sp.Matrix]]:
    """Find all highest-weight vectors in V_m ⊗ V_n.

    A vector v has highest weight k when:
        E . v = 0     and     K . v = q^k v.

    Returns a list of (k, v) pairs in descending order of k.

    Algorithm:
        For each candidate k = |m-n|, |m-n|+2, ..., m+n, select the
        weight subspace with K-eigenvalue q^k by its diagonal indices,
        then compute the kernel of E on that subspace.
    """
    m, n = tensor_rep.m, tensor_rep.n
    summands = cg_summands(m, n)

    # K is diagonal; compute its q-exponent for each basis vector.
    K_diag_exponents = []
    for i in range(m + 1):
        for j in range(n + 1):
            # K-exponents: m - 2i for v_i^A and n - 2j for v_j^B.
            K_diag_exponents.append((m - 2 * i) + (n - 2 * j))

    results: List[Tuple[int, sp.Matrix]] = []
    for k in reversed(summands):
        # Collect indices of the weight-k subspace.
        idx = [t for t, w in enumerate(K_diag_exponents) if w == k]
        if not idx:
            continue
        # Restrict E to this indexed subspace and find its kernel.
        E_sub = sp.Matrix([[tensor_rep.E[r, c] for c in idx] for r in idx])
        # E maps this weight subspace to the next one. For its full kernel,
        # inspect the columns indexed by idx across all target rows.
        E_cols = sp.Matrix([[tensor_rep.E[r, c] for c in idx]
                            for r in range(tensor_rep.dim)])
        null = E_cols.nullspace()
        # Embed each nullspace vector back into the full V_m ⊗ V_n basis.
        for vec in null:
            full = sp.zeros(tensor_rep.dim, 1)
            for local_i, global_i in enumerate(idx):
                full[global_i, 0] = vec[local_i, 0]
            full = sp.simplify(full)
            results.append((k, full))

    return results


def cg_decomposition_summary(m: int, n: int) -> str:
    """Return a readable summary of the V_m ⊗ V_n decomposition."""
    summands = cg_summands(m, n)
    parts = " ⊕ ".join(f"V_{k}" for k in reversed(summands))
    total = sum(k + 1 for k in summands)
    return f"V_{m} ⊗ V_{n} ≅ {parts}    (dimension: {(m+1)*(n+1)} = {total})"
