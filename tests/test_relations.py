"""
test_relations.py
=================

q-aritmetik ve U_q(sl_2) bağıntılarının matris düzeyindeki testleri.
"""

import sympy as sp
import pytest

from quantum_group import (
    QuantumGroupSL2,
    build_representation,
    verify_on_representation,
    all_relations_hold,
    q_integer,
    q_factorial,
    q_binomial,
    classical_limit,
    q,
)


# ---------------------------------------------------------------------------
# q-aritmetik
# ---------------------------------------------------------------------------

@pytest.mark.parametrize("n", [1, 2, 3, 4, 5, 7])
def test_q_integer_classical_limit(n):
    """[n]_q -> n iken q -> 1."""
    assert classical_limit(q_integer(n)) == n


def test_q_integer_zero():
    assert q_integer(0) == 0


@pytest.mark.parametrize("n", [0, 1, 2, 3, 4])
def test_q_factorial_classical_limit(n):
    assert classical_limit(q_factorial(n)) == sp.factorial(n)


@pytest.mark.parametrize("n,k", [(4, 2), (5, 0), (5, 5), (6, 3)])
def test_q_binomial_classical_limit(n, k):
    assert classical_limit(q_binomial(n, k)) == sp.binomial(n, k)


def test_q_integer_symmetry():
    """[n]_q = q^{n-1} + q^{n-3} + ... + q^{-(n-1)} simetrisi."""
    n = 4
    expected = sum(q**(n - 1 - 2 * i) for i in range(n))
    assert sp.simplify(q_integer(n) - expected) == 0


# ---------------------------------------------------------------------------
# Bağıntılar (sembolik q ile matris doğrulaması)
# ---------------------------------------------------------------------------

@pytest.mark.parametrize("n", [0, 1, 2, 3, 4, 5])
def test_relations_symbolic_q(n):
    """V_n üzerinde dört bağıntı (sembolik q) sağlanır."""
    rep = build_representation(n)
    checks = verify_on_representation(rep.E, rep.F, rep.K, rep.K_inv)
    assert all_relations_hold(checks), {k: v.holds for k, v in checks.items()}


@pytest.mark.parametrize("n", [1, 2, 3])
def test_relations_numeric_q(n):
    """Sayısal q (örn. q = 2) altında da bağıntılar sağlanır."""
    q_num = sp.Rational(2)
    rep = build_representation(n, q_sym=q_num)
    checks = verify_on_representation(rep.E, rep.F, rep.K, rep.K_inv,
                                      q_sym=q_num)
    assert all_relations_hold(checks)


def test_facade_verify():
    """QuantumGroupSL2.verify(n=...) yolu çalışır."""
    Uq = QuantumGroupSL2()
    checks = Uq.verify(n=3)
    assert all_relations_hold(checks)


def test_relation_residual_is_matrix():
    """RelationCheck.residual bir SymPy Matrix nesnesidir."""
    rep = build_representation(2)
    checks = verify_on_representation(rep.E, rep.F, rep.K, rep.K_inv)
    for c in checks.values():
        assert isinstance(c.residual, sp.MatrixBase)
