"""Tests of three regimes (classical / generic q / root of unity)."""

import sympy as sp
import pytest

from quantum_group import (
    build_representation,
    classical_K_to_h, classical_commutator_EF,
    root_of_unity_substitution,
)


@pytest.mark.parametrize("n", [1, 2, 3, 4])
def test_classical_limit_h_diagonal(n):
    """h := lim (K-1)/(q-1) is diagonal, with classical weights n - 2k
    as its eigenvalues."""
    rep = build_representation(n)
    h = classical_K_to_h(rep)
    expected = sp.diag(*[n - 2 * k for k in range(n + 1)])
    assert sp.simplify(h - expected) == sp.zeros(n + 1, n + 1)


@pytest.mark.parametrize("n", [1, 2, 3])
def test_classical_commutator_equals_h(n):
    """[E,F] -> h in the classical limit."""
    rep = build_representation(n)
    h = classical_K_to_h(rep)
    comm_lim = classical_commutator_EF(rep)
    assert sp.simplify(h - comm_lim) == sp.zeros(n + 1, n + 1)


def test_root_of_unity_V2_at_q4_singular():
    """At the root of unity q^4 = 1, the E matrix of V_2 vanishes (reducible)."""
    rep = build_representation(2)
    sub = root_of_unity_substitution(rep, 4)
    assert sub["E_q=ζ"] == sp.zeros(3, 3)


def test_root_of_unity_V1_at_q3_regular():
    """At the root of unity q^3 = 1, the E matrix of V_1 remains nonzero."""
    rep = build_representation(1)
    sub = root_of_unity_substitution(rep, 3)
    # On V_1, E has one entry equal to 1, independent of zeta.
    assert sub["E_q=ζ"] != sp.zeros(2, 2)
