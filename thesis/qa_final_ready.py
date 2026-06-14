#!/usr/bin/env python3
"""FINAL-READY DOCX/PDF teslim QA kontrolü."""
import os
import re
import subprocess
import sys
import unicodedata
import zipfile
from xml.etree import ElementTree as ET

HERE = os.path.dirname(os.path.abspath(__file__))
DOCX = os.path.join(HERE, "Quantum Grup Yapıları - YTU Bitirme Tezi - FINAL-READY.docx")
PDF = os.path.join(HERE, "Quantum Grup Yapıları - YTU Bitirme Tezi - FINAL-READY.pdf")
NOTES = os.path.join(HERE, "TESLIM_ONCESI_KONTROL_NOTLARI_FINAL-READY.md")
TEX = os.path.join(HERE, "thesis_ytu.tex")


def normalize(text):
    text = unicodedata.normalize("NFC", text)
    text = text.replace("\xa0", " ")
    return re.sub(r"\s+", " ", text)


def compact(text):
    return re.sub(r"\s+", "", normalize(text))


def docx_text(path):
    ns = {"w": "http://schemas.openxmlformats.org/wordprocessingml/2006/main"}
    parts = []
    with zipfile.ZipFile(path) as zf:
        for name in sorted(n for n in zf.namelist() if n.startswith("word/") and n.endswith(".xml")):
            if not (name == "word/document.xml" or name.startswith("word/header") or name.startswith("word/footer")):
                continue
            root = ET.fromstring(zf.read(name))
            for node in root.findall(".//w:t", ns):
                if node.text:
                    parts.append(node.text)
    return normalize(" ".join(parts))


def pdf_text(path):
    proc = subprocess.run(["pdftotext", path, "-"], text=True, capture_output=True)
    if proc.returncode != 0:
        raise RuntimeError(proc.stderr.strip() or "pdftotext failed")
    return proc.stdout


def tex_text(path):
    with open(path, encoding="utf-8") as f:
        return f.read()


def require(label, condition, errors):
    if not condition:
        errors.append(label)


def citation_check(tex):
    cite_keys = set()
    for body in re.findall(r"\\cite\{([^{}]+)\}", tex):
        cite_keys.update(k.strip() for k in body.split(",") if k.strip())
    bib_keys = set(re.findall(r"\\bibitem\{([^{}]+)\}", tex))
    return cite_keys == bib_keys, sorted(cite_keys - bib_keys), sorted(bib_keys - cite_keys)


def main():
    errors = []
    for label, path in [("DOCX", DOCX), ("PDF", PDF), ("kontrol notu", NOTES)]:
        require(f"{label} dosyası yok", os.path.exists(path), errors)
    if errors:
        for err in errors:
            print("FAIL:", err)
        return 1

    dx = docx_text(DOCX)
    dx_compact = compact(dx)
    px_raw = pdf_text(PDF)
    px = normalize(px_raw)
    px_compact = compact(px)
    tex = tex_text(TEX)
    notes = tex_text(NOTES)

    require("DOCX kapakta öğrenci no eksik", "Öğrenci No: 22025083" in dx, errors)
    require("PDF kapakta öğrenci no eksik", "22025083" in px, errors)

    toc_items = ["1 Giriş", "2 Teorik Arka Plan", "3 Kuantum Grup Uq(sl2)'nin Tanımı", "KAYNAKLAR", "ÖZGEÇMİŞ"]
    for item in toc_items:
        require(f"DOCX İçindekiler/metin eksik: {item}", compact(item) in dx_compact, errors)

    good = ["Tanım 2.1", "Tanım 2.2", "Tanım 2.3", "Teorem 2.4", "Tanım 2.5", "Örnek 2.6", "Tanım 3.1", "Teorem 4.1", "Çizelge 3.1", "Şekil 4.1", "Bölüm 10"]
    for item in good:
        require(f"DOCX doğru sayaç eksik: {item}", item in dx, errors)
        require(f"PDF doğru sayaç eksik: {item}", item in px, errors)

    bad = ["Tanım 7.1", "Tanım 8.1", "Teorem 9.1", "Bölüm 15", "Çizelge 8.1"]
    for item in bad:
        require(f"DOCX yanlış sayaç var: {item}", item not in dx, errors)
        require(f"PDF yanlış sayaç var: {item}", item not in px, errors)

    critical = ["Uq(sl2)", "GLq(2|1)", "Vn", "V1", "R13", "p(e1)=p(e2)=0", "p(e3)=1", "Δ", "ε", "τ", "[n]q"]
    for item in critical:
        require(f"DOCX kritik sembol fallback eksik: {item}", compact(item) in dx_compact, errors)

    pdf_terms = ["TEKNİK", "LİSANS", "Danışman", "ÇELİK", "İÇİNDEKİLER", "ÖZGEÇMİŞ"]
    for item in pdf_terms:
        require(f"PDF normalize Türkçe terim eksik: {item}", item in px, errors)

    cite_ok, missing_bib, uncited_bib = citation_check(tex)
    require(f"Kaynakça-atıf eşleşmiyor missing={missing_bib} uncited={uncited_bib}", cite_ok, errors)

    forbidden_self_refs = ["Bu makale", "bu makalenin", "makalenin kapsamı", "Makalede"]
    for item in forbidden_self_refs:
        require(f"Tezin kendisine makale deniyor: {item}", item not in tex, errors)

    require("Turnitin notu eksik", "Turnitin benzerlik raporu ayrıca alınmalı" in notes and "%30" in notes, errors)

    if errors:
        for err in errors:
            print("FAIL:", err)
        return 1
    print("PASS: FINAL-READY DOCX/PDF QA kontrolleri geçti.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
