r"""
generate_figures.py
===================

Makale (thesis) icin GERCEK hesaplardan vektor (PDF) figurleri uretir.

Bu script mevcut ``quantum_group`` paketinin public API'sini kullanir; paket
kodunu DEGISTIRMEZ. Uretilen figurler thesis.tex tarafindan \includegraphics
ile gomulur.

Cikti dosyalari (bu dizine yazilir):
  * R_gl21_structure.pdf   -- GL_q(2|1) 9x9 R-matrisinin girdi-tipi haritasi
  * ybe_products_27.pdf     -- R12 R13 R23 ve R23 R13 R12 (27x27) sifir-olmayan
                               oruntuleri + tamamen sifir olan kalinti
  * R_sl2_V1.pdf            -- U_q(sl_2) icin 4x4 R ve Rcheck yapisi

Calistirma:
    python3 thesis/figures/generate_figures.py
veya:
    make figures
"""

from __future__ import annotations

import sys
from pathlib import Path

import matplotlib

matplotlib.use("Agg")  # bassiz ortam

import matplotlib.pyplot as plt
from matplotlib.patches import Patch
import numpy as np
import sympy as sp

# Repo kokunu import yoluna ekle (script alt dizinde calissa bile)
REPO_ROOT = Path(__file__).resolve().parents[2]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

from quantum_group import (  # noqa: E402
    q,
    R_matrix_GLq21,
    R12_GLq21,
    R13_GLq21,
    R23_GLq21,
    graded_yang_baxter_residual_GLq21,
    R_matrix_V1,
    R_check_V1,
)

OUT_DIR = Path(__file__).resolve().parent

# Tutarli, sade renk paleti (ince ve temiz tasarim ile uyumlu)
COL_BG = "#f8f8f8"
COL_GRID = "#d2d2d2"
COL_ACCENT = "#3b5b92"
COL_ODD = "#8a2884"     # odd-odd / isaret vurgusu
COL_FILL = "#9bb4d8"    # sifir-olmayan girdi


# ---------------------------------------------------------------------------
# Yardimcilar
# ---------------------------------------------------------------------------

def _entry_type_grid(M: sp.Matrix):
    """9x9 (veya genel) sembolik matristeki her girdiyi tipe gore siniflar.

    Donen: (kategori indeksi matrisi, etiket listesi, renk listesi).
    """
    qs = q
    catalog = [
        (sp.Integer(0), "0", COL_BG),
        (sp.Integer(1), "1", "#cfe0f3"),
        (qs, "q", "#9bb4d8"),
        (qs**2, "q^2", "#5e82bd"),
        (sp.simplify(1 - qs**2), "1-q^2", COL_ODD),
    ]
    n_rows, n_cols = M.rows, M.cols
    grid = np.full((n_rows, n_cols), -1, dtype=int)
    for i in range(n_rows):
        for j in range(n_cols):
            e = sp.simplify(M[i, j])
            for idx, (val, _lab, _col) in enumerate(catalog):
                if sp.simplify(e - val) == 0:
                    grid[i, j] = idx
                    break
    labels = [lab for _v, lab, _c in catalog]
    colors = [c for _v, _l, c in catalog]
    return grid, labels, colors


def _nonzero_pattern(M: sp.Matrix, q_val=sp.Rational(7, 3)) -> np.ndarray:
    """Matrisin sifir-olmayan oruntusunu (0/1) sayisal q ile hizlica cikarir."""
    arr = np.array(M.subs(q, q_val)).astype(np.float64)
    return (np.abs(arr) > 1e-9).astype(int)


# ---------------------------------------------------------------------------
# Figur 1: GL_q(2|1) 9x9 R-matris yapisi
# ---------------------------------------------------------------------------

def figure_R_structure() -> Path:
    R = R_matrix_GLq21()
    grid, labels, colors = _entry_type_grid(R)
    cmap = matplotlib.colors.ListedColormap(colors)

    basis = [f"$e_{i}e_{j}$" for i in range(1, 4) for j in range(1, 4)]

    fig, ax = plt.subplots(figsize=(5.4, 5.0))
    ax.imshow(grid, cmap=cmap, vmin=0, vmax=len(colors) - 1)

    # Izgara cizgileri
    for k in range(len(basis) + 1):
        ax.axhline(k - 0.5, color=COL_GRID, linewidth=0.8)
        ax.axvline(k - 0.5, color=COL_GRID, linewidth=0.8)

    # Sifir-olmayan girdileri sembolik olarak yaz
    for i in range(9):
        for j in range(9):
            if grid[i, j] > 0:
                ax.text(j, i, f"${sp.latex(sp.simplify(R[i, j]))}$",
                        ha="center", va="center", fontsize=7.5, color="black")

    ax.set_xticks(range(9))
    ax.set_yticks(range(9))
    ax.set_xticklabels(basis, fontsize=7.5, rotation=45, ha="right")
    ax.set_yticklabels(basis, fontsize=7.5)
    ax.tick_params(length=0)
    ax.set_title(r"$GL_q(2|1)$ R-matrisi (9$\times$9): girdi tipleri", fontsize=11)

    legend = [Patch(facecolor=colors[i], edgecolor=COL_GRID, label=f"${labels[i]}$")
              for i in range(len(labels))]
    ax.legend(handles=legend, loc="upper left", bbox_to_anchor=(1.02, 1.0),
              fontsize=8, frameon=False, title="girdi")

    fig.tight_layout()
    out = OUT_DIR / "R_gl21_structure.pdf"
    fig.savefig(out, bbox_inches="tight")
    plt.close(fig)
    return out


# ---------------------------------------------------------------------------
# Figur 2: 27x27 YBE urunleri ve sifir kalinti
# ---------------------------------------------------------------------------

def figure_ybe_products() -> Path:
    R12 = R12_GLq21()
    R13 = R13_GLq21()
    R23 = R23_GLq21()

    lhs = R12 * R13 * R23
    rhs = R23 * R13 * R12

    p_lhs = _nonzero_pattern(lhs)
    p_rhs = _nonzero_pattern(rhs)

    # Kalinti SEMBOLIK olarak tam sifirdir; panelde sifir oruntusunu gosteririz
    p_res = _nonzero_pattern(graded_yang_baxter_residual_GLq21())

    panels = [
        (p_lhs, r"$R_{12}R_{13}R_{23}$"),
        (p_rhs, r"$R_{23}R_{13}R_{12}$"),
        (p_res, r"$Y(q)=R_{12}R_{13}R_{23}-R_{23}R_{13}R_{12}$"),
    ]
    cmap = matplotlib.colors.ListedColormap([COL_BG, COL_FILL])

    fig, axes = plt.subplots(1, 3, figsize=(11.5, 4.2))
    for ax, (pat, title) in zip(axes, panels):
        ax.imshow(pat, cmap=cmap, vmin=0, vmax=1)
        nz = int(pat.sum())
        ax.set_title(f"{title}\n(sifir-olmayan girdi: {nz}/729)", fontsize=9)
        ax.set_xticks([0, 8, 17, 26])
        ax.set_yticks([0, 8, 17, 26])
        ax.tick_params(labelsize=7, length=0)
        for s in ax.spines.values():
            s.set_edgecolor(COL_GRID)

    fig.suptitle(
        r"Graded Yang--Baxter: iki urun ozdes oruntu, kalinti $Y(q)\equiv 0$",
        fontsize=11)
    fig.tight_layout(rect=(0, 0, 1, 0.96))
    out = OUT_DIR / "ybe_products_27.pdf"
    fig.savefig(out, bbox_inches="tight")
    plt.close(fig)
    return out


# ---------------------------------------------------------------------------
# Figur 3: U_q(sl_2) 4x4 R ve Rcheck
# ---------------------------------------------------------------------------

def figure_R_sl2() -> Path:
    R = R_matrix_V1()
    Rc = R_check_V1()
    basis = [r"$v_0v_0$", r"$v_0v_1$", r"$v_1v_0$", r"$v_1v_1$"]

    fig, axes = plt.subplots(1, 2, figsize=(8.0, 4.0))
    for ax, (M, title) in zip(axes, [(R, r"$R$"), (Rc, r"$\check R=\tau R$")]):
        pat = _nonzero_pattern(M)
        cmap = matplotlib.colors.ListedColormap([COL_BG, COL_FILL])
        ax.imshow(pat, cmap=cmap, vmin=0, vmax=1)
        for i in range(4):
            for j in range(4):
                e = sp.simplify(M[i, j])
                if e != 0:
                    ax.text(j, i, f"${sp.latex(e)}$", ha="center", va="center",
                            fontsize=8)
        for k in range(5):
            ax.axhline(k - 0.5, color=COL_GRID, linewidth=0.8)
            ax.axvline(k - 0.5, color=COL_GRID, linewidth=0.8)
        ax.set_xticks(range(4)); ax.set_yticks(range(4))
        ax.set_xticklabels(basis, fontsize=8, rotation=45, ha="right")
        ax.set_yticklabels(basis, fontsize=8)
        ax.tick_params(length=0)
        ax.set_title(title, fontsize=11)

    fig.suptitle(r"$U_q(\mathfrak{sl}_2)$: $V_1\otimes V_1$ uzerinde R ve $\check R$",
                 fontsize=11)
    fig.tight_layout(rect=(0, 0, 1, 0.95))
    out = OUT_DIR / "R_sl2_V1.pdf"
    fig.savefig(out, bbox_inches="tight")
    plt.close(fig)
    return out


def main() -> None:
    print("Figurler uretiliyor (gercek hesaplardan)...")
    for fn in (figure_R_structure, figure_ybe_products, figure_R_sl2):
        path = fn()
        print(f"  yazildi: {path.relative_to(REPO_ROOT)}")
    print("Tamamlandi.")


if __name__ == "__main__":
    main()
