"""
visualization.py
================

U_q(sl_2) temsillerinin ve kristallerinin görselleştirilmesi.

İki tip diyagram:

1. **Ağırlık diyagramı** — V_n'in K-ağırlıkları (n - 2k, k = 0..n) bir
   sayı doğrusu üzerinde nokta olarak çizilir. Bu, klasik sl_2 ağırlık
   gösterimiyle aynı yapıya sahiptir; q yalnızca özdeğerlerin çarpan
   tabanını değiştirir, üs örüntüsünü değil.

2. **Kristal grafiği** — B(n) kristali bir yönlü yol b_0 -> b_1 -> ... -> b_n
   olarak networkx ile çizilir.

Tüm fonksiyonlar matplotlib `Figure` döndürür; ekrana gösterme veya kayıt
çağıran sorumluluğundadır.
"""

from __future__ import annotations

from typing import Optional

import matplotlib.pyplot as plt
import networkx as nx

from .crystal import build_crystal


# ---------------------------------------------------------------------------
# Ağırlık diyagramı
# ---------------------------------------------------------------------------

def plot_weight_diagram(n: int, ax: Optional[plt.Axes] = None) -> plt.Figure:
    """V_n için ağırlık diyagramı (sayı doğrusu üzerinde noktalar).

    Ağırlıklar n, n-2, ..., -n+2, -n.
    """
    weights = [n - 2 * k for k in range(n + 1)]

    if ax is None:
        fig, ax = plt.subplots(figsize=(max(4, n + 2), 1.8))
    else:
        fig = ax.figure

    ax.axhline(0, color="lightgray", linewidth=1, zorder=0)
    ax.scatter(weights, [0] * len(weights), s=120, color="C0", zorder=3)

    for w in weights:
        ax.annotate(f"{w}", xy=(w, 0), xytext=(0, 10),
                    textcoords="offset points", ha="center", fontsize=10)

    pad = 1
    ax.set_xlim(min(weights) - pad, max(weights) + pad)
    ax.set_ylim(-1, 1)
    ax.set_yticks([])
    ax.set_xticks(weights)
    ax.set_xlabel("ağırlık (K-özdeğerinin q-üssü)")
    ax.set_title(f"V_{n} ağırlık diyagramı (boyut {n+1})")
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    ax.spines["left"].set_visible(False)
    fig.tight_layout()
    return fig


# ---------------------------------------------------------------------------
# Kristal grafiği
# ---------------------------------------------------------------------------

def plot_crystal_graph(n: int, ax: Optional[plt.Axes] = None) -> plt.Figure:
    """B(n) kristal grafiğini yatay yönlü yol olarak çizer."""
    G = build_crystal(n)

    if ax is None:
        fig, ax = plt.subplots(figsize=(max(5, n + 2), 2.0))
    else:
        fig = ax.figure

    pos = {f"b_{k}": (k, 0) for k in range(n + 1)}

    nx.draw_networkx_nodes(G, pos, node_color="C1", node_size=600, ax=ax)
    nx.draw_networkx_labels(G, pos, labels={node: node for node in G.nodes()},
                            font_size=10, ax=ax)
    nx.draw_networkx_edges(G, pos, arrows=True, arrowstyle="-|>",
                           arrowsize=18, edge_color="black",
                           connectionstyle="arc3", ax=ax)
    edge_labels = {(u, v): r"$\tilde f$" for u, v in G.edges()}
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels,
                                 font_size=9, ax=ax)

    ax.set_title(f"B({n}) kristal grafiği")
    ax.set_axis_off()
    ax.set_xlim(-0.5, n + 0.5)
    ax.set_ylim(-0.5, 0.5)
    fig.tight_layout()
    return fig


def plot_combined(n: int) -> plt.Figure:
    """Bir çağrıda hem ağırlık diyagramı hem kristal grafiğini çizer."""
    fig, axes = plt.subplots(2, 1, figsize=(max(5, n + 2), 4.0))
    plot_weight_diagram(n, ax=axes[0])
    plot_crystal_graph(n, ax=axes[1])
    fig.tight_layout()
    return fig
