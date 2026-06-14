#!/usr/bin/env python3
"""thesis.tex içindeki tikzpicture şekillerini bağımsız PNG olarak render eder."""
import os, re, subprocess

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "figures")

with open(os.path.join(HERE, "thesis.tex"), encoding="utf-8") as f:
    src = f.read()

PRE = r"""\documentclass[border=6pt]{standalone}
\usepackage[T1]{fontenc}
\usepackage[utf8]{inputenc}
\usepackage{mathptmx}
\usepackage{amsmath,amssymb,amsfonts,mathrsfs}
\usepackage[dvipsnames]{xcolor}
\usepackage{tikz}
\usetikzlibrary{calc,positioning,arrows.meta,decorations.pathreplacing,
                decorations.markings,matrix,fit,backgrounds,shapes.misc}
\renewcommand{\sl}{\mathfrak{sl}}
\newcommand{\Uq}{U_q(\sl_2)}
\newcommand{\qint}[1]{[#1]_q}
\newcommand{\Rcheck}{\check{R}}
\definecolor{accent}{RGB}{59,91,146}
\definecolor{accentsoft}{RGB}{155,180,216}
\definecolor{oddsign}{RGB}{138,40,132}
\tikzset{
  strand/.style={line width=1pt, accent!80!black},
  rbox/.style={draw=accent!70!black, fill=accentsoft!55, rounded corners=2pt,
               line width=0.8pt, minimum height=6mm},
  rdot/.style={circle, fill=accent, inner sep=1.6pt},
  knode/.style={circle, draw=accent!70!black, fill=accentsoft!45,
                line width=0.8pt, minimum size=7mm, font=\small},
  kedge/.style={accent!70!black, line width=0.9pt},
  faredge/.style={oddsign!75!black, line width=0.9pt, densely dashed},
  glabel/.style={font=\footnotesize, accent!60!black},
}
\begin{document}
"""

# tikzpicture bloklarını ve hemen ardındaki \label'i eşle
blocks = re.findall(r"(\\begin\{tikzpicture\}.*?\\end\{tikzpicture\})",
                    src, re.DOTALL)
# label'leri figürlerden çıkar: her tikz'in bulunduğu figure'ün label'i
labels = re.findall(r"\\begin\{tikzpicture\}.*?\\end\{tikzpicture\}.*?\\label\{(fig:[^}]+)\}",
                    src, re.DOTALL)

print(f"{len(blocks)} tikzpicture, {len(labels)} label bulundu")

env = dict(os.environ)
env["PATH"] = os.path.expanduser("~/Library/TinyTeX/bin/universal-darwin") + ":" + env["PATH"]

for i, blk in enumerate(blocks):
    name = labels[i].replace("fig:", "tikz_") if i < len(labels) else f"tikz_{i}"
    tex = PRE + blk + "\n\\end{document}\n"
    base = os.path.join(OUT, name)
    with open(base + ".tex", "w", encoding="utf-8") as f:
        f.write(tex)
    r = subprocess.run(["pdflatex", "-interaction=nonstopmode", "-output-directory", OUT,
                        base + ".tex"], env=env, capture_output=True, text=True)
    ok = os.path.exists(base + ".pdf")
    print(("OK  " if ok else "FAIL") + f" {name}")
    if ok:
        subprocess.run(["pdftoppm", "-png", "-r", "200", base + ".pdf", base], env=env)
