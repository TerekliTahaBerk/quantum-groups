"""
generators.py
=============

Symbolic generators for U_q(sl_2).

This module defines the four generators (E, F, K, K^{-1}) and the formal
parameter q as noncommutative SymPy symbols. No relations are imposed at this
level: the structure is a free algebra. `relations.py` supplies the relations.
"""

from __future__ import annotations

import sympy as sp

from .utils import q  # shared q symbol

# Noncommutative symbolic generators. commutative=False prevents SymPy from
# automatically identifying E*F with F*E.
E = sp.Symbol("E", commutative=False)
F = sp.Symbol("F", commutative=False)
K = sp.Symbol("K", commutative=False)
K_inv = sp.Symbol("K^{-1}", commutative=False)


def all_generators() -> dict:
    """Return the generators as a name-to-symbol dictionary."""
    return {"E": E, "F": F, "K": K, "K_inv": K_inv, "q": q}


def commutator(a: sp.Expr, b: sp.Expr) -> sp.Expr:
    """Return the expanded commutator [a, b] = a*b - b*a."""
    return sp.expand(a * b - b * a)
