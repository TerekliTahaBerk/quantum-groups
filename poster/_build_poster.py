#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""YTÜ poster şablonunu (slide1.xml) tez içeriğiyle doldurur. Konum/renk/font korunur."""
import os
HERE = os.path.dirname(os.path.abspath(__file__))
SLIDE = os.path.join(HERE, "unpacked/ppt/slides/slide1.xml")

NAVY = ('<a:solidFill><a:schemeClr val="accent1"><a:lumMod val="50000"/>'
        '</a:schemeClr></a:solidFill>')

def esc(t):
    return t.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")

def head(t, sz=2800):
    return (f'<a:p><a:pPr algn="ctr"><a:lnSpc><a:spcPct val="120000"/></a:lnSpc>'
            f'<a:spcBef><a:spcPts val="600"/></a:spcBef></a:pPr>'
            f'<a:r><a:rPr lang="tr-TR" sz="{sz}" b="1" dirty="0">{NAVY}</a:rPr>'
            f'<a:t>{esc(t)}</a:t></a:r></a:p>')

def body(t, sz=2000, bold_label=None):
    runs = ""
    if bold_label:
        runs += (f'<a:r><a:rPr lang="tr-TR" sz="{sz}" b="1" dirty="0"/>'
                 f'<a:t>{esc(bold_label)} </a:t></a:r>')
    runs += f'<a:r><a:rPr lang="tr-TR" sz="{sz}" dirty="0"/><a:t>{esc(t)}</a:t></a:r>'
    return f'<a:p><a:pPr algn="just"/>{runs}</a:p>'

def bullet(t, sz=2000):
    return (f'<a:p><a:pPr marL="285750" indent="-285750" algn="just">'
            f'<a:buFont typeface="Arial"/><a:buChar char="•"/></a:pPr>'
            f'<a:r><a:rPr lang="tr-TR" sz="{sz}" dirty="0"/><a:t>{esc(t)}</a:t></a:r></a:p>')

def txbody(paras, autofit=True):
    fit = "<a:spAutoFit/>" if autofit else "<a:normAutofit/>"
    return (f'<p:txBody><a:bodyPr wrap="square" lIns="180000" tIns="72000" '
            f'rIns="180000" bIns="72000" rtlCol="0">{fit}</a:bodyPr><a:lstStyle/>'
            + "".join(paras) + "</p:txBody>")

def sp(sid, name, x, y, cx, cy, paras, border=True, autofit=True):
    ln = ('<a:ln><a:solidFill><a:schemeClr val="tx1"/></a:solidFill></a:ln>'
          if border else "")
    return f'''<p:sp><p:nvSpPr><p:cNvPr id="{sid}" name="{name}"/>
<p:cNvSpPr txBox="1"/><p:nvPr/></p:nvSpPr>
<p:spPr><a:xfrm><a:off x="{x}" y="{y}"/><a:ext cx="{cx}" cy="{cy}"/></a:xfrm>
<a:prstGeom prst="rect"><a:avLst/></a:prstGeom><a:noFill/>{ln}</p:spPr>
{txbody(paras, autofit)}</p:sp>'''

def title_line(t, sz):
    return (f'<a:p><a:pPr algn="ctr"><a:lnSpc><a:spcPct val="120000"/></a:lnSpc></a:pPr>'
            f'<a:r><a:rPr lang="tr-TR" altLang="tr-TR" sz="{sz}" b="1" dirty="0">{NAVY}'
            f'<a:latin typeface="Calibri"/><a:cs typeface="Calibri"/></a:rPr>'
            f'<a:t>{esc(t)}</a:t></a:r></a:p>')

def caption(sid, t, x, y, cx):
    return sp(sid, f"cap{sid}", x, y, cx, 700000, [
        f'<a:p><a:pPr algn="ctr"/><a:r><a:rPr lang="tr-TR" sz="1800" i="1" dirty="0"/>'
        f'<a:t>{esc(t)}</a:t></a:r></a:p>'], border=False, autofit=True)

def pic(pid, name, rid, x, y, cx, cy):
    return f'''<p:pic><p:nvPicPr><p:cNvPr id="{pid}" name="{name}"/>
<p:cNvPicPr><a:picLocks noChangeAspect="1"/></p:cNvPicPr><p:nvPr/></p:nvPicPr>
<p:blipFill><a:blip r:embed="{rid}"/><a:stretch><a:fillRect/></a:stretch></p:blipFill>
<p:spPr><a:xfrm><a:off x="{x}" y="{y}"/><a:ext cx="{cx}" cy="{cy}"/></a:xfrm>
<a:prstGeom prst="rect"><a:avLst/></a:prstGeom></p:spPr></p:pic>'''

# ===================== İÇERİK =====================
# --- Başlık bloğu (id=11), tam genişlik ---
title = (f'''<p:sp><p:nvSpPr><p:cNvPr id="11" name="Baslik"/><p:cNvSpPr/><p:nvPr/></p:nvSpPr>
<p:spPr><a:xfrm><a:off x="875174" y="2820000"/><a:ext cx="23610696" cy="2700000"/></a:xfrm>
<a:prstGeom prst="rect"><a:avLst/></a:prstGeom></p:spPr>
<p:txBody><a:bodyPr wrap="square"><a:spAutoFit/></a:bodyPr><a:lstStyle/>'''
    + title_line("2025–2026 Bahar Yarıyılı        MATEMATİK BÖLÜMÜ", 4000)
    + title_line("Quantum Grup Yapılarının Python Ortamında Modellenmesi", 3600)
    + title_line("Taha Berk TEREKLİ        ……………", 2400)
    + title_line("Danışman: Prof. Dr. Salih ÇELİK", 2400)
    + "</p:txBody></p:sp>")

# --- ÖZET (id=12), tam genişlik bant ---
ozet = sp(12, "Ozet", 875174, 5865106, 23610696, 2052000, [
    f'<a:p><a:pPr algn="ctr"><a:lnSpc><a:spcPct val="120000"/></a:lnSpc></a:pPr>'
    f'<a:r><a:rPr lang="tr-TR" sz="3000" b="1" dirty="0">{NAVY}</a:rPr><a:t>ÖZET</a:t></a:r></a:p>',
    body("Bu çalışma, Drinfeld–Jimbo kuantum grubu Uq(sl₂) ve GLq(2|1) kuantum "
         "süpergrubu için temel temsil-teorik ve Yang–Baxter tipi bağıntıları "
         "Python/SymPy ortamında yeniden üretilebilir biçimde modeller. Yöntemin çekirdeği, "
         "her cebirsel eşitliği açık sonlu boyutlu temsiller üzerinde bir kalıntı matrisine "
         "indirgemek ve matrisin tüm girdilerini sembolik olarak sadeleştirip sıfır olup "
         "olmadığını denetlemektir. Raporlanan her eşitlik pytest tabanlı bir teste bağlıdır."),
])

# --- SOL SÜTUN (id=13) ---
left = sp(13, "SolSutun", 875173, 8287432, 11343813, 23863831, [
    head("GİRİŞ"),
    body("Kuantum gruplar, evrensel sarmalayıcı cebir U(g)’nin tek-parametreli (q) "
         "deformasyonu olan; ne değişmeli ne de eş-değişmeli Hopf cebirleridir. "
         "Kalbinde, integrallenebilir sistemler ile düğüm değişmezlerini aynı çatıda "
         "buluşturan Yang–Baxter denklemi ve onun çözümü R-matrisi yatar."),
    head("AMAÇ ve KAPSAM"),
    body("Amaç yeni bir kuantum grup tanımlamak değil; bilinen Uq(sl₂) kuantum grubu ile "
         "GLq(2|1) kuantum süpergrubunun temel yapılarını sonlu boyutlu temsiller üzerinde "
         "modüler, test edilebilir ve yeniden üretilebilir bir sembolik doğrulama altyapısına "
         "dönüştürmektir."),
    head("KURAMSAL TEMEL"),
    body("Uq(sl₂); E, F, K, K⁻¹ üreteçleri ve dört tanımlayıcı bağıntı ile "
         "verilen bir Hopf cebridir:"),
    f'<a:p><a:pPr algn="ctr"/><a:r><a:rPr lang="tr-TR" sz="2000" b="1" dirty="0"/>'
    f'<a:t>KEK⁻¹ = q²E, KFK⁻¹ = q⁻²F, [E,F] = (K−K⁻¹)/(q−q⁻¹)</a:t></a:r></a:p>',
    body("(n+1)-boyutlu indirgenemez temsil Vn açık matrislerle kurulur; E katsayıları "
         "q-tamsayı çarpımları [k]q·[n−k+1]q ile q-deforme olur ve q→1 limitinde "
         "klasik sl₂ temsili geri gelir."),
    head("YÖNTEM"),
    body("Her cebirsel eşitlik, açık temsiller üzerinde bir kalıntı matrisine indirgenir; "
         "matrisin tüm girdileri SymPy ile sembolik olarak sadeleştirilip sıfıra inip inmediği "
         "denetlenir. Yalnızca SymPy’ye bağlı modüler quantum_group paketi geliştirilmiş; "
         "her doğrulama bir pytest testine bağlanmıştır."),
])

# --- SAĞ SÜTUN (id=17) ---
right = sp(17, "SagSutun", 12885245, 8287432, 11600625, 18600000, [
    head("BULGULAR"),
    bullet("Uq(sl₂) için dört tanımlayıcı bağıntı ve dokuz Hopf aksiyomu seçilen "
           "temsillerde sembolik olarak doğrulandı."),
    bullet("Tensör çarpımı Vm⊗Vn üzerinde eş-çarpımdan gelen eylem kuruldu; "
           "Clebsch–Gordan en yüksek ağırlık vektörleri q-deforme katsayılarla elde edildi."),
    bullet("V₁⊗V₁ üzerinde R-matrisi, kuantum Yang–Baxter denklemi "
           "(R₁₂R₁₃R₂₃ = R₂₃R₁₃R₁₂), örgü bağıntısı ve "
           "Hecke skein özdeşliği doğrulandı."),
    head("GLq(2|1) GRADED YANG–BAXTER"),
    body("Salih Çelik ve Sultan A. Çelik’in tanıttığı GLq(2|1) süpergrubunun 9×9 "
         "R-matrisi bağımsız kodlandı. p(e₁)=p(e₂)=0, p(e₃)=1 parite konvansiyonu ve "
         "süper permütasyonla R₁₃ yerleşimi kuruldu; graded Yang–Baxter kalıntısının "
         "tüm 27×27 girdisinin sıfır olduğu sembolik olarak doğrulandı."),
    head("SONUÇ"),
    body("Yüksek boyutlu Yang–Baxter tipi hesaplar, elle yürütülen cebirsel "
         "manipülasyonlardan test edilebilir ve yeniden üretilebilir sembolik doğrulama "
         "prosedürlerine taşınabilir. Parite bilgisi matris düzeyine gömülerek en hata-açık "
         "adım otomatikleştirilmiştir."),
], autofit=False)

# --- KAYNAKÇA (id=22) ---
kaynak = sp(22, "Kaynakca", 12885245, 29621420, 11586246, 2160000, [
    f'<a:p><a:pPr algn="ctr"><a:lnSpc><a:spcPct val="120000"/></a:lnSpc></a:pPr>'
    f'<a:r><a:rPr lang="tr-TR" sz="3000" b="1" dirty="0">{NAVY}</a:rPr><a:t>KAYNAKÇA</a:t></a:r></a:p>',
    body("Çelik, S., Çelik, S. A., (2021). “A New Quantum Supergroup and its Gauss "
         "Decomposition”, Reports on Mathematical Physics, 88(2), 259–272.", sz=1800, bold_label="[1]"),
    body("Kassel, C., (1995). Quantum Groups, Springer, New York.", sz=1800, bold_label="[2]"),
    body("Chari, V., Pressley, A., (1994). A Guide to Quantum Groups, Cambridge "
         "University Press, Cambridge.", sz=1800, bold_label="[3]"),
])

# --- Logo (id=3) ---
logo = pic(3, "Logo", "rId4", 6126984, 591573, 14981279, 2137815)

# --- ŞEKİLLER (boş alt alanları doldurur, sütun çerçeveleri içinde) ---
# SOL sütun: Uq R-matrisi + ağırlık diyagramı
LW = 9400000
lx = 875173 + (11343813 - LW)//2
figA = pic(40, "figA", "rId7", lx, 18450000, LW, int(LW/1.778))
capA = caption(41, "Şekil 1. V₁⊗V₁ üzerinde Drinfeld R-matrisi ve örgülü Ř = τR.",
               lx, 18450000 + int(LW/1.778) + 60000, LW)
figB = pic(42, "figB", "rId8", lx, 25250000, LW, int(LW/2.141))
capB = caption(43, "Şekil 2. V₄ temsilinin ağırlık diyagramı; F yükseltir, E q-katsayılarla taşır.",
               lx, 25250000 + int(LW/2.141) + 60000, LW)

# SAĞ sütun: 27×27 graded YBE + 9×9 R-matrisi
RW = 9400000
rx = 12885245 + (11600625 - RW)//2
figC = pic(44, "figC", "rId5", rx, 19000000, RW, int(RW/2.614))
capC = caption(45, "Şekil 3. Graded Yang–Baxter’in iki tarafı (27×27) özdeş; kalıntı sıfırdır.",
               rx, 19000000 + int(RW/2.614) + 60000, RW)
RW2 = 5200000
rx2 = 12885245 + (11600625 - RW2)//2
figD = pic(46, "figD", "rId6", rx2, 23450000, RW2, int(RW2/1.137))
capD = caption(47, "Şekil 4. GLq(2|1) için 9×9 R-matrisinin girdi-tipi haritası.",
               12885245, 23450000 + int(RW2/1.137) + 60000, 11600625)

shapes = "\n".join([title, ozet, left, right, kaynak, logo,
                    figA, capA, figB, capB, figC, capC, figD, capD])

slide = f'''<?xml version="1.0" encoding="utf-8"?>
<p:sld xmlns:a="http://schemas.openxmlformats.org/drawingml/2006/main" xmlns:r="http://schemas.openxmlformats.org/officeDocument/2006/relationships" xmlns:p="http://schemas.openxmlformats.org/presentationml/2006/main">
  <p:cSld>
    <p:spTree>
      <p:nvGrpSpPr><p:cNvPr id="1" name=""/><p:cNvGrpSpPr/><p:nvPr/></p:nvGrpSpPr>
      <p:grpSpPr><a:xfrm><a:off x="0" y="0"/><a:ext cx="0" cy="0"/><a:chOff x="0" y="0"/><a:chExt cx="0" cy="0"/></a:xfrm></p:grpSpPr>
      {shapes}
    </p:spTree>
  </p:cSld>
  <p:clrMapOvr><a:masterClrMapping/></p:clrMapOvr>
</p:sld>'''

with open(SLIDE, "w", encoding="utf-8") as f:
    f.write(slide)
print("slide1.xml yazıldı:", len(slide), "karakter")
