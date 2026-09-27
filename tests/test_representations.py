"""
test_representations.py
=======================

Structural tests of V_n representations:
- correct dimension
- behavior of highest- and lowest-weight vectors
- classical limit of the weights
- strict lower-triangular F and strict upper-triangular E
"""

import sympy as sp
import pytest

from quantum_group import (
    build_representation,
    highest_weight_vector,
    lowest_weight_vector,
    weight_of,
    classical_limit,
    crystal_string,
    build_crystal,
    f_tilde,
    e_tilde,
    CrystalNode,
    q,
)


# ---------------------------------------------------------------------------
# Dimension and structure
# ---------------------------------------------------------------------------

@pytest.mark.parametrize("n", [0, 1, 2, 3, 5])
def test_dimension(n):
    rep = build_representation(n)
    assert rep.dim == n + 1
    assert rep.E.shape == (n + 1, n + 1)
    assert rep.F.shape == (n + 1, n + 1)
    assert rep.K.shape == (n + 1, n + 1)


@pytest.mark.parametrize("n", [1, 2, 3, 4])
def test_F_is_strict_lower_shift(n):
    """F . v_k = v_{k+1}: F has ones only on the first lower diagonal."""
    rep = build_representation(n)
    for i in range(rep.dim):
        for j in range(rep.dim):
            if i == j + 1:
                assert rep.F[i, j] == 1
            else:
                assert rep.F[i, j] == 0


@pytest.mark.parametrize("n", [1, 2, 3, 4])
def test_E_strict_upper_shift_pattern(n):
    """E has nonzero entries only at positions (k-1, k)."""
    rep = build_representation(n)
    for i in range(rep.dim):
        for j in range(rep.dim):
            if i + 1 != j:
                assert rep.E[i, j] == 0, f"E[{i},{j}] != 0 for n={n}"


# ---------------------------------------------------------------------------
# Highest- and lowest-weight vectors
# ---------------------------------------------------------------------------

@pytest.mark.parametrize("n", [0, 1, 2, 3, 4])
def test_highest_weight_killed_by_E(n):
    rep = build_representation(n)
    v0 = highest_weight_vector(rep)
    assert sp.simplify(rep.E * v0) == sp.zeros(rep.dim, 1)


@pytest.mark.parametrize("n", [0, 1, 2, 3, 4])
def test_lowest_weight_killed_by_F(n):
    rep = build_representation(n)
    vn = lowest_weight_vector(rep)
    assert sp.simplify(rep.F * vn) == sp.zeros(rep.dim, 1)


@pytest.mark.parametrize("n", [1, 2, 3, 4])
def test_highest_weight_K_eigenvalue(n):
    """K . v_0 = q^n v_0."""
    rep = build_representation(n)
    v0 = highest_weight_vector(rep)
    Kv = rep.K * v0
    expected = q**n * v0
    assert sp.simplify(Kv - expected) == sp.zeros(rep.dim, 1)


@pytest.mark.parametrize("n", [1, 2, 3, 4])
def test_weights_classical_limit(n):
    """As q -> 1, the K-eigenvalues approach 1 (q^{n-2k} -> 1)."""
    rep = build_representation(n)
    for k in range(rep.dim):
        assert classical_limit(weight_of(rep, k)) == 1


# ---------------------------------------------------------------------------
# Crystal
# ---------------------------------------------------------------------------

@pytest.mark.parametrize("n", [0, 1, 2, 4])
def test_crystal_node_count(n):
    G = build_crystal(n)
    assert G.number_of_nodes() == n + 1
    assert G.number_of_edges() == n


def test_crystal_string_format():
    assert crystal_string(3) == "b_0 -f-> b_1 -f-> b_2 -f-> b_3"


def test_crystal_operators_boundary():
    n = 3
    top = CrystalNode(index=0, weight=3, label="b_0")
    bot = CrystalNode(index=n, weight=-3, label=f"b_{n}")
    assert e_tilde(top, n) is None
    assert f_tilde(bot, n) is None
    nxt = f_tilde(top, n)
    assert nxt is not None and nxt.index == 1 and nxt.weight == 1
