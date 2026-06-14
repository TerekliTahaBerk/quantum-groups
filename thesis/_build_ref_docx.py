#!/usr/bin/env python3
"""YTÜ biçim stillerini taşıyan pandoc reference.docx üretir."""
import os
from docx import Document
from docx.shared import Pt, Cm, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.style import WD_STYLE_TYPE

HERE = os.path.dirname(os.path.abspath(__file__))
doc = Document()

# Sayfa: A4 + kenar boşlukları (sol 3,5 cm; diğer 2,5 cm)
for sec in doc.sections:
    sec.page_height = Cm(29.7)
    sec.page_width = Cm(21.0)
    sec.left_margin = Cm(3.5)
    sec.right_margin = Cm(2.5)
    sec.top_margin = Cm(2.5)
    sec.bottom_margin = Cm(2.5)

styles = doc.styles

# Normal: Times New Roman 12, 1.5 satır aralığı, iki yana yaslı
normal = styles["Normal"]
normal.font.name = "Times New Roman"
normal.font.size = Pt(12)
pf = normal.paragraph_format
pf.line_spacing = 1.5
pf.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
pf.space_after = Pt(6)

def set_heading(name, size):
    st = styles[name]
    st.font.name = "Times New Roman"
    st.font.size = Pt(size)
    st.font.bold = True
    st.font.color.rgb = RGBColor(0, 0, 0)
    st.paragraph_format.line_spacing = 1.5
    st.paragraph_format.space_before = Pt(12)
    st.paragraph_format.space_after = Pt(8)
    st.paragraph_format.alignment = WD_ALIGN_PARAGRAPH.LEFT

# Başlık dereceleri: 1 -> 17,5pt, 2 -> 14pt, 3 -> 12pt
for nm, sz in [("Heading 1", 17.5), ("Heading 2", 14), ("Heading 3", 12),
               ("Title", 16), ("Heading 4", 12)]:
    try:
        set_heading(nm, sz)
    except KeyError:
        pass

# Kod / verbatim stili (varsa)
for nm in ("Source Code", "Verbatim Char", "No Spacing"):
    try:
        styles[nm].font.name = "Courier New"
        styles[nm].font.size = Pt(9)
    except KeyError:
        pass

doc.save(os.path.join(HERE, "_ref.docx"))
print("_ref.docx yazıldı")
