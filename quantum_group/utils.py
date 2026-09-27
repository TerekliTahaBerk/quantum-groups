"""
utils.py
========

q-arithmetic helpers: q-integers, q-factorials and q-binomial coefficients.

Definitions
-----------
q-integer:
    [n]_q = (q^n - q^{-n}) / (q - q^{-1})
          = q^{n-1} + q^{n-3} + ... + q^{-(n-1)}

q-factorial:
    [n]_q! = [n]_q [n-1]_q ... [1]_q,    [0]_q! = 1

q-binomial:
    [n choose k]_q = [n]_q! / ([k]_q! [n-k]_q!)

These functions return SymPy expressions, so q can remain symbolic or be
assigned a numerical value with subs() when needed.
"""

from __future__ import annotations

import sympy as sp

# Standard module-level symbolic q, available to every module.
q = sp.Symbol("q", nonzero=True)


def q_integer(n: int, q_sym: sp.Expr = q) -> sp.Expr:
    """Return the q-integer [n]_q.

    Parameters
    ----------
    n : int
        May be nonnegative or negative; [-n]_q = -[n]_q.
    q_sym : sympy expression
        The q parameter. Defaults to the module symbol `q`.

    Returns
    -------
    sympy expression.

    Example
    -------
    >>> q_integer(3)
    q**2 + 1 + q**(-2)
    """
    if n == 0:
        return sp.Integer(0)
    expr = (q_sym**n - q_sym**(-n)) / (q_sym - q_sym**(-1))
    return sp.simplify(expr)


def q_factorial(n: int, q_sym: sp.Expr = q) -> sp.Expr:
    """Return the q-factorial [n]_q! = [n]_q [n-1]_q ... [1]_q."""
    if n < 0:
        raise ValueError("The q-factorial is defined only for n >= 0.")
    result = sp.Integer(1)
    for k in range(1, n + 1):
        result *= q_integer(k, q_sym)
    return sp.simplify(result)


def q_binomial(n: int, k: int, q_sym: sp.Expr = q) -> sp.Expr:
    """Return the q-binomial coefficient [n choose k]_q."""
    if k < 0 or k > n:
        return sp.Integer(0)
    return sp.simplify(
        q_factorial(n, q_sym) / (q_factorial(k, q_sym) * q_factorial(n - k, q_sym))
    )


def classical_limit(expr: sp.Expr, q_sym: sp.Expr = q) -> sp.Expr:
    """Compute the classical limit q -> 1 (using L'Hôpital's rule).

    This is useful for symbolic checks of limits such as [n]_q -> n.
    """
    return sp.limit(expr, q_sym, 1)
