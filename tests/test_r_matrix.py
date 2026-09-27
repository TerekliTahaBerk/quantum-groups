"""R-matris, Yang–Baxter ve örgü bağıntısı testleri."""

import sympy as sp
import pytest

from quantum_group import (
    R_matrix_V1, R_check_V1,
    qybe_holds, braid_relation_holds,
    R_check_eigenvalues, hecke_skein_relation_check,
    jones_skein_relation_check,
    q,
)


def test_R_satisfies_qybe():
    R = R_matrix_V1()
    assert qybe_holds(R)


def test_R_matrix_V1_exact_entries():
    expected = sp.Matrix([
        [q, 0, 0, 0],
        [0, 1, q - q**(-1), 0],
        [0, 0, 1, 0],
        [0, 0, 0, q],
    ])
    assert sp.simplify(R_matrix_V1() - expected) == sp.zeros(4, 4)


def test_R_check_satisfies_braid():
    Rv = R_check_V1()
    assert braid_relation_holds(Rv)


def test_R_check_eigenvalues():
    """Ř özdeğerleri q (3 katlı) ve −q^{-1} (1 katlı)."""
    q = sp.Symbol("q", nonzero=True)
    eigs = R_check_eigenvalues()
    assert eigs == {q: 3, -1/q: 1}


def test_hecke_skein():
    """Ř - Ř^{-1} = (q - q^{-1}) I."""
    res = hecke_skein_relation_check()
    assert all(res.values())


def test_jones_skein():
    """Eski ad hâlâ çalışır, fakat DeprecationWarning verir."""
    with pytest.warns(DeprecationWarning, match="hecke_skein_relation_check"):
        res = jones_skein_relation_check()
    assert res == hecke_skein_relation_check()
    assert all(res.values())


def test_R_invertibility():
    R = R_matrix_V1()
    R_inv = R.inv()
    prod = sp.simplify(R * R_inv)
    assert prod == sp.eye(4)
