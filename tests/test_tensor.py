"""Tensör çarpımı ve Clebsch–Gordan ayrışımı testleri."""

import sympy as sp
import pytest

from quantum_group import (
    build_representation,
    tensor_product, cg_summands, find_highest_weight_vectors,
    verify_on_representation,
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
