#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
YTÜ Bitirme Çalışması posteri — resmî şablona (tez-poster-sablonu.24.05.24_0.pptx)
sadık kalarak doldurulur ve ZENGİNLEŞTİRİLİR.

Şablon korunur: 70x90 cm, logo + başlık, ÖZET kutusu, iki sütunlu gövde, KAYNAKÇA.
Sütunların alt boş bölgeleri; algoritma kutusu, kısa kod kutuları, matematik
bağıntı kutusu, "Doğrulanan Yapılar" tablosu, vurgu kutusu, yeniden
üretilebilirlik kutusu, küçültülmüş figürler ve figür açıklamaları ile doldurulur.

Çıktı: poster/Quantum Grup Yapıları - YTU Poster.pptx (+ best-effort PDF)
"""
import os, re, shutil, zipfile, subprocess
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch

HERE = os.path.dirname(os.path.abspath(__file__))
TEMPLATE = os.path.expanduser("~/Downloads/tez-poster-sablonu.24.05.24_0.pptx")
WORK = os.path.join(HERE, "_ytu_build")
FIGDIR = os.path.join(HERE, "figures_ytu")
OUT_PPTX = os.path.join(HERE, "Quantum Grup Yapıları - YTU Poster.pptx")

CM = 360000  # EMU / cm
NAVY = "1F3864"
BLUE = "2E5496"
GREY = "595959"
LGREY = "D9D9D9"
CODEBG = "F3F4F8"
MATHBG = "EAF1FB"
REPRBG = "F1F5FA"
WHITE = "FFFFFF"

def cm(v):  # cm -> EMU
    return int(round(v * CM))

# ---------------------------------------------------------------------------
# FİGÜRLER (matplotlib)
# ---------------------------------------------------------------------------
NAVY_H, BLUE_H, GREY_H, LGREY_H = "#1F3864", "#2E5496", "#595959", "#D9D9D9"

def _save(fig, name):
    os.makedirs(FIGDIR, exist_ok=True)
    p = os.path.join(FIGDIR, name)
    fig.savefig(p, dpi=300, bbox_inches="tight", pad_inches=0.05, facecolor="white")
    plt.close(fig)
    return p

def fig_flow():
    fig, ax = plt.subplots(figsize=(13, 4.4))
    ax.set_xlim(0, 13); ax.set_ylim(0, 4.4); ax.axis("off")
    steps = ["Cebirsel\nbağıntı", "Sonlu boyutlu\ntemsil", "Matris\nmodeli",
             "Kalıntı\nmatrisi", "Sembolik\nsadeleştirme", "pytest ile\ndoğrulama"]
    row_y = [2.95, 0.95]; box_w, box_h, gap = 3.3, 1.35, 0.8; centers = []
    for i, s in enumerate(steps):
        r, c = i // 3, i % 3
        x, y = 0.45 + c * (box_w + gap), row_y[r]
        fc = NAVY_H if i in (0, 5) else "white"
        tc = "white" if i in (0, 5) else NAVY_H
        ax.add_patch(FancyBboxPatch((x, y), box_w, box_h,
                     boxstyle="round,pad=0.02,rounding_size=0.18",
                     linewidth=2.2, edgecolor=NAVY_H, facecolor=fc))
        ax.text(x + box_w/2, y + box_h/2, s, ha="center", va="center",
                fontsize=15, color=tc, fontweight="bold")
        centers.append((x, y, box_w, box_h))
    def arrow(p1, p2, ls="-"):
        ax.add_patch(FancyArrowPatch(p1, p2, arrowstyle="-|>", mutation_scale=22,
                     linewidth=2.2, color=BLUE_H, linestyle=ls))
    for r in range(2):
        for c in range(2):
            i = r*3 + c; x, y, w, h = centers[i]
            arrow((x+w, y+h/2), (centers[i+1][0], y+h/2))
    x3, y3, w3, h3 = centers[2]; x4, y4, w4, h4 = centers[3]
    ax.add_patch(FancyArrowPatch((x3+w3/2, y3), (x4+w4/2, y4+h4),
                 arrowstyle="-|>", mutation_scale=22, linewidth=2.2,
                 color=BLUE_H, linestyle=(0, (4, 2))))
    return _save(fig, "fig_flow.png")

def fig_weight():
    fig, ax = plt.subplots(figsize=(9, 4.6)); n = 2; xs = list(range(n+1))
    labels = [r"$q^{%d}$" % (n-2*k) if (n-2*k) != 0 else r"$q^{0}$" for k in xs]
    yl = 1.0; ax.set_xlim(-0.8, n+0.8); ax.set_ylim(0, 2.4); ax.axis("off")
    ax.plot([-0.4, n+0.4], [yl, yl], color=GREY_H, lw=1.4, zorder=1)
    for k in xs:
        ax.scatter([k], [yl], s=620, color=NAVY_H, zorder=3)
        ax.text(k, yl, r"$v_{%d}$" % k, ha="center", va="center", color="white",
                fontsize=14, fontweight="bold", zorder=4)
        ax.text(k, yl-0.42, labels[k], ha="center", va="center", color=NAVY_H, fontsize=16)
    for k in range(n):
        ax.annotate("", xy=(k+1, yl+0.16), xytext=(k, yl+0.16),
                    arrowprops=dict(arrowstyle="-|>", color=BLUE_H, lw=2.0,
                                    connectionstyle="arc3,rad=-0.35"))
        ax.annotate("", xy=(k, yl-0.16), xytext=(k+1, yl-0.16),
                    arrowprops=dict(arrowstyle="-|>", color="#B05A1C", lw=2.0,
                                    connectionstyle="arc3,rad=-0.35"))
    ax.text(0.5, yl+0.62, r"$F$", color=BLUE_H, fontsize=17, ha="center")
    ax.text(0.5, yl-0.66, r"$E$", color="#B05A1C", fontsize=17, ha="center")
    ax.text(n/2.0, 2.18, r"$V_2$ temsili — $K\,v_k=q^{\,n-2k}v_k$", ha="center",
            va="center", fontsize=15, color=NAVY_H, fontweight="bold")
    return _save(fig, "fig_weight.png")

def fig_braid():
    fig, axes = plt.subplots(1, 3, figsize=(10, 4.3),
                             gridspec_kw=dict(width_ratios=[1, 0.18, 1]))
    def braid(ax, order):
        ax.set_xlim(0, 3); ax.set_ylim(0, 6); ax.axis("off"); cols = [0.5, 1.5, 2.5]
        for c in cols:
            ax.plot([c, c], [0, 6], color=LGREY_H, lw=8, solid_capstyle="round", zorder=1)
        for (a, b), y in zip(order, [4.7, 3.0, 1.3]):
            ca, cb = cols[a], cols[b]
            ax.plot([ca, cb], [y-0.55, y+0.55], color=NAVY_H, lw=6, solid_capstyle="round", zorder=3)
            ax.plot([cb, ca], [y-0.55, y+0.55], color=BLUE_H, lw=6, solid_capstyle="round", zorder=2)
            ax.add_patch(plt.Circle(((ca+cb)/2, y), 0.16, color="white", zorder=4, ec=NAVY_H, lw=1.5))
        for i, c in enumerate(cols):
            ax.text(c, -0.45, str(i+1), ha="center", va="center", fontsize=13, color=GREY_H)
    braid(axes[0], [(0, 1), (0, 2), (1, 2)])
    axes[1].axis("off"); axes[1].text(0.5, 0.5, "=", ha="center", va="center", fontsize=40, color=NAVY_H)
    braid(axes[2], [(1, 2), (0, 2), (0, 1)])
    axes[0].set_title(r"$R_{12}R_{13}R_{23}$", fontsize=15, color=NAVY_H)
    axes[2].set_title(r"$R_{23}R_{13}R_{12}$", fontsize=15, color=NAVY_H)
    fig.suptitle("Kuantum Yang–Baxter denklemi", fontsize=15, color=NAVY_H, fontweight="bold", y=1.02)
    return _save(fig, "fig_braid.png")

# ---------------------------------------------------------------------------
# XML yardımcıları
# ---------------------------------------------------------------------------
def esc(t):
    return t.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")

def heading(text, sz=2800, align="l"):
    return (f'<a:p><a:pPr algn="{align}"><a:lnSpc><a:spcPct val="100000"/></a:lnSpc>'
            f'<a:spcBef><a:spcPts val="600"/></a:spcBef></a:pPr><a:r>'
            f'<a:rPr lang="tr-TR" sz="{sz}" b="1" dirty="0"><a:solidFill>'
            f'<a:schemeClr val="accent1"><a:lumMod val="50000"/></a:schemeClr>'
            f'</a:solidFill></a:rPr><a:t>{esc(text)}</a:t></a:r></a:p>')

def body(text, sz=2000, align="just", bold=False, color=None, center=False, line=110):
    al = "ctr" if center else align
    b = ' b="1"' if bold else ''
    fill = f'<a:solidFill><a:srgbClr val="{color}"/></a:solidFill>' if color else ''
    return (f'<a:p><a:pPr algn="{al}"><a:lnSpc><a:spcPct val="{line}000"/></a:lnSpc></a:pPr>'
            f'<a:r><a:rPr lang="tr-TR" sz="{sz}"{b} dirty="0">{fill}</a:rPr>'
            f'<a:t>{esc(text)}</a:t></a:r></a:p>')

def bullet(text, sz=2000):
    return (f'<a:p><a:pPr marL="285750" indent="-285750" algn="just">'
            f'<a:lnSpc><a:spcPct val="105000"/></a:lnSpc>'
            f'<a:spcBef><a:spcPts val="300"/></a:spcBef>'
            f'<a:buFont typeface="Arial"/><a:buChar char="&#8226;"/></a:pPr>'
            f'<a:r><a:rPr lang="tr-TR" sz="{sz}" dirty="0"/><a:t>{esc(text)}</a:t></a:r></a:p>')

def replace_txbody(xml, shape_name, paragraphs, autofit=True):
    pat = re.compile(r'(name="' + re.escape(shape_name) + r'".*?<p:txBody>)(.*?)(</p:txBody>)', re.S)
    m = pat.search(xml)
    if not m:
        raise RuntimeError("shape not found: " + shape_name)
    head, inner, tail = m.group(1), m.group(2), m.group(3)
    pre_m = re.search(r'^(.*?)(<a:p>)', inner, re.S)
    pre = pre_m.group(1) if pre_m else '<a:bodyPr/><a:lstStyle/>'
    if not autofit:
        pre = pre.replace('<a:spAutoFit/>', '<a:noAutofit/>')
    return xml[:m.start()] + head + pre + "".join(paragraphs) + tail + xml[m.end():]

# --- şekil üreticileri --------------------------------------------------------
_id = [200]
def nid():
    _id[0] += 1
    return _id[0]

def pic_shape(rid, x, y, cx, cy, name="fig"):
    return (f'<p:pic><p:nvPicPr><p:cNvPr id="{nid()}" name="{name}"/>'
            f'<p:cNvPicPr><a:picLocks noChangeAspect="1"/></p:cNvPicPr><p:nvPr/></p:nvPicPr>'
            f'<p:blipFill><a:blip r:embed="{rid}"/><a:stretch><a:fillRect/></a:stretch></p:blipFill>'
            f'<p:spPr><a:xfrm><a:off x="{x}" y="{y}"/><a:ext cx="{cx}" cy="{cy}"/></a:xfrm>'
            f'<a:prstGeom prst="rect"><a:avLst/></a:prstGeom></p:spPr></p:pic>')

def _para(text, sz=1800, bold=False, color=None, mono=False, align="l",
          line=104, spc_before=0, italic=False, num=None):
    fill = f'<a:solidFill><a:srgbClr val="{color}"/></a:solidFill>' if color else ''
    latin = '<a:latin typeface="Consolas" pitchFamily="49" charset="0"/>' if mono else ''
    b = ' b="1"' if bold else ''
    it = ' i="1"' if italic else ''
    pPr_extra = ''
    if num is not None:
        pPr_extra = (f'<a:spcBef><a:spcPts val="300"/></a:spcBef>'
                     f'<a:buFont typeface="+mj-lt"/>'
                     f'<a:buAutoNum type="arabicPeriod"/>')
        marl = ' marL="285750" indent="-285750"'
    else:
        marl = ''
        if spc_before:
            pPr_extra = f'<a:spcBef><a:spcPts val="{spc_before}"/></a:spcBef>'
    return (f'<a:p><a:pPr{marl} algn="{align}"><a:lnSpc><a:spcPct val="{line}000"/></a:lnSpc>'
            f'{pPr_extra}</a:pPr><a:r><a:rPr lang="tr-TR" sz="{sz}"{b}{it} dirty="0">'
            f'{fill}{latin}</a:rPr><a:t>{esc(text)}</a:t></a:r></a:p>')

def box_shape(x, y, cx, cy, paras, fill=None, line_col=NAVY, rounded=True,
              anchor="t", round_amt=3600, name="box", lIns=110000, tIns=70000):
    geom = ('<a:prstGeom prst="roundRect"><a:avLst><a:gd name="adj" '
            f'fmla="val {round_amt}"/></a:avLst></a:prstGeom>') if rounded else \
           '<a:prstGeom prst="rect"><a:avLst/></a:prstGeom>'
    fillxml = f'<a:solidFill><a:srgbClr val="{fill}"/></a:solidFill>' if fill else '<a:noFill/>'
    lnxml = f'<a:ln w="12700"><a:solidFill><a:srgbClr val="{line_col}"/></a:solidFill></a:ln>' if line_col else '<a:ln><a:noFill/></a:ln>'
    return (f'<p:sp><p:nvSpPr><p:cNvPr id="{nid()}" name="{name}"/><p:cNvSpPr/><p:nvPr/></p:nvSpPr>'
            f'<p:spPr><a:xfrm><a:off x="{x}" y="{y}"/><a:ext cx="{cx}" cy="{cy}"/></a:xfrm>'
            f'{geom}{fillxml}{lnxml}</p:spPr>'
            f'<p:txBody><a:bodyPr wrap="square" lIns="{lIns}" tIns="{tIns}" rIns="{lIns}" '
            f'bIns="{tIns}" anchor="{anchor}" rtlCol="0"><a:noAutofit/></a:bodyPr>'
            f'<a:lstStyle/>{"".join(paras)}</p:txBody></p:sp>')

def caption_box(x, y, cx, cy, text):
    return box_shape(x, y, cx, cy,
                     [_para(text, sz=1600, color=GREY, italic=True, align="just", line=104)],
                     fill=None, line_col=None, rounded=False, anchor="t",
                     lIns=40000, tIns=20000, name="caption")

def code_box(x, y, cx, cy, caption, code_lines):
    paras = [_para(caption, sz=1600, bold=True, color=NAVY, line=100, align="l")]
    for ln in code_lines:
        paras.append(_para(ln if ln else " ", sz=1600, mono=True, color="22272E",
                           align="l", line=104))
    return box_shape(x, y, cx, cy, paras, fill=CODEBG, line_col=LGREY,
                     round_amt=2400, anchor="t", name="code", lIns=120000, tIns=70000)

def table_frame(x, y, cx, rows, col_w, center_cols=(1,), rh_cm=1.6, sz=1600):
    """Basit DrawingML tablosu (graphicFrame)."""
    rh = cm(rh_cm)
    grid = "".join(f'<a:gridCol w="{w}"/>' for w in col_w)
    trs = []
    for ri, row in enumerate(rows):
        header = (ri == 0)
        cells = []
        for ci, val in enumerate(row):
            if header:
                fillc, txt_c, b = NAVY, WHITE, ' b="1"'
            else:
                fillc, txt_c, b = (CODEBG if ri % 2 else WHITE), "22272E", ''
            algn = "ctr" if (header or ci in center_cols) else "l"
            cells.append(
                f'<a:tc><a:txBody><a:bodyPr/><a:lstStyle/>'
                f'<a:p><a:pPr algn="{algn}"/><a:r><a:rPr lang="tr-TR" sz="{sz}"{b} dirty="0">'
                f'<a:solidFill><a:srgbClr val="{txt_c}"/></a:solidFill></a:rPr>'
                f'<a:t>{esc(val)}</a:t></a:r></a:p></a:txBody>'
                f'<a:tcPr marL="45720" marR="45720" marT="20000" marB="20000" anchor="ctr">'
                f'<a:solidFill><a:srgbClr val="{fillc}"/></a:solidFill></a:tcPr></a:tc>')
        trs.append(f'<a:tr h="{rh}">{"".join(cells)}</a:tr>')
    return (f'<p:graphicFrame><p:nvGraphicFramePr><p:cNvPr id="{nid()}" name="tablo"/>'
            f'<p:cNvGraphicFramePr/><p:nvPr/></p:nvGraphicFramePr>'
            f'<p:xfrm><a:off x="{x}" y="{y}"/><a:ext cx="{cx}" cy="{rh*len(rows)}"/></p:xfrm>'
            f'<a:graphic><a:graphicData uri="http://schemas.openxmlformats.org/drawingml/2006/table">'
            f'<a:tbl><a:tblPr firstRow="1" bandRow="1"/><a:tblGrid>{grid}</a:tblGrid>'
            f'{"".join(trs)}</a:tbl></a:graphicData></a:graphic></p:graphicFrame>')

def mini_flow_paras(steps):
    txt = "  →  ".join(steps)
    return [_para(txt, sz=1600, bold=True, color=BLUE, align="ctr", line=110)]

def vflow_paras(steps, sz=1700):
    """Dikey akış: her adım ortalı, aralarında ↓ oku."""
    out = []
    for i, s in enumerate(steps):
        if i:
            out.append(_para("↓", sz=sz, bold=True, color=BLUE, align="ctr", line=100))
        out.append(_para(s, sz=sz, bold=True, color=NAVY, align="ctr", line=100))
    return out

# ---------------------------------------------------------------------------
# ANA METİN İÇERİĞİ (sütun gövdeleri)
# ---------------------------------------------------------------------------
def header_paras():
    def line(t, sz):
        return (f'<a:p><a:pPr algn="ctr"><a:lnSpc><a:spcPct val="100000"/></a:lnSpc></a:pPr>'
                f'<a:r><a:rPr lang="tr-TR" altLang="tr-TR" sz="{sz}" b="1" dirty="0">'
                f'<a:solidFill><a:schemeClr val="accent1"><a:lumMod val="50000"/></a:schemeClr>'
                f'</a:solidFill><a:latin typeface="Calibri"/><a:cs typeface="Calibri"/></a:rPr>'
                f'<a:t>{esc(t)}</a:t></a:r></a:p>')
    return [line("MATEMATİK BÖLÜMÜ · Haziran 2026", 2800),
            line("QUANTUM GRUP YAPILARININ PYTHON ORTAMINDA MODELLENMESİ", 3200),
            line("Taha Berk TEREKLİ — Öğrenci No: 22025083", 2400),
            line("Danışman: Prof. Dr. Salih ÇELİK", 2400)]

def ozet_paras():
    h = ('<a:p><a:pPr algn="ctr"><a:lnSpc><a:spcPct val="100000"/></a:lnSpc></a:pPr>'
         '<a:r><a:rPr lang="tr-TR" sz="3000" b="1" dirty="0"/><a:t>ÖZET</a:t></a:r></a:p>')
    txt = ("Bu çalışma, Drinfeld–Jimbo kuantum grubu U_q(sl₂) ve GL_q(2|1) kuantum "
           "süpergrubu için temel cebirsel ve temsil-teorik yapıları Python/SymPy "
           "ortamında modeller. Tanımlayıcı bağıntılar, Hopf cebiri yapısı, tensör "
           "çarpımları, Clebsch–Gordan ayrışımı, R-matrisi ve Yang–Baxter tipi "
           "bağıntılar sembolik olarak doğrulanmıştır. Yöntem, cebirsel eşitlikleri "
           "sonlu boyutlu temsiller üzerinde matris eşitliklerine dönüştürmeye ve "
           "elde edilen kalıntı matrislerinin sembolik olarak sıfır olup olmadığını "
           "test etmeye dayanır. Böylece kuantum grup hesapları açık kaynaklı, test "
           "edilebilir ve yeniden üretilebilir bir Python altyapısına taşınmıştır.")
    return [h, body(txt, sz=2000, align="just", line=115)]

def left_paras():
    p = [heading("1. Amaç", 2800)]
    p.append(body("Kuantum grup teorisindeki cebirsel bağıntıların bilgisayar "
                  "destekli sembolik hesaplama ile doğrulanabileceğini göstermek:",
                  sz=1900, align="just", line=110))
    for b in [
        "U_q(sl₂) kuantum grubunun sonlu boyutlu temsillerini açık matrislerle kurmak.",
        "Tanımlayıcı bağıntıları ve Hopf cebiri aksiyomlarını sembolik doğrulamak.",
        "Tensör çarpımı ve Clebsch–Gordan ayrışımını q-deforme katsayılarla hesaplamak.",
        "R-matrisi ve kuantum Yang–Baxter denklemini test etmek.",
        "GL_q(2|1) için graded Yang–Baxter denklemini süper permütasyonla doğrulamak.",
        "Tüm hesaplamaları test edilebilir ve yeniden üretilebilir hâle getirmek.",
    ]:
        p.append(bullet(b, sz=1900))
    p.append(heading("2. Teorik Arka Plan", 2800))
    p.append(body("Kuantum gruplar, klasik Lie cebirlerinin evrensel sarmalayıcı "
                  "cebirlerinin q-parametresi boyunca deformasyonlarıdır. Temel "
                  "örnek U_q(sl₂); E, F, K, K⁻¹ üreteçleriyle tanımlanan bir Hopf "
                  "cebiridir. Hopf yapısı temsillerin tensör çarpımını tanımlar. "
                  "Yang–Baxter denklemi ise R-matrisleri aracılığıyla kuantum "
                  "gruplar, örgü yapıları ve integrallenebilir sistemler arasında "
                  "temel bir bağlantı kurar. GL_q(2|1) ise graded bir kuantum "
                  "süpergruptur.", sz=1900, line=110))
    # 3, 4. bölümler ve sağ sütundaki 6–11. bölümler aşağıdaki başlıklı kutulara
    # (Stack) yerleştirilir; bölüm numaralandırması korunur.
    return p

def right_paras():
    p = [heading("5. Hesaplamalı Model ve Yazılım Mimarisi", 2800)]
    p.append(body("Yazılım, modüler bir Python paketi olarak tasarlanmıştır. Her "
                  "matematiksel yapı ayrı bir modülde modellenmiş ve ilgili "
                  "doğrulamalar pytest testleriyle ilişkilendirilmiştir. Aşağıdaki "
                  "modül tablosu paketin mimarisini özetler.", sz=1900, line=110))
    return p

def kaynakca_paras():
    h = ('<a:p><a:pPr algn="ctr"><a:lnSpc><a:spcPct val="100000"/></a:lnSpc></a:pPr>'
         '<a:r><a:rPr lang="tr-TR" sz="3000" b="1" dirty="0"/><a:t>KAYNAKÇA</a:t></a:r></a:p>')
    refs = [
        "[1] Drinfeld, V. G. (1986). “Quantum Groups”, Proc. Int. Congress of Mathematicians, Berkeley.",
        "[2] Jimbo, M. (1985). “A q-difference Analogue of U(g) and the Yang–Baxter Equation”, Lett. Math. Phys. 10, 63–69.",
        "[3] Çelik, S., Çelik, S. A. (2021). “A New Quantum Supergroup and its Gauss Decomposition”, Rep. Math. Phys. 88(2), 259–272.",
    ]
    return [h] + [body(r, sz=2000, align="just", line=105) for r in refs]

# ---------------------------------------------------------------------------
# EK KUTULAR / FİGÜRLER — yerleşim
# ---------------------------------------------------------------------------
class Stack:
    """Bir alt-sütunda şekilleri ardışık (üstten alta) yerleştirir.

    Önce tüm öğeler/aralıklar toplanır; render(end_cm) çağrısında, kalan boşluk
    (slack) aralıklara orantılı dağıtılarak sütun çerçevesi boyunca dengeli
    biçimde doldurulur (dikey yaslama). Böylece kutular içeriklerine göre
    boyutlanır ve sütun altı boş "format hatası" görünümü engellenir.
    """
    def __init__(self, x, w, y0_cm):
        self.x, self.w, self.y0 = x, w, cm(y0_cm)
        self.items = []   # ('shape', h_emu, fn(y)) | ('gap', g_emu)
    def box(self, h_cm, paras, **kw):
        self.items.append(('s', cm(h_cm),
            lambda y, p=paras, k=kw, h=h_cm: box_shape(self.x, y, self.w, cm(h), p, **k)))
    def code(self, h_cm, caption, lines):
        self.items.append(('s', cm(h_cm),
            lambda y, c=caption, l=lines, h=h_cm: code_box(self.x, y, self.w, cm(h), c, l)))
    def table(self, rows, col_w, center_cols=(1,), rh_cm=1.6, sz=1600):
        h = cm(rh_cm) * len(rows)
        self.items.append(('s', h,
            lambda y, r=rows, cw=col_w, cc=center_cols, rh=rh_cm, s=sz:
                table_frame(self.x, y, sum(cw), r, cw, center_cols=cc, rh_cm=rh, sz=s)))
    def fig(self, rid, aspect, width_cm=None, name="fig"):
        w = cm(width_cm) if width_cm else self.w
        h = int(w / aspect)
        x = self.x + (self.w - w) // 2
        self.items.append(('s', h, lambda y, r=rid, xx=x, ww=w, hh=h, n=name:
                           pic_shape(r, xx, y, ww, hh, n)))
    def caption(self, h_cm, text):
        self.items.append(('s', cm(h_cm),
            lambda y, t=text, h=h_cm: caption_box(self.x, y, self.w, cm(h), t)))
    def gap(self, g_cm):
        self.items.append(('g', cm(g_cm)))
    def render(self, end_cm=None):
        fixed = sum(h for k, h, *r in self.items if k == 's')
        base_gap = sum(g for k, g in ((it[0], it[1]) for it in self.items) if k == 'g')
        slack = 0
        if end_cm is not None:
            slack = max(0, cm(end_cm) - self.y0 - fixed - base_gap)
        out, y = [], self.y0
        for it in self.items:
            if it[0] == 's':
                out.append(it[2](y)); y += it[1]
            else:
                g = it[1]
                if base_gap > 0:
                    g += int(slack * it[1] / base_gap)
                y += g
        return out


def build_extras():
    """Sütunların boş alt bölgelerine yerleştirilecek tüm ek şekiller.

    SOL : 3. Temel Matematiksel Yapılar, 4. Yöntem (+kod, figürler 1–2)
    SAĞ : 5. modül tablosu, 6. Clebsch–Gordan, 7. R-matrisi (+kod, figür 3),
          8. GL_q(2|1) graded (figür 4), 9. sonuç tablosu, 10. Katkı, 11. Sonuç
    """
    asp_flow, asp_weight, asp_braid = 13/4.4, 9/4.6, 10/4.3
    shapes = []

    # iç alt-sütun konumları
    L1x, LW1 = cm(3.15), cm(14.4)        # SOL-sol
    L2x, LW2 = cm(18.55), cm(14.7)       # SOL-sağ
    R1x, RW1 = cm(36.55), cm(14.8)       # SAĞ-sol
    R2x, RW2 = cm(52.0), cm(15.0)        # SAĞ-sağ

    LY = 38.5       # sol prose (1-2) bitişi
    RY = 30.5       # sağ prose (5 giriş) bitişi
    LEFT_END = 84.0 # sol alt-sütunların hedef bitişi (çerçeve dibi ~89)
    RIGHT_END = 80.0  # sağ alt-sütunların hedef bitişi (KAYNAKÇA ~82.3)

    # ====================== SOL SÜTUN =====================================
    # ----- SOL-sol: 3. Temel Matematiksel Yapılar + 4. Yöntem + kod + 11 --
    sLL = Stack(L1x, LW1, LY)
    sLL.box(9.0, [
        _para("3. Temel Matematiksel Yapılar", sz=2000, bold=True, color=NAVY, line=100, align="ctr"),
        _para("Vₙ temsili (n+1)-boyutludur; v₀,…,vₙ bazında:", sz=1600, italic=True,
              color=GREY, align="ctr", line=104, spc_before=200),
        _para("K · vₖ = qⁿ⁻²ᵏ vₖ", sz=2000, bold=True, color=NAVY, align="ctr", line=120, spc_before=300),
        _para("F · vₖ = vₖ₊₁", sz=2000, bold=True, color=NAVY, align="ctr", line=120),
        _para("E · vₖ = [k]_q [n−k+1]_q vₖ₋₁", sz=2000, bold=True, color=NAVY, align="ctr", line=120),
        _para("[n]_q = (qⁿ − q⁻ⁿ) / (q − q⁻¹)", sz=2000, bold=True, color=NAVY, align="ctr", line=120),
        _para("Bu q-tamsayı katsayıları, klasik sl₂ temsilindeki tamsayı "
              "katsayıların q-deforme karşılıklarıdır.", sz=1600, italic=True,
              color=GREY, align="just", line=104, spc_before=300),
    ], fill=MATHBG, line_col=BLUE, name="matematik")
    sLL.gap(1.2)
    sLL.box(9.0, [
        _para("4. Yöntem — Sıfır-Kalıntı Doğrulaması", sz=2000, bold=True, color=NAVY, line=100),
        _para("Her bağıntı X = Y matris eşitliğine indirgenir; kalıntı Z = X − Y "
              "kurulup tüm girdileri SymPy ile sadeleştirilir:",
              sz=1700, align="just", line=106, spc_before=200),
        _para("Temsil matrislerini oluştur.", sz=1800, num=True),
        _para("Bağıntıyı X = Y biçiminde yaz.", sz=1800, num=True),
        _para("Kalıntı matrisini hesapla: Z = X − Y.", sz=1800, num=True),
        _para("Her girdiyi simplify ile sadeleştir.", sz=1800, num=True),
        _para("Tüm girdiler 0 ise bağıntı doğrulanmıştır.", sz=1800, num=True),
    ], fill="FFFFFF", line_col=NAVY, name="yontem")
    sLL.gap(1.2)
    sLL.code(6.0, "Kod 1 — Sıfır-kalıntı kontrolü",
             ["def is_zero_matrix(M):", "    return all(", "        simplify(x) == 0",
              "        for x in M)", "", "ok = is_zero_matrix(lhs - rhs)"])
    sLL.gap(1.2)
    sLL.box(8.0, [
        _para("11. Sonuç ve Gelecek Çalışmalar", sz=2000, bold=True, color=NAVY, line=100),
        _para("Python/SymPy tabanlı yapı; temsil teorisi, R-matrisi, Yang–Baxter "
              "ve kuantum süpergrup doğrulamaları için yeniden üretilebilir bir "
              "ortam sunar. Gelecek çalışmalar:", sz=1700, align="just", line=106, spc_before=200),
        _para("Jones polinomu ve düğüm değişmezleri.", sz=1700, num=True),
        _para("Daha yüksek rank kuantum gruplara genelleme.", sz=1700, num=True),
        _para("Birim kök durumlarının incelenmesi.", sz=1700, num=True),
        _para("Kristal tabanların kapsamlı modellenmesi.", sz=1700, num=True),
    ], fill="FFFFFF", line_col=GREY, name="sonuc")
    shapes += sLL.render(LEFT_END)

    # ----- SOL-sağ: figürler 1–2 + açıklamalar + 6. Clebsch + klasik limit -
    sLR = Stack(L2x, LW2, LY)
    sLR.fig("rId10", asp_flow, name="fig_flow")
    sLR.gap(0.3)
    sLR.caption(4.4, "Şekil 1. Sıfır-kalıntı doğrulama akışı: cebirsel bağıntıdan "
                     "temsil ve kalıntı matrisine, oradan otomatik pytest "
                     "doğrulamasına uzanan adımlar.")
    sLR.gap(1.0)
    sLR.fig("rId11", asp_weight, width_cm=12.6, name="fig_weight")
    sLR.gap(0.3)
    sLR.caption(5.6, "Şekil 2. V₂ temsilinde K operatörü ağırlıkları q², q⁰, q⁻² "
                     "olarak ayırır. F operatörü vektörleri aşağı taşırken E "
                     "operatörü q-deforme katsayılarla geri taşır; bu, klasik sl₂ "
                     "temsilinin q-deforme karşılığıdır.")
    sLR.gap(1.0)
    sLR.box(9.0, [
        _para("6. Clebsch–Gordan Ayrışımı", sz=2000, bold=True, color=NAVY, line=100, align="ctr"),
        _para("Eş-çarpım sayesinde Vₘ ⊗ Vₙ yine bir temsildir; en yüksek ağırlık "
              "vektörleri sembolik bulunur:", sz=1600, italic=True,
              color=GREY, align="ctr", line=104, spc_before=200),
        _para("V₁ ⊗ V₁ ≅ V₂ ⊕ V₀", sz=2000, bold=True, color=NAVY, align="ctr", line=118, spc_before=300),
        _para("V₂ ⊗ V₂ ≅ V₄ ⊕ V₂ ⊕ V₀", sz=2000, bold=True, color=NAVY, align="ctr", line=118),
        _para("V₃ ⊗ V₂ ≅ V₅ ⊕ V₃ ⊕ V₁", sz=2000, bold=True, color=NAVY, align="ctr", line=118),
        _para("Her aday vektör E · v = 0 ve K · v = qᵏ v koşullarıyla denetlenir.",
              sz=1600, italic=True, color=GREY, align="just", line=104, spc_before=300),
    ], fill=MATHBG, line_col=BLUE, name="clebsch")
    sLR.gap(1.0)
    sLR.box(5.2, [
        _para("q → 1 (Klasik Limit)", sz=1900, bold=True, color=NAVY, line=100),
        _para("q → 1 alındığında [n]_q → n olur ve tüm bağıntılar klasik sl₂ "
              "yapısına indirgenir.", sz=1800, align="just", line=110, spc_before=300),
    ], fill="FFFFFF", line_col=GREY, name="limit")
    shapes += sLR.render(LEFT_END)

    # ====================== SAĞ SÜTUN =====================================
    # ----- SAĞ-sol: 5. modül tablosu + q-tamsayı kodu, 9. sonuç tablosu, 10
    sRL = Stack(R1x, RW1, RY)
    sRL.box(1.5, [_para("Yazılım Mimarisi — Modüller", sz=1800, bold=True,
                        color=NAVY, line=100, align="l")],
            fill=None, line_col=None, rounded=False, lIns=20000, tIns=10000, name="modul-baslik")
    sRL.table([
        ["Modül", "Görev"],
        ["representations.py", "Vₙ temsillerinin kurulması"],
        ["relations.py", "Tanımlayıcı bağıntıların doğrulanması"],
        ["tensor.py", "Tensör çarpımı, Clebsch–Gordan"],
        ["r_matrix.py", "R-matrisi ve Yang–Baxter"],
        ["supergroup_gl21.py", "GL_q(2|1) ve graded YBE"],
        ["tests/", "pytest tabanlı doğrulama"],
    ], [cm(5.5), cm(9.3)], center_cols=(), rh_cm=1.4)
    sRL.gap(1.0)
    sRL.code(6.0, "Kod 2 — q-tamsayı fonksiyonu",
             ["def q_integer(n, q):", "    if n == 0:", "        return 0",
              "    return simplify(", "        (q**n - q**-n)", "        / (q - q**-1))"])
    sRL.gap(1.0)
    sRL.box(1.5, [_para("9. Doğrulanan Sonuçlar", sz=1800, bold=True,
                        color=NAVY, line=100, align="l")],
            fill=None, line_col=None, rounded=False, lIns=20000, tIns=10000, name="sonuc-baslik")
    sRL.table([
        ["Yapı", "Kapsam", "Sonuç"],
        ["U_q(sl₂) bağıntıları", "V₀–V₄", "Doğrulandı"],
        ["Hopf aksiyomları", "Temsil", "Doğrulandı"],
        ["V₁ ⊗ V₁", "4 boyut", "V₂ ⊕ V₀"],
        ["R-matrisi", "4×4", "QYBE sağlandı"],
        ["GL_q(2|1) R", "9×9", "Kodlandı"],
        ["Graded YBE", "27×27", "729 → 0"],
        ["Test altyapısı", "pytest", "Üretilebilir"],
    ], [cm(6.0), cm(3.4), cm(5.4)], rh_cm=1.4)
    sRL.gap(1.0)
    sRL.box(5.4, [
        _para("10. Katkı", sz=1900, bold=True, color=WHITE, line=100),
        _para("El ile uzun ve hataya açık Yang–Baxter tipi hesaplamaların; açık "
              "matrisler ve otomatik testlerle güvenilir, yeniden üretilebilir "
              "biçimde doğrulanabilir hâle getirilmesi.",
              sz=1800, color=WHITE, align="just", line=110, spc_before=300),
    ], fill=NAVY, line_col=NAVY, name="katki")
    shapes += sRL.render(RIGHT_END)

    # ----- SAĞ-sağ: 7. R-matrisi (+kod 3, figür 3), 8. graded YBE ----------
    sRR = Stack(R2x, RW2, RY)
    sRR.box(5.8, [
        _para("7. R-Matrisi ve Yang–Baxter Denklemi", sz=2000, bold=True, color=NAVY, line=100),
        _para("V₁ ⊗ V₁ üzerinde R-matrisi kurulmuş ve kuantum Yang–Baxter denklemi "
              "sembolik doğrulanmıştır:", sz=1700, align="just", line=106, spc_before=200),
        _para("R₁₂ R₁₃ R₂₃ = R₂₃ R₁₃ R₁₂", sz=2000, bold=True, color=NAVY, align="ctr",
              line=120, spc_before=300),
    ], fill="FFFFFF", line_col=NAVY, name="rmatris")
    sRR.gap(1.0)
    sRR.code(4.4, "Kod 3 — Yang–Baxter kalıntısı",
             ["Y = (R12*R13*R23", "     - R23*R13*R12)", "assert is_zero_matrix(Y)"])
    sRR.gap(1.0)
    sRR.fig("rId12", asp_braid, name="fig_braid")
    sRR.gap(0.3)
    sRR.caption(4.4, "Şekil 3. Denklemin iki tarafı farklı örgü sıralarını temsil "
                     "eder; doğrulama sonucunda iki tarafın aynı operatörü verdiği "
                     "sembolik olarak gösterilmiştir.")
    sRR.gap(1.0)
    sRR.box(12.0, [
        _para("8. GL_q(2|1) — Graded Yang–Baxter", sz=2000, bold=True, color=NAVY, line=100),
        _para("Literatürdeki 9×9 R-matrisi SymPy'de kodlanmış; parite seçimi "
              "p(e₁)=0, p(e₂)=0, p(e₃)=1 ile süper permütasyon kurulmuştur. "
              "R₁₃ yerleşimi graded işaretlerden ötürü daha hassastır.",
              sz=1700, align="just", line=106, spc_before=200),
    ] + vflow_paras(["9×9 R-matrisi", "Süper permütasyon", "R₁₂ , R₁₃ , R₂₃",
                     "27×27 kalıntı matrisi", "729 girdi → 0"], sz=1700),
        fill=REPRBG, line_col=BLUE, name="graded")
    shapes += sRR.render(RIGHT_END)
    return shapes

# ---------------------------------------------------------------------------
# MONTAJ
# ---------------------------------------------------------------------------
def build():
    print("Figürler üretiliyor...")
    fig_flow(); fig_weight(); fig_braid()
    if os.path.exists(WORK):
        shutil.rmtree(WORK)
    os.makedirs(WORK)
    with zipfile.ZipFile(TEMPLATE) as z:
        z.extractall(WORK)

    slide_path = os.path.join(WORK, "ppt", "slides", "slide1.xml")
    with open(slide_path, encoding="utf-8") as f:
        xml = f.read()

    xml = replace_txbody(xml, "Dikdörtgen 10", header_paras(), autofit=False)
    xml = xml.replace('<a:bodyPr wrap="square"><a:noAutofit/></a:bodyPr>',
                      '<a:bodyPr wrap="square" anchor="b"><a:noAutofit/></a:bodyPr>')
    xml = replace_txbody(xml, "Metin kutusu 11", ozet_paras())
    xml = replace_txbody(xml, "Metin kutusu 12", left_paras(), autofit=False)
    xml = replace_txbody(xml, "Metin kutusu 16", right_paras(), autofit=False)
    xml = replace_txbody(xml, "Metin kutusu 21", kaynakca_paras())

    media = os.path.join(WORK, "ppt", "media")
    shutil.copy(os.path.join(FIGDIR, "fig_flow.png"), os.path.join(media, "image2.png"))
    shutil.copy(os.path.join(FIGDIR, "fig_weight.png"), os.path.join(media, "image3.png"))
    shutil.copy(os.path.join(FIGDIR, "fig_braid.png"), os.path.join(media, "image4.png"))

    rels_path = os.path.join(WORK, "ppt", "slides", "_rels", "slide1.xml.rels")
    with open(rels_path, encoding="utf-8") as f:
        rels = f.read()
    add = ('<Relationship Id="rId10" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/image" Target="../media/image2.png"/>'
           '<Relationship Id="rId11" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/image" Target="../media/image3.png"/>'
           '<Relationship Id="rId12" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/image" Target="../media/image4.png"/>')
    rels = rels.replace("</Relationships>", add + "</Relationships>")
    with open(rels_path, "w", encoding="utf-8") as f:
        f.write(rels)

    extras = build_extras()
    xml = xml.replace("</p:spTree>", "".join(extras) + "</p:spTree>")
    with open(slide_path, "w", encoding="utf-8") as f:
        f.write(xml)

    if os.path.exists(OUT_PPTX):
        os.remove(OUT_PPTX)
    with zipfile.ZipFile(OUT_PPTX, "w", zipfile.ZIP_DEFLATED) as z:
        for root, _, files in os.walk(WORK):
            for fn in files:
                full = os.path.join(root, fn)
                z.write(full, os.path.relpath(full, WORK))
    print("PPTX yazıldı:", OUT_PPTX)
    return OUT_PPTX

def to_pdf(pptx):
    soffice = shutil.which("soffice") or "/Applications/LibreOffice.app/Contents/MacOS/soffice"
    if not (os.path.exists(soffice) or shutil.which("soffice")):
        print("LibreOffice yok; PDF atlandı."); return None
    try:
        subprocess.run([soffice, "--headless", "--convert-to", "pdf", "--outdir", HERE, pptx],
                       check=True, timeout=240, capture_output=True)
        pdf = os.path.splitext(pptx)[0] + ".pdf"
        if os.path.exists(pdf):
            print("PDF yazıldı:", pdf); return pdf
    except Exception as e:
        print("PDF dönüşümü başarısız:", e)
    return None

if __name__ == "__main__":
    out = build()
    to_pdf(out)
