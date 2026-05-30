"""
main.py
=======

U_q(sl_2) paketinin uçtan uca demo betiği.

Çalıştırmak için:

    python3 main.py

Adımlar:
1. q-aritmetik örnekleri
2. Tanımlayıcı bağıntıları yazdır
3. n = 0, 1, 2, 3, 4 için V_n inşa et ve doğrula
4. n = 4 için ağırlık + kristal diyagramını PNG olarak kaydet
"""

from __future__ import annotations

import os

import matplotlib

matplotlib.use("Agg")  # başsız ortamlar için

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

    section("1. q-aritmetik")
    for n in range(6):
        qn = sp.simplify(q_integer(n))
        print(f"  [{n}]_q = {qn}     (q->1: {classical_limit(qn)})")
    print(f"  [4]_q! = {q_factorial(4)}")

    section("2. U_q(sl_2) tanımlayıcı bağıntıları")
    Uq.print_relations()

    section("3. V_n inşası ve bağıntı doğrulaması")
    for n in range(5):
        rep = Uq.representation(n)
        checks = Uq.verify(rep)
        ok = all(c.holds for c in checks.values())
        print(f"  V_{n}: boyut={rep.dim}, tüm bağıntılar = {ok}")
        print(f"    K-ağırlıkları: {[sp.simplify(w) for w in rep.weights]}")

    section("4. Kristaller")
    for n in range(5):
        print(f"  B({n}): {crystal_string(n)}")

    section("5. Diyagram çıktısı")
    out_dir = os.path.join(os.path.dirname(__file__), "outputs")
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "V4_combined.png")
    fig = plot_combined(4)
    fig.savefig(out_path, dpi=120)
    print(f"  Kaydedildi: {out_path}")

    section("6. GL_q(2|1) graded Yang-Baxter doğrulaması")
    summary = summarize_GLq21_ybe()
    print("  R boyutu:", summary["R_shape"])
    print("  Üçlü tensör uzayı boyutu:", summary["triple_tensor_shape"])
    print("  R nonzero entry sayısı:", summary["nonzero_entries_R"])
    print("  Graded YBE sağlanıyor mu:", summary["residual_is_zero"])


if __name__ == "__main__":
    main()
