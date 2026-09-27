"""Internal argument checks shared by the public API (not part of the API)."""

from __future__ import annotations

import operator

import sympy as sp


def as_int(value, name: str, minimum: int | None = None) -> int:
    """Return ``value`` as a Python int, rejecting non-integral input.

    Accepts ``int``, ``sympy.Integer`` and other objects implementing
    ``__index__``; rejects ``bool``, floats and non-integral SymPy numbers.
    """
    if isinstance(value, bool):
        raise TypeError(f"{name} must be an integer, not bool.")
    try:
        result = operator.index(value)
    except TypeError:
        raise TypeError(
            f"{name} must be an integer; got {value!r} of type "
            f"{type(value).__name__}."
        ) from None
    if minimum is not None and result < minimum:
        raise ValueError(f"{name} must be >= {minimum}; got {result}.")
    return result


def check_square(M, name: str) -> tuple[int, int]:
    """Return the shape of ``M`` after checking it is a square SymPy matrix."""
    if not isinstance(M, sp.MatrixBase):
        raise TypeError(f"{name} must be a SymPy Matrix; got {type(M).__name__}.")
    if M.rows != M.cols:
        raise ValueError(f"{name} must be square; got shape {M.shape}.")
    return M.shape
