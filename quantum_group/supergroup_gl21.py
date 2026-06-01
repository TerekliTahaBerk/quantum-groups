"""
supergroup_gl21.py
==================

Çelik & Çelik (Reports on Mathematical Physics, **88** (2021), 259) makalesinde
tanıtılan yeni kuantum süpergrubu **GL_q(2|1)** için graded (Z_2-dereceli)
Yang–Baxter denkleminin bilgisayar destekli sembolik doğrulaması.

Matematiksel arka plan
----------------------
GL_q(2|1), V = C^{2|1} süper vektör uzayı üzerinde tanımlıdır. Baz vektörleri
e_1, e_2, e_3 olup pariteleri (Z_2-dereceleri):

    p(e_1) = 0,  p(e_2) = 0,  p(e_3) = 1   ->   parity = [0, 0, 1]

ilk iki vektör **even** (çift), üçüncüsü **odd** (tek)tir.

Makalede (s. 261) verilen R-matrisi, V ⊗ V (9 boyutlu) üzerinde etki eden
9×9 bir matristir. Baz sıralaması (internal 0-index ile):

    e_1⊗e_1, e_1⊗e_2, e_1⊗e_3,
    e_2⊗e_1, e_2⊗e_2, e_2⊗e_3,
    e_3⊗e_1, e_3⊗e_2, e_3⊗e_3

R-matrisi graded Yang–Baxter denklemini sağlar:

    R12 R13 R23 = R23 R13 R12          (V ⊗ V ⊗ V üzerinde, 27×27)

burada makalenin tanımına göre

    R12 = R ⊗ I_3
    R23 = I_3 ⊗ R
    R13 = (P ⊗ I_3) R23 (P ⊗ I_3)

ve P, süper permütasyon matrisidir:

    P(e_i ⊗ e_j) = (-1)^{p(i) p(j)} e_j ⊗ e_i.

parity = [0, 0, 1] olduğundan P, klasik takas (swap) matrisinden yalnızca
odd-odd bileşeninde, yani P^{33}_{33} = -1 işaretinde ayrılır.

Bu modülün metodolojik katkısı, elle yapıldığında çok uzun ve hataya açık olan
bu graded Yang–Baxter hesabını, Python/SymPy üzerinde modellenebilir, test
edilebilir ve tekrar üretilebilir bir sembolik doğrulama prosedürüne
dönüştürmektir.
"""

from __future__ import annotations

from itertools import combinations
from typing import Dict, List, Tuple

import sympy as sp

from .hopf import kron_list
from .utils import q as default_q


# ---------------------------------------------------------------------------
# Temel veri: parite, baz ve R-matrisi
# ---------------------------------------------------------------------------

def super_parity_gl21() -> List[int]:
    """GL_q(2|1) baz vektörlerinin Z_2-paritelerini döndürür.

    e_1, e_2 even (0); e_3 odd (1). Yani [0, 0, 1].
    """
    return [0, 0, 1]


def basis_pairs_gl21() -> List[Tuple[int, int]]:
    """V ⊗ V bazının (i, j) çiftleri, **0-index** ile.

    Sıralama satır-büyük (row-major):
    (0,0), (0,1), (0,2), (1,0), (1,1), (1,2), (2,0), (2,1), (2,2).
    Burada index k = 3*i + j, makaledeki e_{i+1} ⊗ e_{j+1} bazına karşılık gelir.
    """
    return [(i, j) for i in range(3) for j in range(3)]


def R_matrix_GLq21(q_sym: sp.Expr = default_q) -> sp.Matrix:
    """Makalede (s. 261) verilen GL_q(2|1) R-matrisi (9×9).

    Baz sıralaması ``basis_pairs_gl21()`` ile uyumludur.
    """
    q = q_sym
    return sp.Matrix([
        [1, 0,      0,  0,        0, 0,      0,        0,      0],
        [0, q**2,   0,  1 - q**2, 0, 0,      0,        0,      0],
        [0, 0,      q,  0,        0, 0,      1 - q**2, 0,      0],
        [0, 0,      0,  1,        0, 0,      0,        0,      0],
        [0, 0,      0,  0,        1, 0,      0,        0,      0],
        [0, 0,      0,  0,        0, q,      0,        1 - q**2, 0],
        [0, 0,      0,  0,        0, 0,      q,        0,      0],
        [0, 0,      0,  0,        0, 0,      0,        q,      0],
        [0, 0,      0,  0,        0, 0,      0,        0,      q**2],
    ])


# ---------------------------------------------------------------------------
# Süper permütasyon ve Kronecker yardımcıları
# ---------------------------------------------------------------------------

def super_permutation_matrix(parity: List[int]) -> sp.Matrix:
    """V ⊗ V üzerinde graded takas (super permutation) matrisi.

        P(e_i ⊗ e_j) = (-1)^{p(i) p(j)} e_j ⊗ e_i.

    Genel boyutta çalışır: d = len(parity) için sonuç (d², d²) boyutludur.
    parity = [0, 0, 1] için bu, klasik swap'ten yalnızca P[8, 8] = -1
    (yani e_3⊗e_3 bileşeni) ile ayrılır.
    """
    d = len(parity)
    P = sp.zeros(d * d, d * d)
    for i in range(d):
        for j in range(d):
            sign = -1 if (parity[i] and parity[j]) else 1
            # giriş: e_i ⊗ e_j  (sütun index i*d + j)
            # çıkış: e_j ⊗ e_i  (satır  index j*d + i)
            P[j * d + i, i * d + j] = sign
    return P


def _kron_list(mats: List[sp.Matrix]) -> sp.Matrix:
    """Geriye uyumlu private ad; public kullanım için ``kron_list``."""
    return kron_list(mats)


def _eye_pow(d: int, n: int) -> sp.Matrix:
    """I_d^{⊗n}; n = 0 için 1×1 birim (skaler nötr eleman)."""
    if n <= 0:
        return sp.eye(1)
    return sp.eye(d ** n)


# ---------------------------------------------------------------------------
# Üç faktörlü yerleşimler: R12, R23, R13  (V ⊗ V ⊗ V, 27×27)
# ---------------------------------------------------------------------------

def R12_GLq21(q_sym: sp.Expr = default_q) -> sp.Matrix:
    """R12 = R ⊗ I_3  (27×27)."""
    return _kron_list([R_matrix_GLq21(q_sym), sp.eye(3)])


def R23_GLq21(q_sym: sp.Expr = default_q) -> sp.Matrix:
    """R23 = I_3 ⊗ R  (27×27)."""
    return _kron_list([sp.eye(3), R_matrix_GLq21(q_sym)])


def R13_GLq21(q_sym: sp.Expr = default_q) -> sp.Matrix:
    """R13 = (P ⊗ I_3) R23 (P ⊗ I_3)  (27×27).

    Makalenin tanımıyla birebir; P süper permütasyon matrisidir.
    """
    P = super_permutation_matrix(super_parity_gl21())
    PI = _kron_list([P, sp.eye(3)])
    R23 = R23_GLq21(q_sym)
    return PI * R23 * PI


# ---------------------------------------------------------------------------
# Graded Yang–Baxter doğrulaması
# ---------------------------------------------------------------------------

def _is_zero_matrix_symbolic(M: sp.Matrix) -> bool:
    """Tüm girdileri sembolik olarak sıfır mı? (entry bazında simplify)."""
    return all(sp.simplify(x) == 0 for x in M)


def graded_yang_baxter_residual_GLq21(q_sym: sp.Expr = default_q) -> sp.Matrix:
    """Y(q) = R12 R13 R23 - R23 R13 R12  (27×27 kalıntı matrisi)."""
    R12 = R12_GLq21(q_sym)
    R13 = R13_GLq21(q_sym)
    R23 = R23_GLq21(q_sym)
    return R12 * R13 * R23 - R23 * R13 * R12


def graded_yang_baxter_holds_GLq21(q_sym: sp.Expr = default_q) -> bool:
    """Graded Yang–Baxter eşitliği tüm girdiler düzeyinde sağlanıyor mu?"""
    return _is_zero_matrix_symbolic(graded_yang_baxter_residual_GLq21(q_sym))


def summarize_GLq21_ybe(q_sym: sp.Expr = default_q) -> dict:
    """GL_q(2|1) graded YBE doğrulamasının özetini döndürür."""
    R = R_matrix_GLq21(q_sym)
    nonzero = sum(1 for x in R if sp.simplify(x) != 0)
    return {
        "dimension": 3,
        "R_shape": (9, 9),
        "triple_tensor_shape": (27, 27),
        "nonzero_entries_R": nonzero,
        "residual_is_zero": graded_yang_baxter_holds_GLq21(q_sym),
    }


# ---------------------------------------------------------------------------
# Genel çoklu tensör yerleşimi: V^{⊗n} üzerinde R_{ij}
# ---------------------------------------------------------------------------

def _adjacent_swap(parity: List[int], n: int, k: int) -> sp.Matrix:
    """V^{⊗n} üzerinde k ve k+1 faktörlerini değiş-tokuş eden graded swap.

    S_k = I^{⊗k} ⊗ P ⊗ I^{⊗(n-k-2)}.
    """
    d = len(parity)
    P = super_permutation_matrix(parity)
    return _kron_list([_eye_pow(d, k), P, _eye_pow(d, n - k - 2)])


def embed_R_in_tensor_power(
    R: sp.Matrix,
    positions: Tuple[int, int],
    tensor_power: int,
    parity: List[int],
) -> sp.Matrix:
    """R-matrisini V^{⊗n} uzayında (i, j) faktörlerine yerleştirir.

    R, V ⊗ V üzerinde etki eden d²×d² bir matristir (d = len(parity)).
    ``positions = (i, j)`` 0-index ve i < j kabul edilir. Çıktı,
    d^n × d^n boyutlu R_{ij} operatörüdür.

    Komşu faktörler (j = i+1) için sonuç basit bir Kronecker yerleşimidir:
        I^{⊗i} ⊗ R ⊗ I^{⊗(n-i-2)}.
    Komşu olmayan yerleşimlerde (j > i+1) ikinci index, art arda gelen
    graded adjacent-swap operatörleriyle (süper permütasyon) i+1'den j'ye
    taşınır:
        R_{i,j} = S_{j-1} ... S_{i+1} · R_{i,i+1} · S_{i+1} ... S_{j-1}.
    Bu konjugasyon, graded işaretlerin doğru taşınmasını garanti eder.
    """
    i, j = positions
    if not (0 <= i < j < tensor_power):
        raise ValueError("positions (i, j) için 0 <= i < j < tensor_power olmalı.")
    d = len(parity)
    n = tensor_power

    # Komşu yerleşim R_{i, i+1}
    op = _kron_list([_eye_pow(d, i), R, _eye_pow(d, n - i - 2)])

    # İkinci indexi i+1'den j'ye konjugasyonla taşı
    for k in range(i + 1, j):
        S_k = _adjacent_swap(parity, n, k)
        op = S_k * op * S_k
    return op


def all_Rij_GLq21(
    tensor_power: int, q_sym: sp.Expr = default_q
) -> Dict[Tuple[int, int], sp.Matrix]:
    """V^{⊗n} üzerindeki tüm R_{ij} operatörlerini (i < j) döndürür.

    Örn. ``all_Rij_GLq21(3)`` -> {(0,1), (0,2), (1,2)};
    ``all_Rij_GLq21(4)`` -> altı operatör, her biri 81×81.
    """
    parity = super_parity_gl21()
    R = R_matrix_GLq21(q_sym)
    return {
        (i, j): embed_R_in_tensor_power(R, (i, j), tensor_power, parity)
        for i, j in combinations(range(tensor_power), 2)
    }


def braid_far_commutativity_residual_GLq21(
    q_sym: sp.Expr = default_q,
) -> sp.Matrix:
    """V^{⊗4} üzerinde uzak komütativite kalıntısı: R12 R34 - R34 R12.

    Ayrık (örtüşmeyen) faktörlere etki eden operatörler komüte etmelidir;
    bu kalıntı sıfır olmalıdır (81×81).
    """
    Rij = all_Rij_GLq21(4, q_sym)
    R12 = Rij[(0, 1)]
    R34 = Rij[(2, 3)]
    return R12 * R34 - R34 * R12


def local_ybe_on_four_tensor_GLq21(
    q_sym: sp.Expr = default_q,
) -> Dict[Tuple[int, int, int], bool]:
    """V^{⊗4} içindeki tüm üçlü alt-blok YBE kontrolleri.

    Üçlüler (0-index): (0,1,2), (0,1,3), (0,2,3), (1,2,3). Her biri için
        R_{ab} R_{ac} R_{bc} = R_{bc} R_{ac} R_{ab}
    eşitliğinin sağlanıp sağlanmadığını döndürür.
    """
    Rij = all_Rij_GLq21(4, q_sym)
    result: Dict[Tuple[int, int, int], bool] = {}
    for a, b, c in combinations(range(4), 3):
        Rab = Rij[(a, b)]
        Rac = Rij[(a, c)]
        Rbc = Rij[(b, c)]
        residual = Rab * Rac * Rbc - Rbc * Rac * Rab
        result[(a, b, c)] = _is_zero_matrix_symbolic(residual)
    return result
