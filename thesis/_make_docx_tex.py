#!/usr/bin/env python3
"""thesis_ytu.tex -> pandoc dostu thesis_ytu_docx.tex.

DOCX tarafında Word/LibreOffice'in LaTeX sayaçlarını yeniden yorumlamasına izin
vermemek için referanslar ve teorem benzeri ortam başlıkları düz metne çevrilir.
"""
import os, re

HERE = os.path.dirname(os.path.abspath(__file__))
with open(os.path.join(HERE, "thesis_ytu.tex"), encoding="utf-8") as f:
    tex = f.read()

def _read_aux_labels():
    aux_path = os.path.join(HERE, "thesis_ytu.aux")
    labels = {}
    if not os.path.exists(aux_path):
        return labels
    with open(aux_path, encoding="utf-8") as f:
        aux = f.read()
    for m in re.finditer(r"\\newlabel\{([^{}]+)\}\{\{([^{}]+)\}", aux):
        labels[m.group(1)] = m.group(2)
    return labels

LABELS = _read_aux_labels()

def _flatten_refs(text):
    def eq_repl(m):
        key = m.group(1).strip()
        return "(%s)" % LABELS.get(key, key)

    def ref_repl(m):
        key = m.group(1).strip()
        return LABELS.get(key, key)

    text = re.sub(r"\\eqref\{([^{}]+)\}", eq_repl, text)
    text = re.sub(r"\\(?:auto|[cC])?ref\{([^{}]+)\}", ref_repl, text)
    return text

def _flatten_theorem_envs(text):
    env_names = {
        "theorem": "Teorem",
        "proposition": "Önerme",
        "lemma": "Lemma",
        "corollary": "Sonuç",
        "definition": "Tanım",
        "example": "Örnek",
        "remark": "Not",
    }
    token = re.compile(
        r"\\(?P<appendix>appendix)\b|"
        r"\\chapter(?P<star>\*)?\{(?P<title>(?:[^{}]|\{[^{}]*\})*)\}|"
        r"\\begin\{(?P<env>" + "|".join(env_names) + r")\}(?:\[(?P<opt>[^\]]+)\])?|"
        r"\\end\{(?P<endenv>" + "|".join(env_names) + r")\}"
    )
    out = []
    pos = 0
    chapter_num = 0
    theorem_num = 0
    appendix = False
    appendix_ord = 0

    for m in token.finditer(text):
        out.append(text[pos:m.start()])
        pos = m.end()

        if m.group("appendix"):
            appendix = True
            theorem_num = 0
            out.append(m.group(0))
            continue

        if m.group("title") is not None:
            if not m.group("star"):
                if appendix:
                    appendix_ord += 1
                    chapter_num = chr(ord("A") + appendix_ord - 1)
                else:
                    chapter_num += 1
                theorem_num = 0
            out.append(m.group(0))
            continue

        env = m.group("env")
        if env:
            theorem_num += 1
            label = env_names[env]
            opt = m.group("opt")
            suffix = ""
            if opt:
                suffix = " (" + opt.strip() + ")"
            out.append(r"\paragraph{%s %s.%s%s.}" % (label, chapter_num, theorem_num, suffix))
            continue

        if m.group("endenv"):
            continue

    out.append(text[pos:])
    return "".join(out)

tex = _flatten_refs(tex)
tex = _flatten_theorem_envs(tex)

# === Özel matematik makrolarını düz LaTeX'e genişlet (pandoc OMML üretebilsin) ===
# pandoc bu kullanıcı makrolarını genişletemediği için satıriçi/blok matematik
# DOCX'te BOŞ düşüyordu. Önce makro tanımlarını kaldır, sonra kullanımları aç.
tex = re.sub(
    r"^\\(?:re)?newcommand\{\\(?:Uq|sl|gfrak|K|Q|C|Z|R|GL|SL|End|id|eps|"
    r"cop|Dop|qint|qfact|qbin|Vn|hwt|Rcheck)\}.*$\n?",
    "", tex, flags=re.M)

# Argümanlı makrolar (tek seviye süslü parantez)
tex = re.sub(r"\\qfact\{([^{}]*)\}", lambda m: "[%s]_q!" % m.group(1), tex)
tex = re.sub(r"\\qint\{([^{}]*)\}",  lambda m: "[%s]_q"  % m.group(1), tex)
tex = re.sub(r"\\Vn\{([^{}]*)\}",    lambda m: "V_{%s}"  % m.group(1), tex)
tex = re.sub(r"\\qbin\{([^{}]*)\}\{([^{}]*)\}",
             lambda m: r"\left[\genfrac{}{}{0pt}{}{%s}{%s}\right]_q"
             % (m.group(1), m.group(2)), tex)

# Argümansız makrolar (harf sınırı korunur; uzun isimler önce)
_noarg = {
    "Rcheck": r"\check{R}", "Uq": r"U_q(\mathfrak{sl}_2)",
    "gfrak": r"\mathfrak{g}", "sl": r"\mathfrak{sl}",
    "Dop": r"\Delta^{\mathrm{op}}", "cop": r"\Delta", "eps": r"\varepsilon",
    "hwt": r"v_0", "End": r"\mathrm{End}", "id": r"\mathrm{id}",
    "GL": r"\mathrm{GL}", "SL": r"\mathrm{SL}",
    "K": r"\mathbb{K}", "Q": r"\mathbb{Q}", "C": r"\mathbb{C}",
    "Z": r"\mathbb{Z}", "R": r"\mathbb{R}",
}
for _name in sorted(_noarg, key=len, reverse=True):
    tex = re.sub(r"\\" + _name + r"(?![a-zA-Z])",
                 lambda m, v=_noarg[_name]: v, tex)

def _plain_inline_math(expr):
    x = expr
    repls = [
        (r"\\mathfrak\{sl\}_2", "sl2"),
        (r"\\mathfrak\{sl\}", "sl"),
        (r"\\mathfrak\{g\}", "g"),
        (r"\\mathbb\{Q\}", "Q"),
        (r"\\mathbb\{C\}", "C"),
        (r"\\mathbb\{K\}", "K"),
        (r"\\mathbb\{Z\}", "Z"),
        (r"\\mathrm\{GL\}_q", "GLq"),
        (r"\\mathrm\{id\}", "id"),
        (r"\\mathrm\{End\}", "End"),
        (r"\\check\{R\}", "Ř"),
        (r"\\Delta\^\{\\mathrm\{op\}\}", "Delta^op"),
        (r"\\Delta", "Δ"),
        (r"\\varepsilon", "ε"),
        (r"\\epsilon", "ε"),
        (r"\\tau", "τ"),
        (r"\\otimes", "⊗"),
        (r"\\times", "×"),
        (r"\\to", "→"),
        (r"\\cong", "≅"),
        (r"\\oplus", "⊕"),
        (r"\\neq", "≠"),
        (r"\\ge", "≥"),
        (r"\\le", "≤"),
        (r"\\in", "∈"),
        (r"\\infty", "∞"),
        (r"\\cdot", "·"),
        (r"\\ldots", "..."),
        (r"\\dots", "..."),
        (r"\\cdots", "⋯"),
    ]
    for old, new in repls:
        x = re.sub(old, new, x)
    x = re.sub(r"\\math(?:frak|rm|bb|cal|bf|it)\{([^{}]*)\}", r"\1", x)
    x = re.sub(r"U_q\(sl2\)", "Uq(sl2)", x)
    x = re.sub(r"GL_q", "GLq", x)
    x = re.sub(r"([A-Za-zRKVp])_\{([^{}]+)\}", r"\1\2", x)
    x = re.sub(r"([A-Za-zRKVp])_([A-Za-z0-9])", r"\1\2", x)
    x = re.sub(r"\[([^{}\]]+)\]_q", r"[\1]q", x)
    x = re.sub(r"\^\{-1\}", "^{-1}", x)
    x = re.sub(r"\^\{([^{}]+)\}", r"^\1", x)
    x = x.replace(r"\left", "").replace(r"\right", "")
    x = x.replace(r"\,", " ").replace(r"\;", " ").replace(r"\!", "")
    x = x.replace("{", "").replace("}", "")
    x = x.replace("\\", "")
    x = re.sub(r"\s+", " ", x).strip()
    x = x.replace("p(e1) = p(e2) = 0", "p(e1)=p(e2)=0")
    x = x.replace("p(e3) = 1", "p(e3)=1")
    x = x.replace("Uq (sl2)", "Uq(sl2)")
    x = x.replace("GLq (2|1)", "GLq(2|1)")
    return x

def _flatten_inline_math_for_docx(text):
    return re.sub(r"\$([^$\n]+)\$", lambda m: _plain_inline_math(m.group(1)), text)

tex = _flatten_inline_math_for_docx(tex)

# Başlıklardaki ($...$) matematiği düz metne çevir: heading OMML'i Word
# İÇİNDEKİLER alanına geçmediğinden, başlık+TOC tutarlı görünsün.
def _math_to_text(s):
    def clean(m):
        x = m.group(1)
        x = re.sub(r"\\math(?:frak|rm|bb|cal|bf|it)\{([^{}]*)\}", r"\1", x)
        x = re.sub(r"\\check\{([^{}]*)\}", r"\1̌", x)
        for ch in ("_", "{", "}", "\\", "$"):
            x = x.replace(ch, "")
        return x
    return re.sub(r"\$([^$]*)\$", clean, s)

def _title_fix(m):
    return "\\" + m.group(1) + "{" + _math_to_text(m.group(2)) + "}"

tex = re.sub(r"\\(chapter|section|subsection)\*?\{((?:[^{}]|\{[^{}]*\})*)\}",
             _title_fix, tex)

# tikzpicture bloklarını sırayla PNG ile değiştir (belge sırası)
order = ["tikz_weight", "tikz_ybe", "tikz_spec", "tikz_superperm", "tikz_place", "tikz_k4"]
it = iter(order)
def repl(m):
    name = next(it)
    return r"\includegraphics[width=0.82\linewidth]{figures/%s-1.png}" % name
tex = re.sub(r"\\begin\{tikzpicture\}.*?\\end\{tikzpicture\}", repl, tex, flags=re.DOTALL)

# spacing ortamları docx'te gereksiz; argümanları metne sızmasın diye kaldır
tex = re.sub(r"\\begin\{spacing\}\{[\d.]+\}", "", tex)
tex = tex.replace(r"\end{spacing}", "")

# pandoc matematik parser'ının takıldığı yerleri sadeleştir
tex = tex.replace("\\setlength{\\arraycolsep}{3.2pt}\n", "")
tex = tex.replace(
    r"\multicolumn{1}{c}{$\qint{n}=\dfrac{q^n-q^{-n}}{q-q^{-1}}$}",
    r"$[n]_q=(q^n-q^{-n})/(q-q^{-1})$")

# Şekil / Çizelge başlıklarına numara etiketi ekle (pandoc otomatik numara koymaz)
fig_labels = ["4.1", "8.1", "8.2", "8.3", "9.1", "9.2", "9.3", "9.4", "9.5"]
tab_labels = ["3.1", "6.1", "9.1", "10.1", "B.1"]

def label_captions(text, env, labels, word):
    out = []
    idx = 0
    pos = 0
    while True:
        b = text.find(r"\begin{" + env + "}", pos)
        if b == -1:
            out.append(text[pos:]); break
        e = text.find(r"\end{" + env + "}", b)
        block = text[b:e]
        cap = block.find(r"\caption{")
        if cap != -1 and idx < len(labels):
            block = (block[:cap] + r"\caption{\textbf{%s %s} " % (word, labels[idx])
                     + block[cap + len(r"\caption{"):])
            idx += 1
        out.append(text[pos:b]); out.append(block)
        pos = e
    return "".join(out)

tex = label_captions(tex, "figure", fig_labels, "Şekil")
tex = label_captions(tex, "table", tab_labels, "Çizelge")

# PDF görselleri -> PNG
tex = tex.replace("R_sl2_V1.pdf", "R_sl2_V1-1.png")
tex = tex.replace("R_gl21_structure.pdf", "R_gl21_structure-1.png")
tex = tex.replace("ybe_products_27.pdf", "ybe_products_27-1.png")

with open(os.path.join(HERE, "thesis_ytu_docx.tex"), "w", encoding="utf-8") as f:
    f.write(tex)
print("thesis_ytu_docx.tex yazıldı")
