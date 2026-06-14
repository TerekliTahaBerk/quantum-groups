#!/usr/bin/env python3
"""FINAL DOCX/PDF metin katmanı ve sayaç QA kontrolü."""
import os
import re
import subprocess
import sys
import unicodedata
import zipfile
from xml.etree import ElementTree as ET

HERE = os.path.dirname(os.path.abspath(__file__))
DOCX = os.path.join(HERE, "Quantum Grup Yapıları - YTU Bitirme Tezi - FINAL.docx")
PDF = os.path.join(HERE, "Quantum Grup Yapıları - YTU Bitirme Tezi - FINAL.pdf")


def normalize(text):
    text = unicodedata.normalize("NFC", text)
    text = text.replace("\xa0", " ")
    return re.sub(r"\s+", " ", text)


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
    return normalize(proc.stdout)


def require(name, condition, errors):
    if not condition:
        errors.append(name)


def main():
    errors = []
    require("FINAL DOCX dosyası yok", os.path.exists(DOCX), errors)
    require("FINAL PDF dosyası yok", os.path.exists(PDF), errors)
    if errors:
        for err in errors:
            print("FAIL:", err)
        return 1

    dx = docx_text(DOCX)
    px = pdf_text(PDF)
    bad = ["Tanım 7.1", "Tanım 7.2", "Tanım 7.3", "Tanım 8.1", "Teorem 9.1", "Bölüm 15", "Çizelge 8.1"]
    good = ["Tanım 2.1", "Tanım 2.2", "Tanım 2.3", "Tanım 3.1", "Teorem 4.1"]
    toc = ["1 Giriş", "2 Teorik Arka Plan", "KAYNAKLAR", "ÖZGEÇMİŞ"]

    for item in bad:
        require(f"DOCX yasaklı sayaç içeriyor: {item}", item not in dx, errors)
        require(f"PDF yasaklı sayaç içeriyor: {item}", item not in px, errors)
    for item in good:
        require(f"DOCX doğru sayaç eksik: {item}", item in dx, errors)
        require(f"PDF doğru sayaç eksik: {item}", item in px, errors)
    for item in toc:
        require(f"DOCX İçindekiler başlığı eksik: {item}", item in dx, errors)
        require(f"PDF İçindekiler başlığı eksik: {item}", item in px, errors)
    require("DOCX 3. bölüm başlığı eksik", "3 Kuantum Grup Uq" in dx and "nin Tanımı" in dx, errors)
    require("PDF 3. bölüm başlığı eksik", "3 Kuantum Grup Uq" in px and "nin Tanımı" in px, errors)

    require("DOCX öğrenci no eksik", "22025083" in dx, errors)
    require("PDF öğrenci no eksik", "22025083" in px, errors)
    require("DOCX öğrenci no yer tutucusu kalmış", "Öğrenci No: …" not in dx and r"\ldots" not in dx, errors)
    require("PDF öğrenci no yer tutucusu kalmış", "Öğrenci No: …" not in px, errors)
    require("DOCX Bölüm 10 referansı eksik", "Bölüm 10" in dx, errors)
    require("PDF Bölüm 10 referansı eksik", "Bölüm 10" in px, errors)

    if errors:
        for err in errors:
            print("FAIL:", err)
        return 1
    print("PASS: FINAL DOCX/PDF sayaç, TOC ve öğrenci no QA kontrolleri geçti.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
