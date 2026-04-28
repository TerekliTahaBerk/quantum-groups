"""R-matris, Yang–Baxter ve örgü bağıntısı testleri."""

import sympy as sp
import pytest

from quantum_group import (
    R_matrix_V1, R_check_V1,
    qybe_holds, braid_relation_holds,
    R_check_eigenvalues, jones_skein_relation_check,
)


def test_R_satisfies_qybe():
    R = R_matrix_V1()
    assert qybe_holds(R)


def test_R_check_satisfies_braid():
    Rv = R_check_V1()
    assert braid_relation_holds(Rv)


def test_R_check_eigenvalues():
    """Ř özdeğerleri q (3 katlı) ve −q^{-1} (1 katlı)."""
    q = sp.Symbol("q", nonzero=True)
    eigs = R_check_eigenvalues()
    assert eigs == {q: 3, -1/q: 1}


def test_jones_skein():
    """Ř - Ř^{-1} = (q - q^{-1}) I."""
    res = jones_skein_relation_check()
    assert all(res.values())


def test_R_invertibility():
    R = R_matrix_V1()
    R_inv = R.inv()
    prod = sp.simplify(R * R_inv)
    assert prod == sp.eye(4)
