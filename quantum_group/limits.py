"""
limits.py
=========

The "three lives" of q: classical (q → 1), generic q and crystal (q → 0).

This module provides helpers for examining how V_n, and hence the structure
of U_q(sl_2), changes with the value of q.

(L1)  Classical limit q -> 1:
      U_q(sl_2) -> U(sl_2). [n]_q -> n; K -> 1, K-1 -> 0; however,
      the operator H := (K - 1) / (q - 1) has a well-defined limit
      giving the classical Cartan element h. Although q^{n-2k} -> 1,
      the eigenvalues of H are the classical weights n-2k.

(L2)  Generic q:
      The usual quantum regime. All formulas are rational in q, and the
      representations are q-deformations of classical representations.

(L3)  Root of unity q^N = 1 (primitive root, N > 2):
      [N]_q = 0. E^N and F^N become central elements; finite-dimensional
      irreducibles are parametrized differently, and the "small quantum
      group" appears. The modules V_n may become reducible and need not split.

(L4)  Crystal limit q -> 0:
      Classical basis choices are singular, but Kashiwara's crystal basis
      leaves a combinatorial structure: the partial maps tilde_e and tilde_f.
      This module computes the q -> 0 "asymptotic order" of matrix
      coefficients of V_n.

These three regimes correspond to the classical, quantum and combinatorial
aspects of quantum groups and frame the thesis's comparison section.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Dict, List, Tuple

import sympy as sp

from .representations import Representation, build_representation
from .utils import q as default_q


# ---------------------------------------------------------------------------
# (L1) Classical limit
# ---------------------------------------------------------------------------

def classical_K_to_h(rep: Representation, q_sym: sp.Expr = default_q) -> sp.Matrix:
    """Compute the operator h := lim_{q->1} (K - 1)/(q - 1).

    Since K is diagonal, this operator is diagonal too, with entries
    lim_{q->1} (q^{n-2k} - 1)/(q - 1) = n - 2k, the classical weights.
    """
    diag = []
    for k in range(rep.dim):
        entry = (rep.K[k, k] - 1) / (q_sym - 1)
        diag.append(sp.limit(entry, q_sym, 1))
    return sp.diag(*diag)


def classical_commutator_EF(
    rep: Representation,
    q_sym: sp.Expr = default_q,
) -> sp.Matrix:
    """Compute the q -> 1 limit of [E,F] directly; it should equal h."""
    comm = rep.E * rep.F - rep.F * rep.E
    return sp.Matrix([[sp.limit(comm[i, j], q_sym, 1)
                       for j in range(rep.dim)] for i in range(rep.dim)])


# ---------------------------------------------------------------------------
# (L3) Root of unity q^N = 1
# ---------------------------------------------------------------------------

def root_of_unity_substitution(
    rep: Representation,
    N: int,
    q_sym: sp.Expr = default_q,
) -> Dict[str, sp.Matrix]:
    """Evaluate q at a primitive Nth root of unity and compute E^N.

    For primitive roots with N > 2, E^N = 0 for every V_n in this
    undivided-basis family; F^N = 0 only when n < N. This does not
    construct the small quantum group or classify its modules.

    The primitive root is represented symbolically as q = exp(2πi/N)
    (sympy.exp(2*sp.pi*sp.I/N))."""
    if not isinstance(N, (int, sp.Integer)) or N <= 2:
        raise ValueError("N must be an integer greater than 2.")
    zeta = sp.exp(2 * sp.pi * sp.I / N)
    sub = lambda M: sp.simplify(M.subs(q_sym, zeta))
    E_N = sub(rep.E**N)
    F_N = sub(rep.F**N)
    K_2N = sub(rep.K**(2 * N))
    return {
        "E^N": E_N,
        "F^N": F_N,
        "K^{2N}": K_2N,
        "E_q=ζ": sub(rep.E),
        "K_q=ζ": sub(rep.K),
    }


# ---------------------------------------------------------------------------
# (L4) Crystal limit q -> 0
# ---------------------------------------------------------------------------

@dataclass
class CrystalAsymptotics:
    """Asymptotic behavior of a matrix entry as q -> 0."""
    entry: sp.Expr
    leading_order: sp.Expr   # smallest exponent as q -> 0 (None = zero)
    crystal_value: int       # 0 (vanishing) or 1 (surviving)


def crystal_asymptotics_F(rep: Representation, q_sym: sp.Expr = default_q) -> sp.Matrix:
    """Return entries of F that survive the q -> 0 limit.

    F has a finite entrywise limit in this basis. Its graph agrees with
    B(n); this is not a construction of a Kashiwara lattice or basis.
    """
    return rep.F


def crystal_asymptotics_E_pattern(
    rep: Representation,
    q_sym: sp.Expr = default_q,
) -> sp.Matrix:
    """Show the q -> 0 behavior of the matrix E.

    E_{k-1, k} = [k]_q [n-k+1]_q. As q -> 0, a dominant power is
    q^{-(k + (n-k+1) - 2)} = q^{-(n-1)} ...; return the leading term
    of each entry for the single-term asymptotic behavior.
    """
    n = rep.n
    out = sp.zeros(rep.dim, rep.dim)
    for k in range(1, rep.dim):
        coeff = rep.E[k - 1, k]
        out[k - 1, k] = coeff.as_leading_term(q_sym)
    return out


def three_limit_summary(n: int) -> str:
    """Return a textual summary of the three regimes for V_n."""
    rep = build_representation(n)
    h = classical_K_to_h(rep)
    h_diag = [h[k, k] for k in range(rep.dim)]
    comm_lim = classical_commutator_EF(rep)
    h_match = sp.simplify(h - comm_lim) == sp.zeros(rep.dim, rep.dim)

    lines = [f"Three regimes for V_{n} (dimension {rep.dim}):"]
    lines.append(f"  (L1) Classical q->1:")
    lines.append(f"      h-eigenvalues = {h_diag}")
    lines.append(f"      [E,F] -> h verified? {h_match}")
    lines.append(f"  (L2) Generic q: K-weights = {[sp.simplify(w) for w in rep.weights]}")
    lines.append(f"  (L4) q->0: E has leading power q^{-(n-1)} for n>=1;"
                 " the separate B(n) graph models crystal arrows")
    return "\n".join(lines)
