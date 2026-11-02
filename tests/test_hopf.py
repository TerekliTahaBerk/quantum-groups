"""Tests of the Hopf structure and its axioms."""

import pytest
import sympy as sp

from quantum_group import (
    antipode,
    build_representation,
    coproduct,
    counit,
    verify_all_hopf_axioms,
)


@pytest.mark.parametrize("n", [1, 2, 3])
def test_hopf_axioms_on_Vn(n):
    rep = build_representation(n)
    res = verify_all_hopf_axioms(rep)
    for group, checks in res.items():
        for X, c in checks.items():
            assert c.holds, f"V_{n}, {group}/{X} did not hold"


def test_coproduct_dimensions():
    rep = build_representation(2)
    Delta = coproduct(rep)
    for _X, M in Delta.items():
        assert M.shape == (rep.dim**2, rep.dim**2)


def test_counit_values():
    eps = counit()
    assert eps["E"] == 0
    assert eps["F"] == 0
    assert eps["K"] == 1
    assert eps["K_inv"] == 1


def test_antipode_K_relation():
    """S(K) S(K^{-1}) must equal 1."""
    rep = build_representation(3)
    S = antipode(rep)
    prod = sp.simplify(S["K"] * S["K_inv"])
    assert prod == sp.eye(rep.dim)
