"""Visualization smoke tests using a noninteractive backend."""

import matplotlib

matplotlib.use("Agg")

import matplotlib.pyplot as plt

from quantum_group import plot_combined, plot_crystal_graph, plot_weight_diagram


def test_plot_weight_diagram_smoke():
    fig = plot_weight_diagram(2)
    assert fig.axes
    plt.close(fig)


def test_plot_crystal_graph_smoke():
    fig = plot_crystal_graph(2)
    assert fig.axes
    plt.close(fig)


def test_plot_combined_smoke():
    fig = plot_combined(2)
    assert len(fig.axes) == 2
    plt.close(fig)
