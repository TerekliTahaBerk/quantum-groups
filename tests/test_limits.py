"""Üç limit (klasik / genel q / birim kök) testleri."""

import sympy as sp
import pytest

from quantum_group import (
    build_representation,
    classical_K_to_h, classical_commutator_EF,
    root_of_unity_substitution,
)


@pytest.mark.parametrize("n", [1, 2, 3, 4])
def test_classical_limit_h_diagonal(n):
    """h := lim (K-1)/(q-1) köşegen olur ve özdeğerleri n - 2k klasik
    ağırlıklarıdır."""
    rep = build_representation(n)
    h = classical_K_to_h(rep)
    expected = sp.diag(*[n - 2 * k for k in range(n + 1)])
    assert sp.simplify(h - expected) == sp.zeros(n + 1, n + 1)


@pytest.mark.parametrize("n", [1, 2, 3])
def test_classical_commutator_equals_h(n):
    """[E,F] -> h klasik limitte."""
    rep = build_representation(n)
    h = classical_K_to_h(rep)
    comm_lim = classical_commutator_EF(rep)
    assert sp.simplify(h - comm_lim) == sp.zeros(n + 1, n + 1)


def test_root_of_unity_V2_at_q4_singular():
    """q^4 = 1 birim kökünde V_2'nin E matrisi sıfırlanır (indirgenebilir)."""
    rep = build_representation(2)
    sub = root_of_unity_substitution(rep, 4)
    assert sub["E_q=ζ"] == sp.zeros(3, 3)


def test_root_of_unity_V1_at_q3_regular():
    """q^3 = 1 birim kökünde V_1'in E matrisi hala sıfır olmayan."""
    rep = build_representation(1)
    sub = root_of_unity_substitution(rep, 3)
    # V_1'de E sadece bir 1 girdisi vardır, zeta'ya bağlı değil
    assert sub["E_q=ζ"] != sp.zeros(2, 2)
