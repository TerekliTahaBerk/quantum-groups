"""Independent regressions for the publication audit; exact arithmetic only."""
from itertools import product, combinations

import pytest
import sympy as sp

from quantum_group import (
    q, q_integer, q_binomial, build_representation, coproduct,
    R_matrix_V1, R_check_V1, R_matrix_V1_coproduct, R_check_V1_coproduct,
    intertwining_residual_V1, intertwining_holds_V1, swap_matrix,
    qybe_holds, braid_relation_holds, tensor_product, find_highest_weight_vectors,
    R_matrix_GLq21, all_Rij_GLq21, embed_R_in_tensor_power,
    root_of_unity_substitution,
)
from quantum_group.limits import crystal_asymptotics_E_pattern
from quantum_group.r_matrix import qybe_residual, braid_relation_residual


def zero(M):
    return all(sp.cancel(x) == 0 for x in M)


@pytest.mark.parametrize('X', ['E', 'F', 'K', 'K_inv'])
def test_coproduct_intertwining_and_braiding(X):
    D = coproduct(build_representation(1))[X]
    assert zero(intertwining_residual_V1(X))
    assert intertwining_holds_V1(X)
    B = R_check_V1_coproduct()
    assert zero(B*D - D*B)
    if X in ('E', 'F'):
        P = swap_matrix(2)
        assert not zero(R_matrix_V1()*D - P*D*P*R_matrix_V1())


def test_universal_fundamental_normalization():
    # Drinfeld §13: q=exp(h/2), X+X- scaling (q-q^-1)/h;
    # h Q_1 = h q^-1, exponential on output (+,-) = q^(1/2).
    t = sp.Symbol('t', positive=True)
    h = sp.Symbol('h', nonzero=True)
    rep = build_representation(1, t)
    cartan = sp.diag(sp.sqrt(t), 1/sp.sqrt(t), 1/sp.sqrt(t), sp.sqrt(t))
    coefficient = sp.simplify(h/t * (t-1/t)/h * sp.sqrt(t))
    image = cartan + coefficient*sp.kronecker_product(rep.E, rep.F)
    assert zero(sp.sqrt(t)*image - R_matrix_V1(t))


def test_compatible_braid_sectors_and_identities():
    B = R_check_V1_coproduct()
    T = tensor_product(build_representation(1), build_representation(1))
    for k, v in find_highest_weight_vectors(T):
        eigenvalue = q if k == 2 else -1/q
        for _ in range(k+1):
            assert zero(B*v - eigenvalue*v)
            v = T.F*v
    assert qybe_holds(R_matrix_V1_coproduct())
    assert braid_relation_holds(B)
    assert zero((B-q*sp.eye(4))*(B+sp.eye(4)/q))
    singlet = sp.Matrix([0, -1/q, 1, 0])
    assert not zero((R_check_V1()+sp.eye(4)/q)*singlet)


def test_specialized_braid_is_not_generically_diagonalizable():
    B = R_check_V1_coproduct(sp.I)
    assert B.eigenvals() == {sp.I: 4}
    assert (B-sp.I*sp.eye(4)).rank() == 1
    assert (B-sp.I*sp.eye(4))**2 == sp.zeros(4)


@pytest.mark.parametrize('m,n', [(1, 1), (2, 2), (3, 2)])
def test_full_cg_change_of_basis(m, n):
    T = tensor_product(build_representation(m), build_representation(n))
    columns, summands = [], []
    for k, highest in find_highest_weight_vectors(T):
        summands.append(build_representation(k))
        v = highest
        for _ in range(k+1):
            columns.append(v)
            v = (T.F*v).applyfunc(sp.cancel)
        assert zero(v)
    C = sp.Matrix.hstack(*columns).applyfunc(sp.cancel)
    assert C.shape == (T.dim, T.dim)
    assert sp.cancel(C.det(method='domain-ge')) != 0
    for name in ('E', 'F', 'K', 'K_inv'):
        D = sp.diag(*(getattr(rep, name) for rep in summands))
        assert zero(getattr(T, name)*C - C*D)


@pytest.mark.parametrize('value', [2, sp.Rational(2, 3), -1, sp.I])
def test_exact_parameters_and_laurent_specialization(value):
    rep = build_representation(3, value)
    for M in (rep.E, rep.F, rep.K, rep.K_inv, R_matrix_V1(value)):
        assert not M.atoms(sp.Float)
    for n in range(-4, 5):
        assert sp.simplify(q_integer(n, value)-q_integer(n).subs(q, value)) == 0
    for n in range(6):
        for k in range(n+1):
            assert sp.simplify(q_binomial(n, k, value)-q_binomial(n, k).subs(q, value)) == 0
    assert q_binomial(4, 2, sp.I) == 2
    assert q_integer(2, -1) == -2


def test_gl21_primary_source_entries():
    # Çelik–Çelik (2021), printed p.261, unnumbered R display after (3).
    entries = {(0,0):1, (1,1):q**2, (1,3):1-q**2, (2,2):q,
               (2,6):1-q**2, (3,3):1, (4,4):1, (5,5):q,
               (5,7):1-q**2, (6,6):q, (7,7):q, (8,8):q**2}
    R = R_matrix_GLq21()
    assert {(i,j):R[i,j] for i in range(9) for j in range(9) if R[i,j] != 0} == entries
    assert R.det() == q**8
    assert R.subs(q, 1) == sp.eye(9)


def component_embedding(R, i, j, n):
    # Independent basis-action formula; does not construct any swap matrix.
    parity = (0, 0, 1)
    basis = list(product(range(3), repeat=n))
    index = {v:k for k,v in enumerate(basis)}
    out = sp.zeros(3**n)
    for col, v in enumerate(basis):
        between = sum(parity[v[k]] for k in range(i+1, j))
        for a, b in product(range(3), repeat=2):
            coefficient = R[3*a+b, 3*v[i]+v[j]]
            if coefficient == 0:
                continue
            w = list(v)
            w[i], w[j] = a, b
            out[index[tuple(w)], col] = coefficient * (-1)**((parity[v[j]]+parity[b])*between)
    return out


def test_all_gl21_embeddings_against_independent_components():
    R = R_matrix_GLq21()
    placements = all_Rij_GLq21(4)
    for (i,j), actual in placements.items():
        assert zero(actual-component_embedding(R, i, j, 4))
    for a,b in combinations(placements, 2):
        if set(a).isdisjoint(b):
            assert zero(placements[a]*placements[b]-placements[b]*placements[a])


def test_ordinary_swap_fails_graded_ybe():
    R = R_matrix_GLq21()
    A, C = sp.kronecker_product(R, sp.eye(3)), sp.kronecker_product(sp.eye(3), R)
    P = sp.kronecker_product(swap_matrix(3), sp.eye(3))
    B = P*C*P
    residual = (A*B*C-C*B*A).applyfunc(sp.factor)
    assert {(i,j):residual[i,j] for i in range(27) for j in range(27) if residual[i,j] != 0} == {
        (8,24):2*q**2*(q-1)**2*(q+1)**2,
        (17,25):2*q**2*(q-1)**2*(q+1)**2,
    }


def test_even_operator_requirement():
    odd = sp.zeros(4)
    odd[0,1] = 1
    with pytest.raises(ValueError, match='even'):
        embed_R_in_tensor_power(odd, (0,1), 3, [0,1])
    with pytest.raises(ValueError, match='shape'):
        embed_R_in_tensor_power(sp.eye(3), (0,1), 3, [0,1])


@pytest.mark.parametrize('N', [0, 1, 2, 2.5])
def test_invalid_root_orders(N):
    with pytest.raises(ValueError, match='greater than 2'):
        root_of_unity_substitution(build_representation(1), N)


def test_root_of_unity_undivided_family():
    result = root_of_unity_substitution(build_representation(4), 4)
    assert zero(result['E^N'])
    assert not zero(result['F^N'])
    assert result['K^{2N}'] == sp.eye(5)


@pytest.mark.parametrize('n', [1, 2, 3, 4])
def test_crystal_leading_term(n):
    M = crystal_asymptotics_E_pattern(build_representation(n))
    assert all(
        M[i,j] == (q**(-(n-1)) if j == i+1 else 0)
        for i in range(n+1) for j in range(n+1))


@pytest.mark.parametrize('check', [qybe_residual, braid_relation_residual])
def test_nonsquare_R_is_rejected(check):
    with pytest.raises(ValueError, match='square'):
        check(sp.zeros(4, 3))


def test_counit_verification_uses_public_values(monkeypatch):
    import quantum_group.hopf as hopf
    monkeypatch.setattr(hopf, 'counit', lambda: {'E':sp.S.One, 'F':sp.S.Zero,
                                               'K':sp.S.One, 'K_inv':sp.S.One})
    assert not hopf.verify_counit(build_representation(1))['E'].holds
    assert not hopf.verify_all_hopf_axioms(build_representation(1))['counit']['E'].holds


def test_integer_parameter_through_public_facade():
    from quantum_group import QuantumGroupSL2
    group = QuantumGroupSL2(2)
    assert '2' in str(group)
    checks = group.verify(n=3)
    assert all(check.holds and not check.residual.atoms(sp.Float)
               for check in checks.values())


def test_q_binomial_recurrence_matches_generic_factorial_quotient():
    from quantum_group import q_factorial
    for n in range(7):
        for k in range(n+1):
            quotient = q_factorial(n)/(q_factorial(k)*q_factorial(n-k))
            assert sp.cancel(q_binomial(n,k)-quotient) == 0
