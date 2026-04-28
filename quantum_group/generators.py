"""
generators.py
=============

U_q(sl_2) için sembolik üreteçler.

Bu modülde dört üreteç (E, F, K, K^{-1}) ve formal parametre q
SymPy'nin değişmeyen sembolleri olarak tanımlanır. Bu seviyede HİÇBİR
bağıntı dayatılmaz: yapı serbest cebirdir. Bağıntılar `relations.py`
tarafından sağlanır.
"""

from __future__ import annotations

import sympy as sp

from .utils import q  # ortak q sembolü

# Değişmeyen sembolik üreteçler. commutative=False işaretlemesi,
# SymPy'nin E*F ile F*E'yi otomatik birleştirmesini engeller.
E = sp.Symbol("E", commutative=False)
F = sp.Symbol("F", commutative=False)
K = sp.Symbol("K", commutative=False)
K_inv = sp.Symbol("K^{-1}", commutative=False)


def all_generators() -> dict:
    """Üreteçleri ad -> sembol sözlüğü olarak döndürür."""
    return {"E": E, "F": F, "K": K, "K_inv": K_inv, "q": q}


def commutator(a: sp.Expr, b: sp.Expr) -> sp.Expr:
    """[a, b] = a*b - b*a komütatörü (genişletilmiş)."""
    return sp.expand(a * b - b * a)
