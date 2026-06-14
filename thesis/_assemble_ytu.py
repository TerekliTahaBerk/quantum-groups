#!/usr/bin/env python3
"""YTÜ bitirme tezi LaTeX kaynağını makale (thesis.tex) gövdesinden üretir."""
import io, os

HERE = os.path.dirname(os.path.abspath(__file__))

def read(p):
    with open(os.path.join(HERE, p), encoding="utf-8") as f:
        return f.read()

src = read("thesis.tex").splitlines()

# 1-indexed inclusive slices
def slice_lines(a, b):
    return "\n".join(src[a-1:b])

def find_line(pattern, start=1):
    for idx, line in enumerate(src[start-1:], start=start):
        if pattern in line:
            return idx
    raise ValueError(f"Bulunamadı: {pattern}")

main = slice_lines(229, 1530)        # Giriş ... Sonuçlar bölümünün sonu
appendix_start = find_line(r"\appendix", 1531)
appendix_end = find_line(r"\begin{thebibliography}", appendix_start) - 1
appendix = slice_lines(appendix_start, appendix_end)

def transform(text):
    text = text.replace(r"\subsection{", r"\zzzSUB{")
    text = text.replace(r"\section{", r"\chapter{")
    text = text.replace(r"\zzzSUB{", r"\section{")
    # Başlık düzeltmeleri (YTÜ terminolojisi)
    text = text.replace(r"\chapter{Giriş ve Motivasyon}", r"\chapter{Giriş}")
    text = text.replace(r"\chapter{Sonuçlar ve Gelecek Çalışma}",
                        r"\chapter{Sonuç ve Öneriler}")

    # --- "makale" (kendine atıf) -> "tez"/"çalışma" ---
    self_ref = [
        (r"\paragraph{Makalenin akışı.}", r"\paragraph{Tezin akışı.}"),
        ("dolayısıyla makalede hesaplamalı olarak",
         "dolayısıyla bu tezde hesaplamalı olarak"),
        ("bu makalenin kapsamı", "bu tezin kapsamı"),
        ("Makalenin ayırt edici hesaplamalı katkısı",
         "Tezin ayırt edici hesaplamalı katkısı"),
        ("Bu ek, makaleye eşlik eden", "Bu ek, bu teze eşlik eden"),
        ("Depo, makaledeki sembolik hesaplamaları",
         "Depo, bu tezdeki sembolik hesaplamaları"),
        ("MANUSCRIPT\\_CODE\\_MAPPING.md}: makaledeki başlıklar",
         "MANUSCRIPT\\_CODE\\_MAPPING.md}: tezdeki başlıklar"),
        ("Bu testler, makaledeki açık", "Bu testler, tezdeki açık"),
        ("Makaledeki şekiller aşağıdaki", "Tezdeki şekiller aşağıdaki"),
        ("yalnızca makalenin ana PDF dosyası", "yalnızca tezin ana PDF dosyası"),
        ("olmalıdır. Makaleye", "olmalıdır. Teze"),
    ]
    # --- "makale" (dış kaynak: Çelik & Çelik 2021) -> açık atıf ---
    ext_ref = [
        ("Burada amaç, o makalede verilen $9\\times 9$",
         "Burada amaç, Çelik ve Çelik'in çalışmasında~\\cite{CelikGL21} verilen $9\\times 9$"),
        ("Makaledeki $R$-matrisi $V\\otimes V$",
         "Çelik ve Çelik'in makalesindeki~\\cite{CelikGL21} $R$-matrisi $V\\otimes V$"),
        ("makaledeki Gauss ayrışımı", "ilgili makaledeki~\\cite{CelikGL21} Gauss ayrışımı"),
    ]
    # --- Atıfsız kaynaklara metin içi atıf ---
    cites = [
        ("V.~Drinfeld ve M.~Jimbo'nun --- istatistik",
         "V.~Drinfeld ve M.~Jimbo'nun~\\cite{Drinfeld,Jimbo,KS} --- istatistik"),
        ("Kashiwara'nın gözlemi, bu limitte",
         "Kashiwara'nın gözlemi~\\cite{Kashiwara,HK}, bu limitte"),
        (r"\emph{Jones polinomudur}.", r"\emph{Jones polinomudur}~\cite{Jones}."),
        (r"\texttt{pytest} tabanlı test takımı.",
         r"\texttt{pytest}~\cite{pytest} tabanlı test takımı."),
        ("şöyledir: SymPy sembolik cebir ve matris",
         "şöyledir: SymPy~\\cite{SymPy} sembolik cebir ve matris"),
    ]
    for old, new in self_ref + ext_ref + cites:
        text = text.replace(old, new)

    return text

def ascii_lstlisting_comments(text):
    table = str.maketrans({
        "ç": "c", "Ç": "C",
        "ğ": "g", "Ğ": "G",
        "ı": "i", "I": "I",
        "İ": "I", "ö": "o",
        "Ö": "O", "ş": "s",
        "Ş": "S", "ü": "u",
        "Ü": "U",
    })

    def repl(m):
        return m.group(0).translate(table)

    return re_sub_lstlisting(text, repl)

def re_sub_lstlisting(text, repl):
    import re
    return re.sub(
        r"\\begin\{lstlisting\}(\[[^\]]*\])?.*?\\end\{lstlisting\}",
        repl,
        text,
        flags=re.DOTALL,
    )

main = transform(main)
appendix = transform(appendix)
main = ascii_lstlisting_comments(main)
appendix = ascii_lstlisting_comments(appendix)

# Appendix: baştaki \appendix komutunu EK yapılandırmasıyla değiştir
appendix_cfg = r"""\clearpage
\phantomsection
\chapter*{EKLER}
\addcontentsline{toc}{chapter}{EKLER}
\appendix
\renewcommand{\thechapter}{\Alph{chapter}}
\renewcommand{\thesection}{\thechapter.\arabic{section}}
\renewcommand{\thefigure}{\thechapter.\arabic{figure}}
\renewcommand{\thetable}{\thechapter.\arabic{table}}
\titleformat{\chapter}[hang]
  {\normalfont\Large\bfseries\raggedleft}{EK~\thechapter}{1em}{}[\headingrule]
"""
assert appendix.lstrip().startswith(r"\appendix")
appendix = appendix.replace(r"\appendix", appendix_cfg, 1)

head = read("_ytu_head.tex")
bib = read("_ytu_bib.tex")
tail = read("_ytu_tail.tex")

out = "\n".join([head, main, "", bib, "", appendix, "", tail])

with open(os.path.join(HERE, "thesis_ytu.tex"), "w", encoding="utf-8") as f:
    f.write(out)

print("thesis_ytu.tex yazıldı:", len(out), "karakter")
