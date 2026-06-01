"""Tensör çarpımı ve Clebsch–Gordan ayrışımı testleri."""

import sympy as sp
import pytest

from quantum_group import (
    build_representation,
    tensor_product, cg_summands, find_highest_weight_vectors,
    verify_on_representation,
    cg_decomposition_summary,
    q,
)


@pytest.mark.parametrize("m,n", [(1, 1), (2, 1), (2, 2), (3, 2)])
def test_tensor_satisfies_relations(m, n):
    """V_m ⊗ V_n üzerinde de U_q(sl_2) bağıntıları sağlanmalı."""
    A = build_representation(m)
    B = build_representation(n)
    T = tensor_product(A, B)
    checks = verify_on_representation(T.E, T.F, T.K, T.K_inv)
    assert all(c.holds for c in checks.values())


@pytest.mark.parametrize("m,n", [(1, 1), (2, 2), (3, 1), (3, 2)])
def test_cg_correct_summand_count(m, n):
    """V_m ⊗ V_n'de en yüksek ağırlık vektörlerinin sayısı min(m,n)+1."""
    A = build_representation(m)
    B = build_representation(n)
    T = tensor_product(A, B)
    hws = find_highest_weight_vectors(T)
    assert len(hws) == min(m, n) + 1


def test_cg_summands_correct():
    assert cg_summands(2, 2) == [0, 2, 4]
    assert cg_summands(3, 1) == [2, 4]


@pytest.mark.parametrize("m,n", [(1, 1), (2, 1), (2, 2)])
def test_highest_weight_vectors_killed_by_E(m, n):
    A = build_representation(m)
    B = build_representation(n)
    T = tensor_product(A, B)
    hws = find_highest_weight_vectors(T)
    for k, v in hws:
        Ev = sp.simplify(T.E * v)
        assert Ev == sp.zeros(T.dim, 1)


@pytest.mark.parametrize("m,n", [(1, 1), (2, 2), (3, 2)])
def test_highest_weight_vectors_have_expected_K_weight(m, n):
    A = build_representation(m)
    B = build_representation(n)
    T = tensor_product(A, B)
    for k, v in find_highest_weight_vectors(T):
        assert sp.simplify(T.K * v - q**k * v) == sp.zeros(T.dim, 1)


def test_cg_decomposition_summaries_for_manuscript_examples():
    assert "V_1 ⊗ V_1 ≅ V_2 ⊕ V_0" in cg_decomposition_summary(1, 1)
    assert "V_2 ⊗ V_2 ≅ V_4 ⊕ V_2 ⊕ V_0" in cg_decomposition_summary(2, 2)
    assert "V_3 ⊗ V_2 ≅ V_5 ⊕ V_3 ⊕ V_1" in cg_decomposition_summary(3, 2)
