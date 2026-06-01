"""
representations.py
==================

U_q(sl_2)'nin sonlu boyutlu indirgenemez en yüksek ağırlıklı temsilleri.

Her negatif olmayan tamsayı n için, V_n adlı (n+1)-boyutlu indirgenemez
temsil vardır. Baz {v_0, v_1, ..., v_n} üzerinde üreteçlerin etkisi:

    K . v_k = q^{n - 2k} v_k                                 (köşegen)
    F . v_k = v_{k+1}        (F . v_n = 0)                    (alt-shift)
    E . v_k = [k]_q [n - k + 1]_q v_{k-1}   (E . v_0 = 0)     (üst-shift)

Bu modül, üreteçlerin matrislerini SymPy `Matrix` olarak döndürür.
Boyut sırası: indeks k = 0, 1, ..., n; vektör v_k, k. standart birim
vektörü olarak temsil edilir.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import List

import sympy as sp

from .utils import q, q_integer


@dataclass
class Representation:
    """U_q(sl_2)'nin sonlu boyutlu temsili V_n için kap."""
    n: int                  # en yüksek ağırlık
    dim: int                # boyut = n + 1
    E: sp.Matrix
    F: sp.Matrix
    K: sp.Matrix
    K_inv: sp.Matrix
    weights: List[sp.Expr]  # K-özdeğerleri q^{n-2k}, k=0..n

    def __repr__(self) -> str:  # pragma: no cover
        return f"<U_q(sl_2) temsili V_{self.n}, boyut={self.dim}>"


def _zero_matrix(dim: int) -> sp.Matrix:
    return sp.zeros(dim, dim)


def build_representation(n: int, q_sym: sp.Expr = q) -> Representation:
    """V_n indirgenemez temsilini açık matrisler olarak inşa eder.

    Parametreler
    ------------
    n : int
        En yüksek ağırlık (boyut = n + 1). n >= 0.
    q_sym : sympy ifadesi
        q parametresi. Sembolik bırakılabilir veya sayısal verilebilir.

    Dönüş
    -----
    Representation
        Üreteç matrisleri ve K-ağırlık listesi içeren veri sınıfı.
    """
    if n < 0:
        raise ValueError("En yüksek ağırlık n negatif olamaz.")

    dim = n + 1

    # K köşegen: K . v_k = q^{n-2k} v_k
    weights = [q_sym**(n - 2 * k) for k in range(dim)]
    K_mat = sp.diag(*weights)
    K_inv_mat = sp.diag(*[w**(-1) for w in weights])

    # F alt-shift: F . v_k = v_{k+1}, son k = n hariç.
    F_mat = _zero_matrix(dim)
    for k in range(n):  # k = 0, ..., n-1
        F_mat[k + 1, k] = sp.Integer(1)

    # E üst-shift: E . v_k = [k]_q [n-k+1]_q v_{k-1}, k = 1..n
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
    """v_0: en yüksek ağırlık vektörü; E tarafından sıfırlanır."""
    v = sp.zeros(rep.dim, 1)
    v[0, 0] = sp.Integer(1)
    return v


def lowest_weight_vector(rep: Representation) -> sp.Matrix:
    """v_n: en düşük ağırlık vektörü; F tarafından sıfırlanır."""
    v = sp.zeros(rep.dim, 1)
    v[rep.dim - 1, 0] = sp.Integer(1)
    return v


def weight_of(rep: Representation, k: int) -> sp.Expr:
    """v_k baz vektörünün K-özdeğerini (q^{n-2k}) döndürür."""
    if not (0 <= k < rep.dim):
        raise IndexError(f"k, [0, {rep.dim}) aralığında olmalı.")
    return rep.weights[k]
