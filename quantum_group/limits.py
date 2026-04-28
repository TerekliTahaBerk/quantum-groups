"""
limits.py
=========

q parametresinin "üç hayatı": klasik (q → 1), genel q, kristal (q → 0).

Bu modül, V_n temsilinin ve dolayısıyla U_q(sl_2)'nin yapısının q
değerine göre nasıl değiştiğini incelemek için yardımcılar sağlar.

(L1)  Klasik limit q -> 1:
      U_q(sl_2) -> U(sl_2). [n]_q -> n; K -> 1, K-1 -> 0; ancak
      H := (K - 1) / (q - 1) operatörü iyi tanımlı limite sahiptir
      ve klasik h Cartan elemanını verir. q^{n-2k} -> 1 gibi görünür
      ama H özdeğerleri n-2k klasik ağırlıklara karşılık gelir.

(L2)  Genel q:
      Tipik kuantum rejim. Tüm formüller q'da rasyoneldir; temsiller
      klasik temsillerin q-deformasyonudur.

(L3)  Birim kök q^N = 1 (N >= 2):
      [N]_q = 0 olur. E^N, F^N merkez elemanları haline gelir;
      sonlu boyutlu indirgenemezler farklı parametrelenir; "küçük
      kuantum grup" ortaya çıkar. V_n'in matrisleri tekil olabilir.

(L4)  Kristal limit q -> 0:
      Klasik baz seçimleriyle tekil; ancak Kashiwara'nın kristal bazı
      kombinatoryal bir yapı bırakır: tilde_e, tilde_f kısmî
      fonksiyonları. Bu modülde V_n'in matris katsayılarının q -> 0
      "asimptotik mertebesi" hesaplanır.

Bu üç limit, kuantum grupların "klasik / kuantum / kombinatoryal" üç
yüzüne karşılık gelir ve tezin karşılaştırma bölümünün omurgasını
oluşturur.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Dict, List, Tuple

import sympy as sp

from .representations import Representation, build_representation
from .utils import q as default_q


# ---------------------------------------------------------------------------
# (L1) Klasik limit
# ---------------------------------------------------------------------------

def classical_K_to_h(rep: Representation, q_sym: sp.Expr = default_q) -> sp.Matrix:
    """h := lim_{q->1} (K - 1)/(q - 1) operatörünü hesaplar.

    K köşegen olduğu için bu operatör de köşegendir; öğeleri
    lim_{q->1} (q^{n-2k} - 1)/(q - 1) = n - 2k klasik ağırlıklarıdır.
    """
    diag = []
    for k in range(rep.dim):
        entry = (rep.K[k, k] - 1) / (q_sym - 1)
        diag.append(sp.limit(entry, q_sym, 1))
    return sp.diag(*diag)


def classical_commutator_EF(
    rep: Representation,
    q_sym: sp.Expr = default_q,
) -> sp.Matrix:
    """[E,F]'nin q -> 1 limitini doğrudan hesaplar; klasik h'a eşit
    olmalıdır."""
    comm = rep.E * rep.F - rep.F * rep.E
    return sp.Matrix([[sp.limit(comm[i, j], q_sym, 1)
                       for j in range(rep.dim)] for i in range(rep.dim)])


# ---------------------------------------------------------------------------
# (L3) Birim kök q^N = 1
# ---------------------------------------------------------------------------

def root_of_unity_substitution(
    rep: Representation,
    N: int,
    q_sym: sp.Expr = default_q,
) -> Dict[str, sp.Matrix]:
    """q'yu N-inci primitif birim kökle değerlendirir ve E^N matrisini hesaplar.

    Beklenen sonuç: V_n için n < N olduğunda E^N = 0 (nilpotent yapısı
    korunur); n >= N olduğunda farklı davranış sergilenir.

    Burada q = exp(2πi/N) yerine sembolik primitif kök kullanılır
    (sympy.exp(2*sp.pi*sp.I/N))."""
    zeta = sp.exp(2 * sp.pi * sp.I / N)
    sub = lambda M: sp.simplify(M.subs(q_sym, zeta))
    E_N = sub(rep.E**N)
    F_N = sub(rep.F**N)
    K_2N = sub(rep.K**(2 * N))
    return {
        "E^N": E_N,
        "F^N": F_N,
        "K^{2N}": K_2N,
        "E_q=ζ": sub(rep.E),
        "K_q=ζ": sub(rep.K),
    }


# ---------------------------------------------------------------------------
# (L4) Kristal limit q -> 0
# ---------------------------------------------------------------------------

@dataclass
class CrystalAsymptotics:
    """Bir matris girişinin q -> 0 asimptotik davranışı."""
    entry: sp.Expr
    leading_order: sp.Expr   # q -> 0'da en küçük üs (None = sıfır)
    crystal_value: int       # 0 (kaybolan) veya 1 (kalan)


def crystal_asymptotics_F(rep: Representation, q_sym: sp.Expr = default_q) -> sp.Matrix:
    """F matrisinin q -> 0 limitinde "sağ kalan" girdileri.

    F'nin tüm girişleri 1 veya 0 olduğu için F kristal limitinde
    değişmeden kalır.
    """
    return rep.F


def crystal_asymptotics_E_pattern(
    rep: Representation,
    q_sym: sp.Expr = default_q,
) -> sp.Matrix:
    """E matrisinin q -> 0 davranışını gösterir.

    E_{k-1, k} = [k]_q [n-k+1]_q. q -> 0'da bu tek terimde belirleyici
    güç q^{-(k + (n-k+1) - 2)} = q^{-(n-1)} ... gibi öğeler vardır;
    tam tek-terim asimptotik için her girişin başlıca terimini
    döndürürüz.
    """
    n = rep.n
    out = sp.zeros(rep.dim, rep.dim)
    for k in range(1, rep.dim):
        coeff = rep.E[k - 1, k]
        # Başlıca asimptotik (en yüksek negatif kuvveti baskın olur):
        # SymPy.series ile q=0 etrafında açılım
        try:
            ser = sp.series(coeff, q_sym, 0, 2).removeO()
        except Exception:
            ser = coeff
        out[k - 1, k] = sp.simplify(ser)
    return out


def three_limit_summary(n: int) -> str:
    """V_n için üç limitin özet açıklamasını metin olarak döndürür."""
    rep = build_representation(n)
    h = classical_K_to_h(rep)
    h_diag = [h[k, k] for k in range(rep.dim)]
    comm_lim = classical_commutator_EF(rep)
    h_match = sp.simplify(h - comm_lim) == sp.zeros(rep.dim, rep.dim)

    lines = [f"V_{n} (boyut {rep.dim}) için üç limit:"]
    lines.append(f"  (L1) Klasik q->1:")
    lines.append(f"      h-özdeğerleri = {h_diag}")
    lines.append(f"      [E,F] -> h doğrulandı mı? {h_match}")
    lines.append(f"  (L2) Genel q: K-ağırlıkları = {[sp.simplify(w) for w in rep.weights]}")
    lines.append(f"  (L4) Kristal q->0: E katsayıları sıfır olmayan;"
                 " F kristal işlemi olarak hayatta kalır")
    return "\n".join(lines)
