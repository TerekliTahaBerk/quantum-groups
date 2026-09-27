"""Regression tests for the shared matrix helpers and public input validation."""

import pytest
import sympy as sp

import quantum_group.hopf as hopf
import quantum_group.r_matrix as r_matrix
import quantum_group.relations as relations
import quantum_group.supergroup_gl21 as gl21
from quantum_group import (
    QuantumGroupSL2,
    R_matrix_GLq21,
    build_crystal,
    build_representation,
    cg_summands,
    crystal_nodes,
    crystal_string,
    embed_R_in_tensor_power,
    all_Rij_GLq21,
    is_zero_matrix,
    kron_list,
    plot_weight_diagram,
    q,
    q_binomial,
    q_factorial,
    q_integer,
    qybe_residual,
    swap_matrix,
    verify_on_representation,
    weight_of,
)
from quantum_group.linalg import kron


# ---------------------------------------------------------------------------
# Shared helpers and backward-compatible aliases
# ---------------------------------------------------------------------------

def test_kron_matches_sympy_kronecker_product():
    A = sp.Matrix([[1, q], [0, 2]])
    B = sp.Matrix([[0, 1, q**-1], [3, 0, 0]])
    assert kron(A, B) == sp.kronecker_product(A, B)
    assert kron_list([A, B, A]) == sp.kronecker_product(A, B, A)


def test_kron_list_rejects_empty_input():
    with pytest.raises(ValueError, match="at least one"):
        kron_list([])


def test_private_aliases_point_to_shared_helpers():
    assert hopf._kron is kron
    assert hopf.kron_list is kron_list
    assert relations.is_zero_matrix is is_zero_matrix
    assert relations._is_zero_matrix is is_zero_matrix
    assert r_matrix._is_zero is is_zero_matrix
    assert gl21._is_zero_matrix_symbolic is is_zero_matrix


def test_is_zero_matrix_requires_exact_cancellation():
    assert is_zero_matrix(sp.Matrix([[q - q, (q**2 - 1) / (q - 1) - q - 1]]))
    assert not is_zero_matrix(sp.Matrix([[0, q - 1]]))


# ---------------------------------------------------------------------------
# Non-integral or negative sizes, weights and indices
# ---------------------------------------------------------------------------

@pytest.mark.parametrize("bad", [1.5, 2.0, sp.Rational(1, 2), "2", True])
def test_build_representation_rejects_non_integral_weight(bad):
    with pytest.raises(TypeError, match="integer"):
        build_representation(bad)


def test_build_representation_accepts_sympy_integer():
    assert build_representation(sp.Integer(2)).dim == 3


def test_build_representation_rejects_negative_weight():
    with pytest.raises(ValueError, match="nonnegative"):
        build_representation(-1)


@pytest.mark.parametrize("func,args", [
    (q_integer, (1.5,)),
    (q_factorial, (2.5,)),
    (q_binomial, (4, 1.0)),
    (q_binomial, (4.0, 1)),
])
def test_q_arithmetic_rejects_non_integers(func, args):
    with pytest.raises(TypeError, match="integer"):
        func(*args)


def test_q_factorial_rejects_negative():
    with pytest.raises(ValueError, match="n >= 0"):
        q_factorial(-1)


@pytest.mark.parametrize("func", [build_crystal, crystal_nodes, crystal_string,
                                  plot_weight_diagram])
def test_crystal_and_plot_sizes_must_be_nonnegative_integers(func):
    with pytest.raises(ValueError):
        func(-1)
    with pytest.raises(TypeError):
        func(1.5)


@pytest.mark.parametrize("m,n", [(-1, 1), (1, -2)])
def test_cg_summands_rejects_negative_weights(m, n):
    with pytest.raises(ValueError, match=">= 0"):
        cg_summands(m, n)


def test_weight_of_rejects_float_index():
    with pytest.raises(TypeError, match="integer"):
        weight_of(build_representation(2), 1.0)


@pytest.mark.parametrize("d", [0, -1])
def test_swap_matrix_rejects_nonpositive_dimension(d):
    with pytest.raises(ValueError, match=">= 1"):
        swap_matrix(d)


# ---------------------------------------------------------------------------
# Matrix shapes
# ---------------------------------------------------------------------------

def test_verify_on_representation_rejects_mismatched_shapes():
    rep2, rep3 = build_representation(2), build_representation(3)
    with pytest.raises(ValueError, match="same shape"):
        verify_on_representation(rep2.E, rep3.F, rep2.K, rep2.K_inv)


def test_verify_on_representation_rejects_non_square():
    rep = build_representation(1)
    with pytest.raises(ValueError, match="square"):
        verify_on_representation(sp.zeros(2, 3), rep.F, rep.K, rep.K_inv)


def test_verify_on_representation_rejects_non_matrix():
    rep = build_representation(1)
    with pytest.raises(TypeError, match="Matrix"):
        verify_on_representation([[0, 1], [0, 0]], rep.F, rep.K, rep.K_inv)


@pytest.mark.parametrize("R", [sp.zeros(3, 3), sp.zeros(0, 0)])
def test_qybe_rejects_non_tensor_square_dimensions(R):
    with pytest.raises(ValueError, match="d²"):
        qybe_residual(R)


# ---------------------------------------------------------------------------
# Graded embeddings
# ---------------------------------------------------------------------------

@pytest.mark.parametrize("positions", [(0, 1.0), (0, 1, 2), (1, 0), (0, 3)])
def test_embedding_rejects_invalid_positions(positions):
    with pytest.raises((TypeError, ValueError)):
        embed_R_in_tensor_power(R_matrix_GLq21(), positions, 3, [0, 0, 1])


@pytest.mark.parametrize("parity", [[], [0, 0, 2]])
def test_embedding_rejects_invalid_parity(parity):
    with pytest.raises(ValueError, match="parity"):
        embed_R_in_tensor_power(R_matrix_GLq21(), (0, 1), 3, parity)


@pytest.mark.parametrize("n", [1, 2.0])
def test_tensor_power_must_be_integer_at_least_two(n):
    with pytest.raises((TypeError, ValueError)):
        all_Rij_GLq21(n)


# ---------------------------------------------------------------------------
# Deformation parameter
# ---------------------------------------------------------------------------

def test_facade_rejects_zero_q():
    with pytest.raises(ValueError, match="nonzero"):
        QuantumGroupSL2(0)


def test_symbolic_parameters_remain_allowed():
    t = sp.Symbol("t", nonzero=True)
    checks = QuantumGroupSL2(t).verify(n=2)
    assert all(check.holds for check in checks.values())
