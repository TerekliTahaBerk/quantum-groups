#!/usr/bin/env bash
set -euo pipefail

cd "$(dirname "$0")"
export PATH="$HOME/Library/TinyTeX/bin/universal-darwin:$PATH"
export TEXMFVAR="/tmp/ytu_texmf_var"
export XDG_CACHE_HOME="/tmp/ytu_font_cache"
mkdir -p "$TEXMFVAR" "$XDG_CACHE_HOME"

OUT="Quantum Grup Yapıları - YTU Bitirme Tezi - PDF-FINAL.pdf"

echo "==> 1) LaTeX kaynak montajı"
python3 _assemble_ytu.py

echo "==> 2) TikZ figürleri"
python3 _render_tikz.py

echo "==> 3) PDF build (LuaLaTeX x3)"
lualatex -interaction=nonstopmode -halt-on-error thesis_ytu.tex >/tmp/ytu_pdf_final_1.log 2>&1
lualatex -interaction=nonstopmode -halt-on-error thesis_ytu.tex >/tmp/ytu_pdf_final_2.log 2>&1
lualatex -interaction=nonstopmode -halt-on-error thesis_ytu.tex >/tmp/ytu_pdf_final_3.log 2>&1

cp -f thesis_ytu.pdf "$OUT"

echo "==> 4) PDF QA"
python3 qa_pdf_final.py

echo "==> bitti: $OUT"
