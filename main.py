"""
main.py
=======

End-to-end demonstration script for the U_q(sl_2) package.

Run with:

    python3 main.py

Steps:
1. q-arithmetic examples
2. Defining relations of U_q(sl_2)
3. Construction and relation checks for V_0..V_4
4. Crystal paths
5. Save the V_4 weight and crystal diagram as a PNG
6. Graded Yang–Baxter verification for GL_q(2|1)
"""

from __future__ import annotations

import os

import matplotlib

matplotlib.use("Agg")  # for headless environments

import sympy as sp

from quantum_group import (
    QuantumGroupSL2,
    q_integer,
    q_factorial,
    classical_limit,
    plot_combined,
    crystal_string,
    summarize_GLq21_ybe,
)


def section(title: str) -> None:
    print()
    print("=" * 72)
    print(title)
    print("=" * 72)


def main() -> None:
    Uq = QuantumGroupSL2()

    section("1. q-arithmetic")
    for n in range(6):
        qn = sp.simplify(q_integer(n))
        print(f"  [{n}]_q = {qn}     (q->1: {classical_limit(qn)})")
    print(f"  [4]_q! = {q_factorial(4)}")

    section("2. Defining relations of U_q(sl_2)")
    Uq.print_relations()

    section("3. Construction and relation checks for V_n")
    for n in range(5):
        rep = Uq.representation(n)
        checks = Uq.verify(rep)
        ok = all(c.holds for c in checks.values())
        print(f"  V_{n}: dimension={rep.dim}, all relations hold = {ok}")
        print(f"    K-weights: {[sp.simplify(w) for w in rep.weights]}")

    section("4. Crystals")
    for n in range(5):
        print(f"  B({n}): {crystal_string(n)}")

    section("5. Diagram output")
    out_dir = os.path.join(os.path.dirname(__file__), "outputs")
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "V4_combined.png")
    fig = plot_combined(4)
    fig.savefig(out_path, dpi=120)
    print(f"  Saved: {out_path}")

    section("6. GL_q(2|1) graded Yang-Baxter verification")
    summary = summarize_GLq21_ybe()
    print("  R shape:", summary["R_shape"])
    print("  Triple tensor shape:", summary["triple_tensor_shape"])
    print("  Number of nonzero R entries:", summary["nonzero_entries_R"])
    print("  Graded YBE holds:", summary["residual_is_zero"])


if __name__ == "__main__":
    main()
