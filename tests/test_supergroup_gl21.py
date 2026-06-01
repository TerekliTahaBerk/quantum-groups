"""
test_supergroup_gl21.py
=======================

GL_q(2|1) süpergrubu için R-matrisi, süper permütasyon ve graded
Yang–Baxter doğrulamasının pytest testleri.
"""

import sympy as sp

from quantum_group import (
    R_matrix_GLq21,
    super_parity_gl21,
    super_permutation_matrix,
    swap_matrix,
    R12_GLq21,
    R13_GLq21,
    R23_GLq21,
    graded_yang_baxter_residual_GLq21,
    graded_yang_baxter_holds_GLq21,
    embed_R_in_tensor_power,
    all_Rij_GLq21,
    braid_far_commutativity_residual_GLq21,
    local_ybe_on_four_tensor_GLq21,
)
from quantum_group.utils import q


# ---------------------------------------------------------------------------
# R-matrisi ve süper permütasyon
# ---------------------------------------------------------------------------

def test_R_matrix_shape():
    assert R_matrix_GLq21().shape == (9, 9)


def test_R_matrix_nonzero_pattern():
    R = R_matrix_GLq21()
    nonzero_positions = {
        (i, j) for i in range(9) for j in range(9)
        if sp.simplify(R[i, j]) != 0
    }
    expected = {
        (0, 0), (1, 1), (1, 3), (2, 2), (2, 6),
        (3, 3), (4, 4), (5, 5), (5, 7),
        (6, 6), (7, 7), (8, 8),
    }
    assert nonzero_positions == expected


def test_super_permutation_shape():
    P = super_permutation_matrix(super_parity_gl21())
    assert P.shape == (9, 9)


def test_super_permutation_involution():
    P = super_permutation_matrix(super_parity_gl21())
    assert P * P == sp.eye(9)


def test_super_permutation_odd_odd_sign():
    # e_3 ⊗ e_3 -> internal 0-index (2,2), düz index 8.
    P = super_permutation_matrix(super_parity_gl21())
    assert P[8, 8] == -1


def test_R12_R13_R23_shapes():
    assert R12_GLq21().shape == (27, 27)
    assert R13_GLq21().shape == (27, 27)
    assert R23_GLq21().shape == (27, 27)


def test_graded_R13_differs_from_ordinary_R13():
    R23 = R23_GLq21()
    P_super = super_permutation_matrix(super_parity_gl21())
    P_plain = swap_matrix(3)
    I = sp.eye(3)
    R13_super = sp.kronecker_product(P_super, I) * R23 * sp.kronecker_product(P_super, I)
    R13_plain = sp.kronecker_product(P_plain, I) * R23 * sp.kronecker_product(P_plain, I)
    assert sp.simplify(R13_super - R13_plain) != sp.zeros(27, 27)


# ---------------------------------------------------------------------------
# Graded Yang–Baxter
# ---------------------------------------------------------------------------

def test_GLq21_graded_yang_baxter_symbolic():
    assert graded_yang_baxter_holds_GLq21() is True


def test_GLq21_graded_yang_baxter_numeric_substitution():
    # Hızlı güvenlik testi: q = 2 için kalıntı sayısal olarak sıfır.
    residual = graded_yang_baxter_residual_GLq21(sp.Integer(2))
    assert residual == sp.zeros(27, 27)


# ---------------------------------------------------------------------------
# Genel çoklu tensör yerleşimi
# ---------------------------------------------------------------------------

def test_embed_R_tensor_power_3_matches_named_R12_R13_R23():
    parity = super_parity_gl21()
    R = R_matrix_GLq21()
    assert embed_R_in_tensor_power(R, (0, 1), 3, parity) == R12_GLq21()
    assert sp.simplify(
        embed_R_in_tensor_power(R, (0, 2), 3, parity) - R13_GLq21()
    ) == sp.zeros(27, 27)
    assert embed_R_in_tensor_power(R, (1, 2), 3, parity) == R23_GLq21()


def test_all_Rij_tensor_power_4_shapes():
    Rij = all_Rij_GLq21(4)
    assert len(Rij) == 6
    for M in Rij.values():
        assert M.shape == (81, 81)


# Not: V^{⊗4} testleri 81×81 matrislerle çalışır. Sembolik (genel q) doğrulama
# bu boyutta makul sürede tamamlandığından numeric ikame yerine doğrudan
# sembolik kontrol tercih edilmiştir; gerekirse q=2 ikamesiyle hızlandırılabilir.

def test_far_commutativity_R12_R34():
    residual = braid_far_commutativity_residual_GLq21()
    assert all(sp.simplify(x) == 0 for x in residual)


def test_local_ybe_on_four_tensor():
    result = local_ybe_on_four_tensor_GLq21()
    assert set(result.keys()) == {(0, 1, 2), (0, 1, 3), (0, 2, 3), (1, 2, 3)}
    assert all(result.values())
