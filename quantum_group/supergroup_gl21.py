"""
supergroup_gl21.py
==================

Computer-assisted symbolic verification of the graded (Z_2-graded)
Yang–Baxter equation for the quantum supergroup **GL_q(2|1)** introduced
by Çelik & Çelik (Reports on Mathematical Physics, **88** (2021), 259).

Mathematical background
-----------------------
GL_q(2|1) is defined on the super vector space V = C^{2|1}. Its basis
vectors e_1, e_2, e_3 have parities (Z_2-degrees):

    p(e_1) = 0,  p(e_2) = 0,  p(e_3) = 1   ->   parity = [0, 0, 1]

The first two vectors are **even**; the third is **odd**.

The R-matrix given on page 261 of the paper acts on V ⊗ V (dimension 9)
and has size 9×9. The basis order (with internal zero-based indexing) is:

    e_1⊗e_1, e_1⊗e_2, e_1⊗e_3,
    e_2⊗e_1, e_2⊗e_2, e_2⊗e_3,
    e_3⊗e_1, e_3⊗e_2, e_3⊗e_3

The R-matrix satisfies the graded Yang–Baxter equation:

    R12 R13 R23 = R23 R13 R12          (on V ⊗ V ⊗ V, 27×27)

where, following the paper's definition,

    R12 = R ⊗ I_3
    R23 = I_3 ⊗ R
    R13 = (P ⊗ I_3) R23 (P ⊗ I_3)

and P is the super-permutation matrix:

    P(e_i ⊗ e_j) = (-1)^{p(i) p(j)} e_j ⊗ e_i.

Since parity = [0, 0, 1], P differs from the ordinary swap matrix only in
the odd-odd component, where P^{33}_{33} = -1.

This module turns a lengthy, error-prone manual graded Yang–Baxter
calculation into a symbolic verification procedure that can be modelled,
tested and reproduced in Python/SymPy.
"""

from __future__ import annotations

from itertools import combinations
from typing import Dict, List, Tuple

import sympy as sp

from .hopf import kron_list
from .utils import q as default_q


# ---------------------------------------------------------------------------
# Core data: parity, basis and R-matrix
# ---------------------------------------------------------------------------

def super_parity_gl21() -> List[int]:
    """Return the Z_2 parities of the GL_q(2|1) basis vectors.

    e_1 and e_2 are even (0); e_3 is odd (1). Thus [0, 0, 1].
    """
    return [0, 0, 1]


def basis_pairs_gl21() -> List[Tuple[int, int]]:
    """Return (i, j) pairs of the V ⊗ V basis with **zero-based indices**.

    Row-major order:
    (0,0), (0,1), (0,2), (1,0), (1,1), (1,2), (2,0), (2,1), (2,2).
    Index k = 3*i + j corresponds to e_{i+1} ⊗ e_{j+1} in the paper.
    """
    return [(i, j) for i in range(3) for j in range(3)]


def R_matrix_GLq21(q_sym: sp.Expr = default_q) -> sp.Matrix:
    """Return the GL_q(2|1) R-matrix (9×9) from page 261 of the paper.

    The basis order matches ``basis_pairs_gl21()``.
    """
    q = sp.sympify(q_sym)
    return sp.Matrix([
        [1, 0,      0,  0,        0, 0,      0,        0,      0],
        [0, q**2,   0,  1 - q**2, 0, 0,      0,        0,      0],
        [0, 0,      q,  0,        0, 0,      1 - q**2, 0,      0],
        [0, 0,      0,  1,        0, 0,      0,        0,      0],
        [0, 0,      0,  0,        1, 0,      0,        0,      0],
        [0, 0,      0,  0,        0, q,      0,        1 - q**2, 0],
        [0, 0,      0,  0,        0, 0,      q,        0,      0],
        [0, 0,      0,  0,        0, 0,      0,        q,      0],
        [0, 0,      0,  0,        0, 0,      0,        0,      q**2],
    ])


# ---------------------------------------------------------------------------
# Super-permutation and Kronecker helpers
# ---------------------------------------------------------------------------

def super_permutation_matrix(parity: List[int]) -> sp.Matrix:
    """Return the graded swap (super-permutation) matrix on V ⊗ V.

        P(e_i ⊗ e_j) = (-1)^{p(i) p(j)} e_j ⊗ e_i.

    For d = len(parity), the result has shape (d², d²). With
    parity = [0, 0, 1], it differs from the ordinary swap only at
    P[8, 8] = -1 (the e_3⊗e_3 component).
    """
    if not parity or any(p not in (0, 1) for p in parity):
        raise ValueError("parity must be a nonempty list of zeros and ones.")
    d = len(parity)
    P = sp.zeros(d * d, d * d)
    for i in range(d):
        for j in range(d):
            sign = -1 if (parity[i] and parity[j]) else 1
            # Input: e_i ⊗ e_j  (column index i*d + j)
            # Output: e_j ⊗ e_i  (row index j*d + i)
            P[j * d + i, i * d + j] = sign
    return P


def _kron_list(mats: List[sp.Matrix]) -> sp.Matrix:
    """Backward-compatible private alias; use ``kron_list`` publicly."""
    return kron_list(mats)


def _eye_pow(d: int, n: int) -> sp.Matrix:
    """I_d^{⊗n}; for n = 0, return the 1×1 identity (scalar unit)."""
    if n <= 0:
        return sp.eye(1)
    return sp.eye(d ** n)


# ---------------------------------------------------------------------------
# Three-factor embeddings: R12, R23, R13  (V ⊗ V ⊗ V, 27×27)
# ---------------------------------------------------------------------------

def R12_GLq21(q_sym: sp.Expr = default_q) -> sp.Matrix:
    """R12 = R ⊗ I_3  (27×27)."""
    return _kron_list([R_matrix_GLq21(q_sym), sp.eye(3)])


def R23_GLq21(q_sym: sp.Expr = default_q) -> sp.Matrix:
    """R23 = I_3 ⊗ R  (27×27)."""
    return _kron_list([sp.eye(3), R_matrix_GLq21(q_sym)])


def R13_GLq21(q_sym: sp.Expr = default_q) -> sp.Matrix:
    """R13 = (P ⊗ I_3) R23 (P ⊗ I_3)  (27×27).

    This follows the paper's definition; P is the super-permutation matrix.
    """
    P = super_permutation_matrix(super_parity_gl21())
    PI = _kron_list([P, sp.eye(3)])
    R23 = R23_GLq21(q_sym)
    return PI * R23 * PI


# ---------------------------------------------------------------------------
# Graded Yang–Baxter verification
# ---------------------------------------------------------------------------

def _is_zero_matrix_symbolic(M: sp.Matrix) -> bool:
    """Check whether all entries are symbolically zero, simplifying each."""
    return all(sp.simplify(x) == 0 for x in M)


def graded_yang_baxter_residual_GLq21(q_sym: sp.Expr = default_q) -> sp.Matrix:
    """Return Y(q) = R12 R13 R23 - R23 R13 R12 (27×27 residual matrix)."""
    R12 = R12_GLq21(q_sym)
    R13 = R13_GLq21(q_sym)
    R23 = R23_GLq21(q_sym)
    return R12 * R13 * R23 - R23 * R13 * R12


def graded_yang_baxter_holds_GLq21(q_sym: sp.Expr = default_q) -> bool:
    """Check the graded Yang–Baxter equation entry by entry."""
    return _is_zero_matrix_symbolic(graded_yang_baxter_residual_GLq21(q_sym))


def summarize_GLq21_ybe(q_sym: sp.Expr = default_q) -> dict:
    """Return a summary of the GL_q(2|1) graded YBE verification."""
    R = R_matrix_GLq21(q_sym)
    nonzero = sum(1 for x in R if sp.simplify(x) != 0)
    return {
        "dimension": 3,
        "R_shape": (9, 9),
        "triple_tensor_shape": (27, 27),
        "nonzero_entries_R": nonzero,
        "residual_is_zero": graded_yang_baxter_holds_GLq21(q_sym),
    }


# ---------------------------------------------------------------------------
# General tensor-power embedding: R_{ij} on V^{⊗n}
# ---------------------------------------------------------------------------

def _adjacent_swap(parity: List[int], n: int, k: int) -> sp.Matrix:
    """Graded swap of factors k and k+1 on V^{⊗n}.

    S_k = I^{⊗k} ⊗ P ⊗ I^{⊗(n-k-2)}.
    """
    d = len(parity)
    P = super_permutation_matrix(parity)
    return _kron_list([_eye_pow(d, k), P, _eye_pow(d, n - k - 2)])


def embed_R_in_tensor_power(
    R: sp.Matrix,
    positions: Tuple[int, int],
    tensor_power: int,
    parity: List[int],
) -> sp.Matrix:
    """Embed the R-matrix into factors (i, j) of V^{⊗n}.

    R must be an even d²×d² operator on V ⊗ V (d = len(parity)).
    Odd operators require additional prefix signs and are not supported.
    ``positions = (i, j)`` uses zero-based indices with i < j. The output
    is the d^n × d^n operator R_{ij}.

    For adjacent factors (j = i+1), use a simple Kronecker embedding:
        I^{⊗i} ⊗ R ⊗ I^{⊗(n-i-2)}.
    For nonadjacent factors (j > i+1), move the second index from i+1 to j
    using successive graded adjacent swaps (super-permutations):
        R_{i,j} = S_{j-1} ... S_{i+1} · R_{i,i+1} · S_{i+1} ... S_{j-1}.
    This conjugation carries the graded signs correctly.
    """
    i, j = positions
    if not (0 <= i < j < tensor_power):
        raise ValueError("positions (i, j) must satisfy 0 <= i < j < tensor_power.")
    d = len(parity)
    n = tensor_power
    if not parity or any(p not in (0, 1) for p in parity):
        raise ValueError("parity must be a nonempty list of zeros and ones.")
    if R.shape != (d*d, d*d):
        raise ValueError("R must have shape (d², d²), where d = len(parity).")
    degrees = [(parity[a] + parity[b]) % 2 for a in range(d) for b in range(d)]
    if any(degrees[a] != degrees[b] and sp.simplify(R[a, b]) != 0
           for a in range(d*d) for b in range(d*d)):
        raise ValueError("R must be an even operator (preserve total parity).")

    # Adjacent embedding R_{i, i+1}
    op = _kron_list([_eye_pow(d, i), R, _eye_pow(d, n - i - 2)])

    # Move the second index from i+1 to j by conjugation.
    for k in range(i + 1, j):
        S_k = _adjacent_swap(parity, n, k)
        op = S_k * op * S_k
    return op


def all_Rij_GLq21(
    tensor_power: int, q_sym: sp.Expr = default_q
) -> Dict[Tuple[int, int], sp.Matrix]:
    """Return all R_{ij} operators (i < j) on V^{⊗n}.

    For example, ``all_Rij_GLq21(3)`` -> {(0,1), (0,2), (1,2)};
    ``all_Rij_GLq21(4)`` -> six operators, each 81×81.
    """
    parity = super_parity_gl21()
    R = R_matrix_GLq21(q_sym)
    return {
        (i, j): embed_R_in_tensor_power(R, (i, j), tensor_power, parity)
        for i, j in combinations(range(tensor_power), 2)
    }


def braid_far_commutativity_residual_GLq21(
    q_sym: sp.Expr = default_q,
) -> sp.Matrix:
    """Far-commutativity residual on V^{⊗4}: R12 R34 - R34 R12.

    Operators on disjoint factors should commute, so this 81×81 residual
    should be zero.
    """
    Rij = all_Rij_GLq21(4, q_sym)
    R12 = Rij[(0, 1)]
    R34 = Rij[(2, 3)]
    return R12 * R34 - R34 * R12


def local_ybe_on_four_tensor_GLq21(
    q_sym: sp.Expr = default_q,
) -> Dict[Tuple[int, int, int], bool]:
    """Check the YBE on every triple of factors in V^{⊗4}.

    Triples (zero-based): (0,1,2), (0,1,3), (0,2,3), (1,2,3). For each,
        R_{ab} R_{ac} R_{bc} = R_{bc} R_{ac} R_{ab}
    return whether the equation holds.
    """
    Rij = all_Rij_GLq21(4, q_sym)
    result: Dict[Tuple[int, int, int], bool] = {}
    for a, b, c in combinations(range(4), 3):
        Rab = Rij[(a, b)]
        Rac = Rij[(a, c)]
        Rbc = Rij[(b, c)]
        residual = Rab * Rac * Rbc - Rbc * Rac * Rab
        result[(a, b, c)] = _is_zero_matrix_symbolic(residual)
    return result
