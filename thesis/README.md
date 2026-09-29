# Undergraduate thesis

The package originated in the author's undergraduate thesis. These files are
kept for provenance and are not the current manuscript; that is the userguide
in [`../scipost/`](../scipost/), whose Section 5.2 describes how the package
was used to audit this thesis.

- `Lisans Bitirme Tezi.pdf` — the submitted thesis, *Quantum Grup
  Yapılarının Python Ortamında Modellenmesi* ("Modelling Quantum Group
  Structures in Python"), Department of Mathematics, Yıldız Technical
  University, June 2026 (in Turkish; supervisor Prof. Dr. Salih Çelik).
- `thesis_ytu.tex` — its LaTeX source, assembled from an earlier article
  version by a script that is now only in the Git history. The submitted PDF
  was built with `lualatex thesis_ytu.tex` (three runs; needs Times New Roman
  and babel's Turkish support); pdflatex also works, with other fonts.
- `figures/` — the figures the thesis includes; `generate_figures.py`
  regenerates the three package-derived ones (`R_sl2_V1.pdf`,
  `R_gl21_structure.pdf`, `ybe_products_27.pdf`) from `quantum_group`
  output (`make figures`).
- `poster.pdf` — the poster presented with the thesis.
- `ERRATA.md` — mathematical and convention corrections found in the
  September 2026 audit (see `../AUDIT.md`). The thesis files themselves are
  intentionally left unchanged.

The thesis build pipeline (Word conversion, pre-submission check notes, page
renders), an earlier article version (`thesis.tex`, `thesis_revised.tex`)
and the poster sources were removed in version 1.1.1; they remain in the Git
history (last in commit `7aafa2c`).
