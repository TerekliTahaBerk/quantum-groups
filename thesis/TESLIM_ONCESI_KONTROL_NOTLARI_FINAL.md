# Teslim Öncesi Kontrol Notları — FINAL

**Tez:** Quantum Grup Yapılarının Python Ortamında Modellenmesi
**Öğrenci:** Taha Berk TEREKLİ — **Danışman:** Prof. Dr. Salih ÇELİK
**Bölüm:** Matematik Bölümü — **Tür:** Lisans Bitirme Tezi — **Tarih:** Haziran, 2026
**Hazırlık tarihi:** 2026-06-04

### Teslim dosyaları
- `Quantum Grup Yapıları - YTU Bitirme Tezi - FINAL.docx` — ana teslim DOCX (İÇİNDEKİLER dolu)
- `Quantum Grup Yapıları - YTU Bitirme Tezi - FINAL.pdf` — **ana teslim PDF (LaTeX kaynaklı, 47 s.)**
- `Quantum Grup Yapıları - YTU Bitirme Tezi - FINAL-DOCX-RENDER.pdf` — alternatif PDF (DOCX'ten, ~58 s.)
- `TESLIM_ONCESI_KONTROL_NOTLARI_FINAL.md` — bu dosya

> Tüm düzeltmeler kaynak + build pipeline'da kalıcıdır. Yeniden üretim: `bash thesis/build_ytu.sh`
> Zincir: `_assemble_ytu.py` → `pdflatex ×2` → `_build_ref_docx.py` → `_make_docx_tex.py` →
> `pandoc` → `_postprocess_docx.py` → **`_materialize_toc.py` (LibreOffice ile İÇİNDEKİLER doldurma)**.

---

## 1. Yapılan son düzeltmeler

1. **İÇİNDEKİLER artık görünür şekilde dolu.** Word/LibreOffice alan güncellemesine
   bağımlı kalmamak için `_postprocess_docx.py` statik, görünür İçindekiler satırları
   yazar. Sayfa numaraları ve başlıklar `word/document.xml` içinde **gerçek metindir**.
2. **Başlıklardaki matematik metne çevrildi.** Heading'lerdeki OMML Word İÇİNDEKİLER
   alanına geçmediğinden, başlık matematiği düz metne dönüştürüldü
   (`_make_docx_tex.py`): "3 Kuantum Grup **Uq(sl2)**'nin Tanımı", "4 **Uq(sl2)**'nin
   Sonlu Boyutlu Temsil Teorisi", "9 **GLq(2|1)** için Graded...", "3.1 **q**-Deformasyon",
   "10.5 ...(**V2** örneği)". Hem başlıkta hem İÇİNDEKİLER'de okunur.
3. **FINAL adlı teslim dosyaları** üretildi (eski DUZELTILMIS dosyaları korundu).
4. Önceki turdaki tüm düzeltmeler korundu: kapak+logo, DOCX matematik (OMML),
   makale→tez, kaynakça-atıf eşleşmesi, Çizelge terminolojisi, başlık/sayfa düzeni.

---

## 2. DOCX İçindekiler güncelleme sonucu — ✅ GEÇTİ

`word/document.xml` içinde İÇİNDEKİLER **dolu ve statik metin** olarak yer alır.
Görünür içerik render ile doğrulandı:

```
ÖNSÖZ 3 · İÇİNDEKİLER 4 · SİMGE LİSTESİ 6 · KISALTMA LİSTESİ 9 · ŞEKİL LİSTESİ 10 ·
ÇİZELGE LİSTESİ 11 · ÖZET 12 · ABSTRACT 13 · 1 Giriş 14 · 2 Teorik Arka Plan 16 ·
3 Kuantum Grup Uq(sl2)'nin Tanımı 19 · 4 Uq(sl2)'nin Sonlu Boyutlu Temsil Teorisi 22 ·
5 Kristal Tabanlar 24 · 6 Yazılım Mimarisi 25 · 7 Tensör Çarpımı ve C–G Ayrışımı 29 ·
8 R-Matrisi ve Yang–Baxter Denklemi 32 · 9 GLq(2|1) için Graded Y–B Doğrulaması 36 ·
10 Klasik, Kuantum ve Birim Kök Limitleri 44 · 11 Sonuç ve Öneriler 48 ·
KAYNAKLAR 50 · EKLER 51 · EK A 52 · EK B 56 · ÖZGEÇMİŞ 57
```

Sayfa numaraları DOCX'in kendi dizgisine göredir. DOCX `render_docx.py` ile 57 sayfa
PNG/PDF olarak render edildi; İçindekiler sayfası dolu ve görünür.

---

## 3. Öğrenci numarası durumu — ✅ TAMAMLANDI

Gerçek öğrenci numarası kullanıcı tarafından sağlandı ve `_ytu_head.tex` içindeki
`\OgrenciNo` makrosuna işlendi. Kapakta (hem dış hem iç kapak) aynı bilgi görünür:

> `Öğrenci No: 22025083`

DOCX ve PDF metin katmanlarında `22025083` bulundu; öğrenci no yer tutucusu kalmadı
(`qa_final.py` ile doğrulandı).

---

## 4. DOCX matematik görsel QA sonucu — ✅ GEÇTİ

- DOCX'te 637 OMML denklemi; ÖNSÖZ'de `Uq(sl2)` ve `GLq(2|1)` dolu (doğrulandı).
- SİMGE LİSTESİ'ndeki tüm semboller görsel render'da dolu: `Uq(sl2)`, `sl2`, `U(g)`,
  `E,F,K,K⁻¹`, `q`, `[n]q`, `Vn`, `v0`, `Δ`, `ε`, `S`, `R`, `Ř`, `τ`, `⊗`, `GLq(2|1)`,
  `p(ei)`, `P`, `Rij`, `B(n)`, `ζ`.
- Görsel QA: DOCX → PDF (LibreOffice) render edildi; R-matrisi/Yang–Baxter bölümünde
  `R12, R13, R23`, `⊗`, `τ`, `R12R23=R23R13R12`, "8×8 sıfır matris", `p(e1)=p(e2)=0`,
  `p(e3)=1` ve kod blokları **görünür** (boş/karesiz değil).
- Not: ham `pdftotext`/python-docx parse'ında bazı OMML run'ları boş görünebilir; bu
  bir parser davranışıdır, görsel render'da matematik tamdır.

---

## 5. PDF Türkçe metin katmanı sonucu — ✅ GEÇTİ (normalize ile)

`pdftotext` + Unicode **NFC normalizasyonu** sonrası tüm hedef kelimeler doğru bulunur:
`TEKNİK, ÜNİVERSİTESİ, FEN-EDEBİYAT, LİSANS, Danışman, İÇİNDEKİLER, ŞEKİL, ÇİZELGE,
ÖZGEÇMİŞ, doğrulama, bağıntı, çalışma` (12/12 OK).

**Önemli not:** pdflatex T1 fontunda `İ, ş, ğ, ç…` ham extraction'da birleşik
(combining) karakter dizisi olarak çıkabilir; bu nedenle **arama/kopyalamadan önce NFC
normalizasyonu uygulanmalıdır.** Normalize sonrası arama sorunsuzdur ve **görsel PDF'te
karakter bozukluğu yoktur** (kapak ve gövde gözle doğrulandı). Bozuk `˙ ¸ ˘` ayrık
gösterimi (ör. `TEKN˙IK`) yoktur.

---

## 6. PDF/DOCX sayfa sayısı ve sayfa numarası tutarlılığı

- **Ana teslim PDF (LaTeX):** 47 sayfa — matematik/kod dizgisi en sağlam tercih.
- **DOCX (Word/LibreOffice dizgisi):** ~58 sayfa; İÇİNDEKİLER bu dizgiye göre dolu.
- İki çıktının **içeriği birebir aynı kaynaktandır**; ancak farklı dizgi motorları
  nedeniyle **sayfa numaraları birebir aynı değildir.**
- **Karar:** Ana teslim PDF olarak **LaTeX PDF önerilir** (madde 6'daki kurum tercihi).
  Kurum DOCX ile PDF sayfa numaralarının **birebir** aynı olmasını isterse, birlikte
  verilen `…- FINAL-DOCX-RENDER.pdf` (DOCX'ten üretilen, sayfa numaraları DOCX ile
  aynı) **alternatif teslim PDF'i** olarak kullanılabilir.

---

## 7. Kaynakça ve atıf kontrolü — ✅ GEÇTİ

- 12 tanımlı kaynak, 12 atıf anahtarı; **atıfsız kaynak yok, kaynaksız atıf yok**
  (`\cite` kümesi = `\bibitem` kümesi). pdflatex'te undefined citation uyarısı yok.
- "makale/makalede/makalenin" ifadeleri **yalnızca dış makaleye** (Çelik & Çelik 2021)
  atıfta kaldı ve `\cite{CelikGL21}` ile netleştirildi (2 yer). Tezin kendisine atıf
  yapan tüm ifadeler "tez/çalışma/bu tez/bu çalışmada" yapıldı. (Build yorum satırı
  hariç — çıktıya girmez.)
- Kaynakça APA, iki yana yaslı, 1 satır aralığı. İnternet kaynaklarında (SymPy, pytest)
  erişim tarihi var; gelecek tarih yok.

---

## 8. Şekil/Çizelge kontrolü — ✅ GEÇTİ

- Terminoloji: **Çizelge** (korundu). `ÇİZELGE LİSTESİ` mevcut.
- Şekiller (9): 4.1, 8.1, 8.2, 8.3, 9.1, 9.2, 9.3, 9.4, 9.5 — `Şekil N.M`, açıklama altta.
- Çizelgeler (5): 3.1, 6.1, 9.1, 10.1, B.1 — `Çizelge N.M`, açıklama üstte.
- Son rakamdan sonra nokta yok; numaradan sonra bir boşluk; liste başlıkları metindeki
  açıklamalarla eşleşiyor.

---

## 9. Başlık ve sayfa düzeni kontrolü — ✅ GEÇTİ

- A4; sol kenar 3,5 cm, diğer kenarlar 2,5 cm.
- Ana metin Times New Roman 12 pt, 1,5 satır aralığı, iki yana yaslı.
- 1. derece başlık 17,5 pt koyu; alt başlık 14 pt koyu; her sözcüğün ilk harfi büyük;
  başlık numarasında nokta yok; ana bölümler yeni sayfadan başlıyor.
- Ön sayfalar Romen (i, ii…), Giriş'ten itibaren Arap rakamı; sayfa no alt-ortada.
- Kapak FR-1925'e uygun: **YTÜ Fen-Edebiyat logosu**, "MATEMATİK BÖLÜMÜ", tez başlığı,
  öğrenci ve öğrenci no, "LİSANS BİTİRME TEZİ", "Danışman / Prof. Dr. Salih ÇELİK",
  "Haziran, 2026". Dış ve iç kapak aynı.
- Küçük not: DOCX kapağında dikey boşluklar PDF kapağına göre daha sıkışıktır (içerik
  ve sıra tam); tam FR-1925 dikey yerleşimi için PDF kapağı referanstır.

---

## 10. Turnitin uyarısı

> **Turnitin benzerlik raporu ayrıca alınmalı ve benzerlik indeksi %30'u aşmamalıdır.
> Dosyalar içinde Turnitin raporu bulunmadığından oran tahmin edilmemiştir.**

---

## Manuel tamamlanması gerekenler (özet)
1. **Turnitin raporu** — ayrıca alınmalı (%30 sınırı).
2. **PDF kaynağı tercihi** — kurum birebir sayfa eşleşmesi isterse FINAL-DOCX-RENDER.pdf
   kullanılmalı (madde 6).
3. İsteğe bağlı: Word'de İÇİNDEKİLER'i bir kez F9 ile yenilemek (zaten dolu).
