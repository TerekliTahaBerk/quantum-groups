#!/usr/bin/env python3
"""PDF-FINAL teslim QA kontrolü."""
import os
import re
import subprocess
import sys
import unicodedata

HERE = os.path.dirname(os.path.abspath(__file__))
PDF = os.path.join(HERE, "Quantum Grup Yapıları - YTU Bitirme Tezi - PDF-FINAL.pdf")
TEX = os.path.join(HERE, "thesis_ytu.tex")
LOGS = [
    os.path.join(HERE, "thesis_ytu.log"),
    "/tmp/ytu_pdf_final_3.log",
]


def run(cmd):
    proc = subprocess.run(cmd, text=True, capture_output=True)
    if proc.returncode != 0:
        raise RuntimeError(proc.stderr.strip() or proc.stdout.strip() or "command failed")
    return proc.stdout


def normalize(text):
    text = unicodedata.normalize("NFKC", text)
    text = text.replace("\xa0", " ")
    return re.sub(r"\s+", " ", text)


def compact(text):
    return re.sub(r"\s+", "", normalize(text))


def require(label, condition, errors):
    if not condition:
        errors.append(label)


def pdf_text():
    return run(["pdftotext", PDF, "-"])


def pdfinfo():
    return run(["pdfinfo", PDF])


def read(path):
    with open(path, encoding="utf-8", errors="replace") as f:
        return f.read()


def citation_check(tex):
    cite_keys = set()
    for body in re.findall(r"\\cite\{([^{}]+)\}", tex):
        cite_keys.update(k.strip() for k in body.split(",") if k.strip())
    bib_keys = set(re.findall(r"\\bibitem\{([^{}]+)\}", tex))
    return cite_keys == bib_keys, sorted(cite_keys - bib_keys), sorted(bib_keys - cite_keys)


def main():
    errors = []
    require("PDF dosyası yok", os.path.exists(PDF), errors)
    if errors:
        for err in errors:
            print("FAIL:", err)
        return 1

    info = pdfinfo()
    m = re.search(r"Page size:\s+([0-9.]+) x ([0-9.]+) pts", info)
    require("PDF page size okunamadı", m is not None, errors)
    if m:
        w, h = float(m.group(1)), float(m.group(2))
        require(f"A4 değil: {w} x {h}", abs(w - 595.276) < 1.0 and abs(h - 841.89) < 1.0, errors)

    raw = pdf_text()
    norm = normalize(raw)
    comp = compact(raw)

    required = [
        "22025083",
        "İÇİNDEKİLER",
        "SİMGE LİSTESİ",
        "ÖZET",
        "1 Giriş",
        "2 Teorik Arka Plan",
        "3 Kuantum Grup Uq(sl2)’nin Tanımı",
        "11 Sonuç ve Öneriler",
        "KAYNAKLAR",
        "ÖZGEÇMİŞ",
        "Tanım 2.1",
        "Tanım 3.1",
        "Teorem 4.1",
        "Tablo 3.1",
        "Şekil 4.1",
        "Uq(sl2)",
        "GLq(2|1)",
    ]
    for item in required:
        require(f"PDF metninde eksik: {item}", compact(item) in comp, errors)

    good_counters = ["Tanım 2.2", "Tanım 2.3", "Teorem 2.4", "Tanım 2.5", "Örnek 2.6", "Bölüm 10"]
    for item in good_counters:
        require(f"PDF doğru sayaç eksik: {item}", compact(item) in comp, errors)

    bad = ["ABSTRACT", "Keywords:", "Bölüm 15", "Tanım 7.1", "Tanım 8.1", "Teorem 9.1", "??", "undefined"]
    for item in bad:
        require(f"PDF hatalı ifade içeriyor: {item}", item not in norm, errors)

    turkish = ["MATEMATİK", "LİSANS", "Danışman", "ÇELİK", "İÇİNDEKİLER", "ŞEKİL", "TABLO", "ÖZGEÇMİŞ", "doğrulama", "bağıntı", "çalışma"]
    for item in turkish:
        require(f"Ham/normalize Türkçe metin eksik: {item}", item in raw or item in norm, errors)

    tex = read(TEX)
    cite_ok, missing_bib, uncited_bib = citation_check(tex)
    require(f"Kaynakça-atıf eşleşmiyor missing={missing_bib} uncited={uncited_bib}", cite_ok, errors)

    log_text = "\n".join(read(path) for path in LOGS if os.path.exists(path))
    undefined_patterns = [
        "Reference `",
        "Citation `",
        "There were undefined references",
        "There were undefined citations",
        "LaTeX Warning: Reference",
        "LaTeX Warning: Citation",
    ]
    for pattern in undefined_patterns:
        require(f"LaTeX log undefined uyarısı içeriyor: {pattern}", pattern not in log_text, errors)

    overfull = re.findall(r"Overfull \\hbox .*", log_text)
    if overfull:
        print("WARN: Overfull hbox raporu:")
        for line in overfull:
            print("WARN:", line)
    else:
        print("PASS: Overfull hbox yok.")

    if errors:
        for err in errors:
            print("FAIL:", err)
        return 1
    print("PASS: PDF-FINAL QA kontrolleri geçti.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
