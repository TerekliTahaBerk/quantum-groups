"""
representations.py
==================

Finite-dimensional irreducible highest-weight representations of U_q(sl_2).

For every nonnegative integer n, there is an (n+1)-dimensional irreducible
representation V_n. On the basis {v_0, v_1, ..., v_n}, the generators act as:

    K . v_k = q^{n - 2k} v_k                                 (diagonal)
    F . v_k = v_{k+1}        (F . v_n = 0)                    (lower shift)
    E . v_k = [k]_q [n - k + 1]_q v_{k-1}   (E . v_0 = 0)     (upper shift)

This module returns the generator matrices as SymPy `Matrix` objects.
Basis order: k = 0, 1, ..., n; v_k is represented by the kth standard basis vector.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import List

import sympy as sp

from .utils import q, q_integer


@dataclass
class Representation:
    """Container for the finite-dimensional U_q(sl_2) representation V_n."""
    n: int                  # highest weight
    dim: int                # dimension = n + 1
    E: sp.Matrix
    F: sp.Matrix
    K: sp.Matrix
    K_inv: sp.Matrix
    weights: List[sp.Expr]  # K-eigenvalues q^{n-2k}, k=0..n

    def __repr__(self) -> str:  # pragma: no cover
        return f"<U_q(sl_2) representation V_{self.n}, dimension={self.dim}>"


def _zero_matrix(dim: int) -> sp.Matrix:
    return sp.zeros(dim, dim)


def build_representation(n: int, q_sym: sp.Expr = q) -> Representation:
    """Construct the irreducible representation V_n as explicit matrices.

    Parameters
    ----------
    n : int
        Highest weight (dimension = n + 1). n >= 0.
    q_sym : sympy expression
        The q parameter, symbolic or numerical.

    Returns
    -------
    Representation
        Data class containing generator matrices and a list of K-weights.
    """
    if n < 0:
        raise ValueError("The highest weight n must be nonnegative.")

    dim = n + 1

    # K is diagonal: K . v_k = q^{n-2k} v_k
    weights = [q_sym**(n - 2 * k) for k in range(dim)]
    K_mat = sp.diag(*weights)
    K_inv_mat = sp.diag(*[w**(-1) for w in weights])

    # F is a lower shift: F . v_k = v_{k+1}, except at k = n.
    F_mat = _zero_matrix(dim)
    for k in range(n):  # k = 0, ..., n-1
        F_mat[k + 1, k] = sp.Integer(1)

    # E is an upper shift: E . v_k = [k]_q [n-k+1]_q v_{k-1}, k = 1..n
    E_mat = _zero_matrix(dim)
    for k in range(1, dim):  # k = 1, ..., n
        coeff = q_integer(k, q_sym) * q_integer(n - k + 1, q_sym)
        E_mat[k - 1, k] = sp.simplify(coeff)

    return Representation(
        n=n,
        dim=dim,
        E=sp.simplify(E_mat),
        F=F_mat,
        K=sp.simplify(K_mat),
        K_inv=sp.simplify(K_inv_mat),
        weights=weights,
    )


def build_representation_core(n: int, q_sym: sp.Expr = q) -> Representation:
    """Manuscript-compatible wrapper for ``build_representation``.

    The implementation returns the repository's ``Representation`` data class
    rather than a bare tuple, so downstream code can access ``E``, ``F``,
    ``K`` and ``K_inv`` by name.
    """
    return build_representation(n, q_sym=q_sym)


def highest_weight_vector(rep: Representation) -> sp.Matrix:
    """Return v_0, the highest-weight vector annihilated by E."""
    v = sp.zeros(rep.dim, 1)
    v[0, 0] = sp.Integer(1)
    return v


def lowest_weight_vector(rep: Representation) -> sp.Matrix:
    """Return v_n, the lowest-weight vector annihilated by F."""
    v = sp.zeros(rep.dim, 1)
    v[rep.dim - 1, 0] = sp.Integer(1)
    return v


def weight_of(rep: Representation, k: int) -> sp.Expr:
    """Return the K-eigenvalue (q^{n-2k}) of basis vector v_k."""
    if not (0 <= k < rep.dim):
        raise IndexError(f"k must be in [0, {rep.dim}).")
    return rep.weights[k]
