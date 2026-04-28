"""
quantum_group_sl2.py
====================

QuantumGroupSL2 sınıfı: paketin üst seviye cephesi.

Bu sınıf U_q(sl_2)'yi tek bir nesne olarak kapsar; üreteçleri, bağıntıları
ve temsil oluşturma yöntemlerini bir araya getirir.
"""

from __future__ import annotations

from typing import Dict, Optional

import sympy as sp

from . import generators as gens
from . import relations as rels
from . import representations as reps
from .utils import q as default_q


class QuantumGroupSL2:
    """U_q(sl_2) kuantum grubunu temsil eden cephe sınıfı.

    Parametreler
    ------------
    q : sympy ifadesi, varsayılan modül sembolü `q`
        Deformasyon parametresi. Sayısal değer (örn. sp.Rational(2,1)) veya
        sembolik kalabilir.

    Örnek
    -----
    >>> Uq = QuantumGroupSL2()
    >>> print(Uq)
    U_q(sl_2) kuantum grubu (q sembolik)
    >>> rep = Uq.representation(2)
    >>> Uq.verify(rep)['R4'].holds
    True
    """

    def __init__(self, q: sp.Expr = default_q):
        self.q = q
        self.E = gens.E
        self.F = gens.F
        self.K = gens.K
        self.K_inv = gens.K_inv

    # ------------------------------------------------------------------
    # Üreteç ve bağıntı erişimi
    # ------------------------------------------------------------------

    def generators(self) -> dict:
        """Üreteçleri ad -> sembol sözlüğü olarak döndürür."""
        return {"E": self.E, "F": self.F, "K": self.K, "K_inv": self.K_inv,
                "q": self.q}

    def relations(self):
        """Sembolik tanımlayıcı bağıntıların listesi."""
        return rels.symbolic_relations()

    def print_relations(self) -> None:
        """Bağıntıları okunabilir biçimde yazdırır."""
        print(rels.pretty_print_relations())

    # ------------------------------------------------------------------
    # Temsil inşası ve doğrulama
    # ------------------------------------------------------------------

    def representation(self, n: int) -> reps.Representation:
        """V_n indirgenemez temsilini döndürür (boyut n + 1)."""
        return reps.build_representation(n, q_sym=self.q)

    def verify(
        self,
        rep: Optional[reps.Representation] = None,
        n: Optional[int] = None,
    ) -> Dict[str, rels.RelationCheck]:
        """Bir temsil üzerinde dört bağıntıyı kontrol eder.

        `rep` verilmezse ve `n` verilirse, V_n inşa edilir ve doğrulanır.
        """
        if rep is None:
            if n is None:
                raise ValueError("Bir temsil veya bir n değeri verin.")
            rep = self.representation(n)

        return rels.verify_on_representation(
            E_mat=rep.E,
            F_mat=rep.F,
            K_mat=rep.K,
            Kinv_mat=rep.K_inv,
            q_sym=self.q,
        )

    # ------------------------------------------------------------------
    # Düzgün yazdırma
    # ------------------------------------------------------------------

    def __repr__(self) -> str:  # pragma: no cover
        q_desc = "sembolik" if self.q.free_symbols else f"={self.q}"
        return f"U_q(sl_2) kuantum grubu (q {q_desc})"

    def __str__(self) -> str:  # pragma: no cover
        return self.__repr__()
