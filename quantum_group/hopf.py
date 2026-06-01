"""
hopf.py
=======

U_q(sl_2)'nin Hopf cebir yapısı: eş-çarpım Δ, eş-birim ε, antipot S.

Tanımlar (üreteçler üzerinde)
----------------------------
    Δ(E) = E ⊗ 1 + K ⊗ E
    Δ(F) = F ⊗ K^{-1} + 1 ⊗ F
    Δ(K) = K ⊗ K
    Δ(K^{-1}) = K^{-1} ⊗ K^{-1}

    ε(E) = 0,  ε(F) = 0,  ε(K) = 1,  ε(K^{-1}) = 1

    S(E) = -K^{-1} E
    S(F) = -F K
    S(K) = K^{-1}
    S(K^{-1}) = K

Hopf aksiyomları (bir temsil V üzerinde matris düzeyinde doğrulanabilir):

    (H1)  Eş-birleşmelilik: (Δ ⊗ id) Δ(X) = (id ⊗ Δ) Δ(X)
    (H2)  Eş-birim: (ε ⊗ id) Δ(X) = X = (id ⊗ ε) Δ(X)
    (H3)  Antipot: μ ∘ (S ⊗ id) ∘ Δ(X) = ε(X) · 1 = μ ∘ (id ⊗ S) ∘ Δ(X)

Burada μ matris çarpımıdır (cebir çarpımı).

Bu modül, bir Representation nesnesi verildiğinde her üreteç için bu üç
aksiyomu Kronecker çarpımı (matris tensör çarpımı) ile somut olarak doğrular.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Dict, Tuple

import sympy as sp

from .representations import Representation
from .utils import q as default_q


# ---------------------------------------------------------------------------
# Soyut Hopf yapı dönüşümleri (matris düzeyinde)
# ---------------------------------------------------------------------------

def coproduct(rep: Representation) -> Dict[str, sp.Matrix]:
    """Δ(X)'in V ⊗ V üzerindeki matris temsilini döndürür.

    Bir temsil V verildiğinde ve V ⊗ V'nin bazı standart Kronecker
    sıralamasıysa (önce V'nin baz indisi yavaş, sonra V'nin baz indisi
    hızlı), Δ(X)'in matrisi formüllerden hesaplanır.
    """
    I = sp.eye(rep.dim)

    return {
        "E": _kron(rep.E, I) + _kron(rep.K, rep.E),
        "F": _kron(rep.F, rep.K_inv) + _kron(I, rep.F),
        "K": _kron(rep.K, rep.K),
        "K_inv": _kron(rep.K_inv, rep.K_inv),
    }


def counit() -> Dict[str, sp.Expr]:
    """ε: U_q(sl_2) -> Q(q). Üreteçler üzerinde sayısal değerler."""
    return {
        "E": sp.Integer(0),
        "F": sp.Integer(0),
        "K": sp.Integer(1),
        "K_inv": sp.Integer(1),
    }


def antipode(rep: Representation) -> Dict[str, sp.Matrix]:
    """S(X)'in V üzerindeki matris temsilini döndürür."""
    return {
        "E": -rep.K_inv * rep.E,
        "F": -rep.F * rep.K,
        "K": rep.K_inv,
        "K_inv": rep.K,
    }


def _kron(A: sp.Matrix, B: sp.Matrix) -> sp.Matrix:
    """SymPy matrisleri için Kronecker (tensör) çarpımı."""
    m, n = A.shape
    p, qd = B.shape
    out = sp.zeros(m * p, n * qd)
    for i in range(m):
        for j in range(n):
            block = A[i, j] * B
            out[i * p:(i + 1) * p, j * qd:(j + 1) * qd] = block
    return out


def kron_list(mats: Tuple[sp.Matrix, ...] | list[sp.Matrix]) -> sp.Matrix:
    """Verilen matrislerin soldan sağa Kronecker çarpımını döndürür."""
    if not mats:
        raise ValueError("kron_list en az bir matris gerektirir.")
    result = mats[0]
    for M in mats[1:]:
        result = _kron(result, M)
    return result


# ---------------------------------------------------------------------------
# Hopf aksiyomlarının doğrulanması
# ---------------------------------------------------------------------------

@dataclass
class HopfAxiomCheck:
    name: str
    holds: bool
    detail: str = ""

    def __repr__(self) -> str:  # pragma: no cover
        return f"<{self.name}: {'OK' if self.holds else 'BAŞARISIZ'}>"


def verify_counit(rep: Representation) -> Dict[str, HopfAxiomCheck]:
    """(ε ⊗ id) Δ(X) = X = (id ⊗ ε) Δ(X) eşitliğini doğrular.

    ε bir skalardır; ε ⊗ id bir tensörü kontrakt eder: V ⊗ V -> V.
    Matris düzeyinde, V'nin n-boyutlu olduğunu varsayalım. Δ(X) bir
    n²×n² matrisidir; (ε ⊗ id) onu nasıl indirgeyeceğini bilmemiz için
    Δ(X)'i Σ X_(1) ⊗ X_(2) biçiminde bilmek gerekir, ama biz sadece
    matris formuna sahibiz. Doğrudan inşa: her üreteç için Δ(X) = Σ A_i ⊗ B_i
    kapatımının formülden bilinen yapısını kullanırız.
    """
    eps = counit()
    n = rep.dim
    I = sp.eye(n)
    results: Dict[str, HopfAxiomCheck] = {}

    # Her üreteç için, Δ(X) = Σ A_i ⊗ B_i biçiminde elimizde:
    #   E:  [(E,I), (K,E)]
    #   F:  [(F,K_inv), (I,F)]
    #   K:  [(K,K)]
    #   K_inv: [(K_inv,K_inv)]
    decompositions: Dict[str, list] = {
        "E": [(rep.E, I), (rep.K, rep.E)],
        "F": [(rep.F, rep.K_inv), (I, rep.F)],
        "K": [(rep.K, rep.K)],
        "K_inv": [(rep.K_inv, rep.K_inv)],
    }
    rep_mats = {"E": rep.E, "F": rep.F, "K": rep.K, "K_inv": rep.K_inv}

    for X, terms in decompositions.items():
        # (ε ⊗ id) Δ(X) = Σ ε(A_i) · B_i  (A_i'nin "skalarlaşması" değil;
        # ε bir homomorfizm, A_i bir matristir. Doğru anlam: ε aslında
        # cebir üzerinden tanımlıdır; matris temsilinde "ε(A_i) · B_i"
        # ifadesi A_i'yi ε'nun cebirsel halefiyle değiştirmek demektir.)
        # Bu yüzden burada decompositions'taki A_i'ler ζ-üreteçlere
        # "etiketli" olarak verilir; aşağıda etiketler üzerinden ε uygularız.
        pass  # Tam denetim _verify_counit_via_labels ile

    return _verify_counit_via_labels(rep)


def _verify_counit_via_labels(rep: Representation) -> Dict[str, HopfAxiomCheck]:
    """Eş-birim aksiyomunu, Δ'nın etiketli ayrışımı üzerinden doğrular."""
    n = rep.dim
    I = sp.eye(n)
    eps = counit()

    # Etiketli ayrışım: her üreteç X için Δ(X) = Σ X1_i ⊗ X2_i
    # Burada X1_i, X2_i {E, F, K, K_inv, 1} sembollerinden biri olabilir.
    # ε sıfırlanan üreteçleri sıfırlar (E, F), K ve K_inv için 1 verir.
    decompositions = {
        "E": [("E", "1"), ("K", "E")],
        "F": [("F", "K_inv"), ("1", "F")],
        "K": [("K", "K")],
        "K_inv": [("K_inv", "K_inv")],
    }
    label_to_mat = {"E": rep.E, "F": rep.F, "K": rep.K,
                    "K_inv": rep.K_inv, "1": I}
    label_to_eps = {"E": 0, "F": 0, "K": 1, "K_inv": 1, "1": 1}
    target = {"E": rep.E, "F": rep.F, "K": rep.K, "K_inv": rep.K_inv}

    results: Dict[str, HopfAxiomCheck] = {}
    for X, terms in decompositions.items():
        # Sol uygulama: (ε ⊗ id) Δ(X) = Σ ε(X1_i) · X2_i
        left = sum((sp.Integer(label_to_eps[a]) * label_to_mat[b]
                    for (a, b) in terms), sp.zeros(n, n))
        # Sağ uygulama: (id ⊗ ε) Δ(X) = Σ X1_i · ε(X2_i)
        right = sum((label_to_mat[a] * sp.Integer(label_to_eps[b])
                     for (a, b) in terms), sp.zeros(n, n))
        ok_left = sp.simplify(left - target[X]) == sp.zeros(n, n)
        ok_right = sp.simplify(right - target[X]) == sp.zeros(n, n)
        results[X] = HopfAxiomCheck(
            name=f"Eş-birim ({X})",
            holds=bool(ok_left and ok_right),
        )
    return results


def verify_antipode(rep: Representation) -> Dict[str, HopfAxiomCheck]:
    """μ ∘ (S ⊗ id) ∘ Δ(X) = ε(X) · I = μ ∘ (id ⊗ S) ∘ Δ(X) eşitliğini
    doğrular. Sonuç V üzerinde n×n matris denklemleridir."""
    n = rep.dim
    I = sp.eye(n)
    eps = counit()
    S = antipode(rep)
    label_to_mat = {"E": rep.E, "F": rep.F, "K": rep.K,
                    "K_inv": rep.K_inv, "1": I}
    label_to_S = {"E": S["E"], "F": S["F"], "K": S["K"],
                  "K_inv": S["K_inv"], "1": I}

    decompositions = {
        "E": [("E", "1"), ("K", "E")],
        "F": [("F", "K_inv"), ("1", "F")],
        "K": [("K", "K")],
        "K_inv": [("K_inv", "K_inv")],
    }

    results: Dict[str, HopfAxiomCheck] = {}
    for X, terms in decompositions.items():
        # μ ∘ (S ⊗ id) ∘ Δ(X) = Σ S(X1_i) · X2_i
        left = sum((label_to_S[a] * label_to_mat[b]
                    for (a, b) in terms), sp.zeros(n, n))
        # μ ∘ (id ⊗ S) ∘ Δ(X) = Σ X1_i · S(X2_i)
        right = sum((label_to_mat[a] * label_to_S[b]
                     for (a, b) in terms), sp.zeros(n, n))
        target = sp.Integer(eps[X]) * I
        ok_left = sp.simplify(left - target) == sp.zeros(n, n)
        ok_right = sp.simplify(right - target) == sp.zeros(n, n)
        results[X] = HopfAxiomCheck(
            name=f"Antipot ({X})",
            holds=bool(ok_left and ok_right),
        )
    return results


def verify_coassociativity(rep: Representation) -> Dict[str, HopfAxiomCheck]:
    """(Δ ⊗ id) Δ(X) = (id ⊗ Δ) Δ(X) eşitliğini V ⊗ V ⊗ V üzerinde doğrular.

    Δ tanımıyla tutarlı olduğundan bu otomatik olarak sağlanmalıdır;
    yine de sayısal/matris düzeyinde bir kanıt sağlar.
    """
    n = rep.dim
    I = sp.eye(n)
    Delta = coproduct(rep)

    # (Δ ⊗ id) Δ(X): n^2 x n^2 matrisi olan Δ(X)'in sol kanadına Δ uygulanır.
    # Bu, Δ(X)'i Σ A_i ⊗ B_i biçiminde yazmamızı gerektirir; etiketli
    # ayrışımı kullanırız ve her A_i'nin Δ'sını alırız.

    decompositions = {
        "E": [("E", "1"), ("K", "E")],
        "F": [("F", "K_inv"), ("1", "F")],
        "K": [("K", "K")],
        "K_inv": [("K_inv", "K_inv")],
    }
    label_to_mat = {"E": rep.E, "F": rep.F, "K": rep.K,
                    "K_inv": rep.K_inv, "1": I}
    label_to_Delta = {
        "E": Delta["E"],
        "F": Delta["F"],
        "K": Delta["K"],
        "K_inv": Delta["K_inv"],
        "1": _kron(I, I),
    }

    results: Dict[str, HopfAxiomCheck] = {}
    for X, terms in decompositions.items():
        # Sol: Σ Δ(A_i) ⊗ B_i  (n^3 x n^3)
        left = sum((_kron(label_to_Delta[a], label_to_mat[b])
                    for (a, b) in terms), sp.zeros(n**3, n**3))
        # Sağ: Σ A_i ⊗ Δ(B_i)
        right = sum((_kron(label_to_mat[a], label_to_Delta[b])
                     for (a, b) in terms), sp.zeros(n**3, n**3))
        diff = sp.simplify(left - right)
        ok = diff == sp.zeros(n**3, n**3)
        results[X] = HopfAxiomCheck(
            name=f"Eş-birleşmelilik ({X})",
            holds=bool(ok),
        )
    return results


def verify_all_hopf_axioms(rep: Representation) -> Dict[str, Dict[str, HopfAxiomCheck]]:
    """Tüm Hopf aksiyomlarını V üzerinde doğrular ve gruplanmış sonuç döndürür."""
    return {
        "coassociativity": verify_coassociativity(rep),
        "counit": _verify_counit_via_labels(rep),
        "antipode": verify_antipode(rep),
    }
