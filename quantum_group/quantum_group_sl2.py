"""
quantum_group_sl2.py
====================

QuantumGroupSL2: the package's high-level facade.

This class wraps U_q(sl_2) in one object, bringing together its generators,
relations and representation-building methods.
"""

from __future__ import annotations

from typing import Dict, Optional

import sympy as sp

from . import generators as gens
from . import relations as rels
from . import representations as reps
from .utils import q as default_q


class QuantumGroupSL2:
    """Facade class representing the quantum group U_q(sl_2).

    Parameters
    ----------
    q : sympy expression, defaults to the module symbol `q`
        Deformation parameter. May be numerical (e.g. sp.Rational(2,1))
        or symbolic.

    Example
    -------
    >>> Uq = QuantumGroupSL2()
    >>> print(Uq)
    U_q(sl_2) quantum group (q symbolic)
    >>> rep = Uq.representation(2)
    >>> Uq.verify(rep)['R4'].holds
    True
    """

    def __init__(self, q: sp.Expr = default_q):
        self.q = q
        self.E = gens.E
        self.F = gens.F
        self.K = gens.K
        self.K_inv = gens.K_inv

    # ------------------------------------------------------------------
    # Generator and relation access
    # ------------------------------------------------------------------

    def generators(self) -> dict:
        """Return the generators as a name-to-symbol dictionary."""
        return {"E": self.E, "F": self.F, "K": self.K, "K_inv": self.K_inv,
                "q": self.q}

    def relations(self):
        """Return the symbolic defining relations."""
        return rels.symbolic_relations()

    def print_relations(self) -> None:
        """Print the relations in a readable form."""
        print(rels.pretty_print_relations())

    # ------------------------------------------------------------------
    # Representation construction and verification
    # ------------------------------------------------------------------

    def representation(self, n: int) -> reps.Representation:
        """Return the irreducible representation V_n (dimension n + 1)."""
        return reps.build_representation(n, q_sym=self.q)

    def verify(
        self,
        rep: Optional[reps.Representation] = None,
        n: Optional[int] = None,
    ) -> Dict[str, rels.RelationCheck]:
        """Check the four relations on a representation.

        If `rep` is omitted and `n` is supplied, construct and check V_n.
        """
        if rep is None:
            if n is None:
                raise ValueError("Provide a representation or a value for n.")
            rep = self.representation(n)

        return rels.verify_on_representation(
            E_mat=rep.E,
            F_mat=rep.F,
            K_mat=rep.K,
            Kinv_mat=rep.K_inv,
            q_sym=self.q,
        )

    # ------------------------------------------------------------------
    # Readable representation
    # ------------------------------------------------------------------

    def __repr__(self) -> str:  # pragma: no cover
        q_desc = "symbolic" if self.q.free_symbols else f"={self.q}"
        return f"U_q(sl_2) quantum group (q {q_desc})"

    def __str__(self) -> str:  # pragma: no cover
        return self.__repr__()
