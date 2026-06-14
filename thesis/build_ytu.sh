#!/usr/bin/env bash
# =====================================================================
#  YTÜ Fen-Edebiyat Lisans Bitirme Tezi — tam üretim pipeline'ı
#  (KL-058 / FR-1925 uyumlu). thesis.tex kaynağından DOCX + PDF üretir.
#  Tüm düzeltmeler kaynak/scriptlerde; bu betik onları sırayla çalıştırır.
# =====================================================================
set -euo pipefail
cd "$(dirname "$0")"
export PATH="$HOME/Library/TinyTeX/bin/universal-darwin:$PATH"
SOFFICE="$HOME/Applications/LibreOffice.app/Contents/MacOS/soffice"
DOCX="Quantum Grup Yapıları - YTÜ Bitirme Tezi.docx"
PDF="Quantum Grup Yapıları - YTÜ Bitirme Tezi.pdf"

echo "==> 1) YTÜ logosu (FR-1925 şablonundan, yoksa)"
[ -f figures/ytu_logo.png ] || echo "   UYARI: figures/ytu_logo.png yok!"

echo "==> 2) thesis_ytu.tex montajı (makale->tez, \\cite ekleri, Tablo->Çizelge)"
python3 _assemble_ytu.py

echo "==> 3) TikZ figürleri (PNG)"
python3 _render_tikz.py

echo "==> 4) PDF (pdflatex x2)"
pdflatex -interaction=nonstopmode thesis_ytu.tex >/tmp/ytu_pdf1.log 2>&1
pdflatex -interaction=nonstopmode thesis_ytu.tex >/tmp/ytu_pdf2.log 2>&1
cp -f thesis_ytu.pdf "$PDF"

echo "==> 5) pandoc reference.docx (YTÜ stilleri)"
python3 _build_ref_docx.py

echo "==> 6) thesis_ytu_docx.tex (makro genişletme + figür PNG)"
python3 _make_docx_tex.py

echo "==> 7) pandoc -> DOCX (matematik OMML)"
pandoc thesis_ytu_docx.tex -o "$DOCX" \
  --reference-doc=_ref.docx \
  --resource-path=.:figures 2>/tmp/ytu_pandoc.log

echo "==> 8) DOCX cilalama (numaralandırma, İÇİNDEKİLER alanı, listeler, kapak)"
python3 _postprocess_docx.py

echo "==> 9) İÇİNDEKİLER alanını LibreOffice ile DOLDUR ve DOCX'e kaydet"
if [ -x "$SOFFICE" ]; then
  python3 _materialize_toc.py "$DOCX"
else
  echo "   UYARI: soffice yok, İÇİNDEKİLER alanı Word'de F9 ile güncellenir (updateFields açık)"
fi

echo "==> 10) FINAL teslim dosyaları"
FINAL_DOCX="Quantum Grup Yapıları - YTU Bitirme Tezi - FINAL.docx"
FINAL_PDF="Quantum Grup Yapıları - YTU Bitirme Tezi - FINAL.pdf"
FINAL_DOCXPDF="Quantum Grup Yapıları - YTU Bitirme Tezi - FINAL-DOCX-RENDER.pdf"
READY_DOCX="Quantum Grup Yapıları - YTU Bitirme Tezi - FINAL-READY.docx"
READY_PDF="Quantum Grup Yapıları - YTU Bitirme Tezi - FINAL-READY.pdf"
READY_DOCXPDF="Quantum Grup Yapıları - YTU Bitirme Tezi - FINAL-READY-DOCX-RENDER.pdf"
cp -f "$DOCX" "$FINAL_DOCX"
cp -f "$PDF"  "$FINAL_PDF"
# Alternatif: DOCX'ten üretilen PDF (sayfa numaraları DOCX ile birebir)
if [ -x "$SOFFICE" ]; then
  rm -rf /tmp/ytu_qa && mkdir -p /tmp/ytu_qa
  pkill -f soffice 2>/dev/null || true
  sleep 1
  if "$SOFFICE" -env:UserInstallation=file:///tmp/ytu_libreoffice_convert_profile \
    --headless --norestore --convert-to pdf --outdir /tmp/ytu_qa "$FINAL_DOCX" \
    >/tmp/ytu_soffice.log 2>&1; then
    cp -f /tmp/ytu_qa/*.pdf "$FINAL_DOCXPDF" 2>/dev/null && echo "   $FINAL_DOCXPDF"
  else
    echo "   UYARI: doğrudan LibreOffice PDF dönüşümü başarısız; render_docx fallback deneniyor."
    RENDER_DOCX="$HOME/.codex/plugins/cache/openai-primary-runtime/documents/26.601.10930/skills/documents/render_docx.py"
    RENDER_PY="$HOME/.cache/codex-runtimes/codex-primary-runtime/dependencies/python/bin/python3"
    if [ -x "$RENDER_PY" ] && [ -f "$RENDER_DOCX" ]; then
      rm -rf /tmp/ytu_docx_render_build && mkdir -p /tmp/ytu_docx_render_build
      "$RENDER_PY" "$RENDER_DOCX" "$FINAL_DOCX" --output_dir /tmp/ytu_docx_render_build --emit_pdf >/tmp/ytu_render_docx.log 2>&1
      cp -f /tmp/ytu_docx_render_build/*.pdf "$FINAL_DOCXPDF" 2>/dev/null && echo "   $FINAL_DOCXPDF"
    else
      echo "   UYARI: DOCX-render PDF üretilemedi; ana FINAL PDF LaTeX'ten üretildi."
    fi
  fi
  pkill -f soffice 2>/dev/null || true
fi
cp -f "$FINAL_DOCX" "$READY_DOCX"
cp -f "$FINAL_PDF" "$READY_PDF"
[ -f "$FINAL_DOCXPDF" ] && cp -f "$FINAL_DOCXPDF" "$READY_DOCXPDF"

echo "==> 11) FINAL QA"
python3 qa_final.py
[ -f "TESLIM_ONCESI_KONTROL_NOTLARI_FINAL-READY.md" ] && python3 qa_final_ready.py

echo "==> bitti: FINAL DOCX + PDF (+ DOCX-RENDER alternatifi)"
