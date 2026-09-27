"""
linalg.py
=========

Small exact-matrix helpers shared by the verification modules.

* ``kron`` / ``kron_list`` — Kronecker (tensor) products of SymPy matrices,
  using the standard basis order in which the left factor's index changes
  slowly and the right factor's index changes quickly.
* ``is_zero_matrix`` — the zero-residual test used throughout the package.

These helpers were previously duplicated as private functions in several
modules (``hopf._kron``, ``r_matrix._is_zero``,
``supergroup_gl21._is_zero_matrix_symbolic``). Those names remain as
aliases for backward compatibility.
"""

from __future__ import annotations

from typing import Sequence

import sympy as sp


def kron(A: sp.Matrix, B: sp.Matrix) -> sp.Matrix:
    """Return the Kronecker product A ⊗ B of two SymPy matrices.

    >>> kron(sp.eye(2), sp.Matrix([[0, 1], [1, 0]])).shape
    (4, 4)
    """
    m, n = A.shape
    p, r = B.shape
    out = sp.zeros(m * p, n * r)
    for i in range(m):
        for j in range(n):
            out[i * p:(i + 1) * p, j * r:(j + 1) * r] = A[i, j] * B
    return out


def kron_list(mats: Sequence[sp.Matrix]) -> sp.Matrix:
    """Return the left-to-right Kronecker product of the given matrices."""
    if not mats:
        raise ValueError("kron_list requires at least one matrix.")
    result = mats[0]
    for M in mats[1:]:
        result = kron(result, M)
    return result


def is_zero_matrix(M: sp.Matrix) -> bool:
    """Return whether every entry of ``M`` simplifies to zero.

    ``True`` means each entry was reduced to the exact value 0 by
    ``sympy.simplify``. ``False`` means at least one entry was not; for
    arbitrary SymPy expressions this is not by itself a proof that the
    entry is nonzero, because ``simplify`` is not a decision procedure.
    For the rational functions of ``q`` produced by this package, a
    nonzero result can be confirmed with ``sympy.cancel``.
    """
    return all(sp.simplify(entry) == 0 for entry in M)
