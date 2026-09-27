"""
crystal.py
==========

Combinatorial model of the Kashiwara crystal B(n) for U_q(sl_2).

In the q -> 0 limit, the basis vectors of V_n become the combinatorial
objects {b_0, b_1, ..., b_n}. The generators E and F reduce to partial maps:

    tilde_f(b_k) = b_{k+1},   for k < n;     tilde_f(b_n) = None
    tilde_e(b_k) = b_{k-1},   for k > 0;     tilde_e(b_0) = None

Weight map: wt(b_k) = n - 2k.

This module constructs the crystal as a directed labelled graph: nodes carry
(name, weight) pairs, and edges are tilde_f arrows.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import List, Optional, Tuple

import networkx as nx

from ._validation import as_int


@dataclass
class CrystalNode:
    """A single crystal node in B(n)."""
    index: int      # k = 0, 1, ..., n
    weight: int     # n - 2k
    label: str      # "b_k"


def build_crystal(n: int) -> nx.DiGraph:
    """Construct the crystal graph B(n).

    Parameters
    ----------
    n : int
        Highest weight (dimension = n + 1). n >= 0.

    Returns
    -------
    networkx.DiGraph
        Each node "b_k" (str) has 'index', 'weight' and 'label' attributes.
        Edges are tilde_f arrows (b_k -> b_{k+1}).
    """
    n = as_int(n, "n")
    if n < 0:
        raise ValueError("n must be nonnegative.")

    G = nx.DiGraph()
    for k in range(n + 1):
        node = f"b_{k}"
        G.add_node(node, index=k, weight=n - 2 * k, label=node)

    for k in range(n):
        G.add_edge(f"b_{k}", f"b_{k+1}", operator="f")

    G.graph["n"] = n
    return G


def crystal_nodes(n: int) -> List[CrystalNode]:
    """Return the nodes of B(n) as a list of CrystalNode objects."""
    n = as_int(n, "n", minimum=0)
    return [CrystalNode(index=k, weight=n - 2 * k, label=f"b_{k}")
            for k in range(n + 1)]


def f_tilde(node: CrystalNode, n: int) -> Optional[CrystalNode]:
    """Apply the crystal operator tilde_f."""
    if node.index >= n:
        return None
    return CrystalNode(index=node.index + 1, weight=n - 2 * (node.index + 1),
                       label=f"b_{node.index + 1}")


def e_tilde(node: CrystalNode, n: int) -> Optional[CrystalNode]:
    """Apply the crystal operator tilde_e."""
    if node.index <= 0:
        return None
    return CrystalNode(index=node.index - 1, weight=n - 2 * (node.index - 1),
                       label=f"b_{node.index - 1}")


def crystal_string(n: int) -> str:
    """Return B(n) as text: b_0 -f-> b_1 -f-> ... -f-> b_n."""
    n = as_int(n, "n", minimum=0)
    return " -f-> ".join(f"b_{k}" for k in range(n + 1))
