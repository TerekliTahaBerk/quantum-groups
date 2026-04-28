"""
tensor.py
=========

U_q(sl_2) temsillerinin tensör çarpımı ve Clebsch–Gordan ayrışımı.

Tensör çarpım yapısı eş-çarpım Δ aracılığıyla taşınır:

    X . (v ⊗ w) = Δ(X) . (v ⊗ w)

Bu yüzden V_m ⊗ V_n üzerinde üreteçlerin etkisi:

    E . (v ⊗ w) = E v ⊗ w + K v ⊗ E w
    F . (v ⊗ w) = F v ⊗ K^{-1} w + v ⊗ F w
    K . (v ⊗ w) = K v ⊗ K w

Clebsch–Gordan ayrışımı (klasikle aynı yapı):

    V_m ⊗ V_n  ≅  V_{m+n}  ⊕  V_{m+n-2}  ⊕  ...  ⊕  V_{|m-n|}

Bu modül V_m ⊗ V_n üzerinde etki matrislerini inşa eder ve her doğrudan
toplam parçası için en yüksek ağırlık vektörünü açıkça hesaplar.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import List, Tuple

import sympy as sp

from .representations import Representation, build_representation
from .hopf import _kron
from .utils import q as default_q


@dataclass
class TensorRepresentation:
    """V_m ⊗ V_n için kap."""
    m: int
    n: int
    dim: int
    E: sp.Matrix
    F: sp.Matrix
    K: sp.Matrix
    K_inv: sp.Matrix


def tensor_product(repA: Representation, repB: Representation) -> TensorRepresentation:
    """Δ aracılığıyla V_m ⊗ V_n üzerinde üreteçlerin matris etkisini inşa eder.

    Baz sıralaması: e_{i,j} = v_i^A ⊗ v_j^B, sözlük sıralı (önce i, sonra j).
    """
    nA, nB = repA.dim, repB.dim
    IA = sp.eye(nA)
    IB = sp.eye(nB)

    E = _kron(repA.E, IB) + _kron(repA.K, repB.E)
    F = _kron(repA.F, repB.K_inv) + _kron(IA, repB.F)
    K = _kron(repA.K, repB.K)
    K_inv = _kron(repA.K_inv, repB.K_inv)

    return TensorRepresentation(
        m=repA.n, n=repB.n, dim=nA * nB,
        E=sp.simplify(E), F=sp.simplify(F),
        K=sp.simplify(K), K_inv=sp.simplify(K_inv),
    )


# ---------------------------------------------------------------------------
# Clebsch–Gordan ayrışımı
# ---------------------------------------------------------------------------

def cg_summands(m: int, n: int) -> List[int]:
    """V_m ⊗ V_n = ⊕ V_k için ortaya çıkan k değerlerini listeler.

    k = |m-n|, |m-n|+2, ..., m+n  (hepsi m+n ile aynı pariteye sahip).
    """
    lo = abs(m - n)
    hi = m + n
    return list(range(lo, hi + 1, 2))


def find_highest_weight_vectors(
    tensor_rep: TensorRepresentation,
    q_sym: sp.Expr = default_q,
) -> List[Tuple[int, sp.Matrix]]:
    """V_m ⊗ V_n içindeki tüm en yüksek ağırlık vektörlerini bulur.

    Bir vektör v "en yüksek ağırlık k vektörüdür" anlamı:
        E . v = 0     ve     K . v = q^k v.

    Dönüş: [(k, v)] çiftleri listesi; k azalan sırada.

    Algoritma:
        Her aday k = |m-n|, |m-n|+2, ..., m+n için K-özdeğeri q^k olan
        ağırlık altuzayını seçer (köşegen olduğu için indis seçimiyle),
        bu altuzaydaki E'nin çekirdeğini hesaplar.
    """
    m, n = tensor_rep.m, tensor_rep.n
    summands = cg_summands(m, n)

    # K'nin köşegen olduğu varsayılır; her bazı vektörü için K-üssünü hesapla.
    K_diag_exponents = []
    for i in range(m + 1):
        for j in range(n + 1):
            # v_i^A için K-üssü m - 2i, v_j^B için n - 2j
            K_diag_exponents.append((m - 2 * i) + (n - 2 * j))

    results: List[Tuple[int, sp.Matrix]] = []
    for k in reversed(summands):
        # Ağırlık k altuzayının indislerini topla
        idx = [t for t, w in enumerate(K_diag_exponents) if w == k]
        if not idx:
            continue
        # E matrisinin bu indis altuzayına kısıtlamasını al ve çekirdeğini bul.
        E_sub = sp.Matrix([[tensor_rep.E[r, c] for c in idx] for r in idx])
        # Aslında E ağırlık altuzayını bir altta atan bir operatördür;
        # tam çekirdek için E'nin tüm sütunlarına bakmak gerekir.
        # Daha doğrusu: E'nin idx üzerindeki sütunlarına bakıp tüm domain
        # üzerinde sıfır olanları seçeriz.
        E_cols = sp.Matrix([[tensor_rep.E[r, c] for c in idx]
                            for r in range(tensor_rep.dim)])
        null = E_cols.nullspace()
        # null alanındaki her vektörü tam V_m ⊗ V_n bazına geri yerleştir.
        for vec in null:
            full = sp.zeros(tensor_rep.dim, 1)
            for local_i, global_i in enumerate(idx):
                full[global_i, 0] = vec[local_i, 0]
            full = sp.simplify(full)
            results.append((k, full))

    return results


def cg_decomposition_summary(m: int, n: int) -> str:
    """V_m ⊗ V_n ayrışımını okunabilir biçimde döndürür."""
    summands = cg_summands(m, n)
    parts = " ⊕ ".join(f"V_{k}" for k in reversed(summands))
    total = sum(k + 1 for k in summands)
    return f"V_{m} ⊗ V_{n} ≅ {parts}    (boyut: {(m+1)*(n+1)} = {total})"
