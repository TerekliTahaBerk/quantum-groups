"""
utils.py
========

q-aritmetik yardımcıları: q-tamsayı, q-faktöriyel ve q-binom katsayıları.

Tanımlar
--------
q-tamsayı:
    [n]_q = (q^n - q^{-n}) / (q - q^{-1})
          = q^{n-1} + q^{n-3} + ... + q^{-(n-1)}

q-faktöriyel:
    [n]_q! = [n]_q [n-1]_q ... [1]_q,    [0]_q! = 1

q-binom:
    [n choose k]_q = [n]_q! / ([k]_q! [n-k]_q!)

Bu fonksiyonlar SymPy ifadeleri döndürür; böylece sembolik q ile çalışılabilir
ve gerektiğinde sayısal q için subs() çağrılabilir.
"""

from __future__ import annotations

import sympy as sp

# Modül düzeyinde standart sembolik q. Tüm modüller içe aktarabilir.
q = sp.Symbol("q", nonzero=True)


def q_integer(n: int, q_sym: sp.Expr = q) -> sp.Expr:
    """q-tamsayı [n]_q'yi döndürür.

    Parametreler
    ------------
    n : int
        İşaretsiz tamsayı veya negatif olabilir; [-n]_q = -[n]_q.
    q_sym : sympy ifadesi
        q parametresi. Varsayılan olarak modül sembolü `q`.

    Dönüş
    -----
    sympy ifadesi.

    Örnek
    -----
    >>> q_integer(3)
    q**2 + 1 + q**(-2)  # eşdeğer biçimde sadeleştirilebilir
    """
    if n == 0:
        return sp.Integer(0)
    expr = (q_sym**n - q_sym**(-n)) / (q_sym - q_sym**(-1))
    return sp.simplify(expr)


def q_factorial(n: int, q_sym: sp.Expr = q) -> sp.Expr:
    """q-faktöriyel [n]_q! = [n]_q [n-1]_q ... [1]_q'yi döndürür."""
    if n < 0:
        raise ValueError("q-faktöriyel yalnızca n >= 0 için tanımlıdır.")
    result = sp.Integer(1)
    for k in range(1, n + 1):
        result *= q_integer(k, q_sym)
    return sp.simplify(result)


def q_binomial(n: int, k: int, q_sym: sp.Expr = q) -> sp.Expr:
    """q-binom katsayısı [n choose k]_q'yi döndürür."""
    if k < 0 or k > n:
        return sp.Integer(0)
    return sp.simplify(
        q_factorial(n, q_sym) / (q_factorial(k, q_sym) * q_factorial(n - k, q_sym))
    )


def classical_limit(expr: sp.Expr, q_sym: sp.Expr = q) -> sp.Expr:
    """q -> 1 klasik limitini hesaplar (L'Hôpital ile).

    Bu, [n]_q -> n gibi limitlerin sembolik doğrulaması için kullanışlıdır.
    """
    return sp.limit(expr, q_sym, 1)
