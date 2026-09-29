# Historical thesis material

This directory preserves the undergraduate thesis from which the package
originated, for provenance. **None of these files is the current
manuscript; that is the SciPost Physics Codebases userguide in
[`../scipost/`](../scipost/).** Section 5.2 of the userguide describes how
the package was used to audit this thesis.

- `Lisans Bitirme Tezi.pdf` — the submitted thesis, *Quantum Grup
  Yapılarının Python Ortamında Modellenmesi* ("Modelling Quantum Group
  Structures in Python"), Department of Mathematics, Yıldız Technical
  University, June 2026 (in Turkish; supervisor Prof. Dr. Salih Çelik).
- `thesis_ytu.tex` — LaTeX source of the thesis; `thesis_ytu_docx.tex`,
  `_*.py`, `build_ytu.sh`, `build_pdf_final.sh` and `_ref.docx` are the
  author's thesis build pipeline (paths in the shell scripts are specific to
  the author's macOS machine). `…FINAL-READY.docx` is the Word delivery copy.
- `thesis.tex`, `thesis_revised.tex`, `math.cls` — an earlier Turkish
  article version of the same material (`make historical-article-pdf`).
- `figures/generate_figures.py` — regenerates the three package-derived
  figures used in the thesis (`R_sl2_V1.pdf`, `R_gl21_structure.pdf`,
  `ybe_products_27.pdf`) from `quantum_group` output (`make figures`).
  The `tikz_*` files are hand-drawn diagrams.
- `*KONTROL_NOTLARI*.md`, `qa_*.py`, `qa_pdf_pages/` — the author's
  pre-submission formatting checks (Turkish) and page renders they refer to.
- `ERRATA.md` — mathematical and convention corrections to the archived
  thesis identified during the September 2026 audit (see `../AUDIT.md`).
  The archived thesis files are intentionally left unchanged.
