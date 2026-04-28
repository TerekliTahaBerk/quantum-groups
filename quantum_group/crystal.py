"""
crystal.py
==========

U_q(sl_2) için Kashiwara kristal taban B(n)'in kombinatoryal modeli.

q -> 0 limitinde V_n temsilinin baz vektörleri kombinatoryal nesnelere
{b_0, b_1, ..., b_n} dönüşür. E ve F üreteçleri kısmi fonksiyonlara indirgenir:

    tilde_f(b_k) = b_{k+1},   k < n iken;     tilde_f(b_n) = None
    tilde_e(b_k) = b_{k-1},   k > 0 iken;     tilde_e(b_0) = None

Ağırlık dönüşümü: wt(b_k) = n - 2k.

Bu dosya kristali yönlü etiketli bir grafik olarak inşa eder; düğümler
(name, weight) çiftleridir, kenarlar tilde_f oklarıdır.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import List, Optional, Tuple

import networkx as nx


@dataclass
class CrystalNode:
    """B(n) içindeki tek bir kristal düğümü."""
    index: int      # k = 0, 1, ..., n
    weight: int     # n - 2k
    label: str      # "b_k"


def build_crystal(n: int) -> nx.DiGraph:
    """B(n) kristal grafiğini inşa eder.

    Parametreler
    ------------
    n : int
        En yüksek ağırlık (boyut = n + 1). n >= 0.

    Dönüş
    -----
    networkx.DiGraph
        Düğüm = "b_k" (str). Her düğümde 'index', 'weight', 'label'
        nitelikleri bulunur. Kenarlar tilde_f okları (b_k -> b_{k+1}).
    """
    if n < 0:
        raise ValueError("n negatif olamaz.")

    G = nx.DiGraph()
    for k in range(n + 1):
        node = f"b_{k}"
        G.add_node(node, index=k, weight=n - 2 * k, label=node)

    for k in range(n):
        G.add_edge(f"b_{k}", f"b_{k+1}", operator="f")

    G.graph["n"] = n
    return G


def crystal_nodes(n: int) -> List[CrystalNode]:
    """B(n) düğümlerini CrystalNode listesi olarak döndürür."""
    return [CrystalNode(index=k, weight=n - 2 * k, label=f"b_{k}")
            for k in range(n + 1)]


def f_tilde(node: CrystalNode, n: int) -> Optional[CrystalNode]:
    """Kristal operatörü tilde_f."""
    if node.index >= n:
        return None
    return CrystalNode(index=node.index + 1, weight=n - 2 * (node.index + 1),
                       label=f"b_{node.index + 1}")


def e_tilde(node: CrystalNode, n: int) -> Optional[CrystalNode]:
    """Kristal operatörü tilde_e."""
    if node.index <= 0:
        return None
    return CrystalNode(index=node.index - 1, weight=n - 2 * (node.index - 1),
                       label=f"b_{node.index - 1}")


def crystal_string(n: int) -> str:
    """B(n) kristalini metin olarak döndürür: b_0 -f-> b_1 -f-> ... -f-> b_n."""
    return " -f-> ".join(f"b_{k}" for k in range(n + 1))
