# Teslim Öncesi Kontrol Notları

**Tez:** Quantum Grup Yapılarının Python Ortamında Modellenmesi
**Öğrenci:** Taha Berk TEREKLİ — **Danışman:** Prof. Dr. Salih ÇELİK
**Bölüm:** Matematik Bölümü — **Tür:** Lisans Bitirme Tezi — **Tarih:** Haziran, 2026
**Tarih (hazırlık):** 2026-06-04

Teslim dosyaları:
- `Quantum Grup Yapıları - YTU Bitirme Tezi - DUZELTILMIS.docx`
- `Quantum Grup Yapıları - YTU Bitirme Tezi - DUZELTILMIS.pdf`

> Tüm düzeltmeler **kaynak ve build scriptlerinde** yapılmıştır; çıktılar elle
> düzenlenmemiştir. Yeniden üretmek için: `bash thesis/build_ytu.sh`
> (zincir: `_assemble_ytu.py` → `pdflatex ×2` → `_build_ref_docx.py` →
> `_make_docx_tex.py` → `pandoc` → `_postprocess_docx.py`).

---

## 1. Yapılan düzeltmeler

1. **Kapak (FR-1925 uyumu).** Dış ve iç kapağa **YTÜ Fen-Edebiyat Fakültesi logosu**
   eklendi (FR-1925 şablonundan çıkarıldı → `figures/ytu_logo.png`). "T.C. / YILDIZ
   TEKNİK ÜNİVERSİTESİ / FEN-EDEBİYAT FAKÜLTESİ / MATEMATİK BÖLÜMÜ", tez başlığı,
   "Taha Berk TEREKLİ", "LİSANS BİTİRME TEZİ", "Danışman / Prof. Dr. Salih ÇELİK",
   "Haziran, 2026" doğru. Öğrenci numarası **uydurulmadı**; "Öğrenci No: ……………"
   yer tutucusu kullanıldı.
2. **DOCX matematik kayıpları giderildi (asıl hata).** Pandoc'un genişletemediği özel
   makrolar (`\Uq, \sl, \gfrak, \Vn, \Rcheck, \qint, \qfact, \qbin, \hwt, \eps, \cop,
   \Dop, \K,\Q,\C,\Z,\R, \GL,\SL,\End,\id`) `_make_docx_tex.py` içinde düz LaTeX'e
   genişletildi. Artık DOCX'te `Uq(sl2)`, `GLq(2|1)`, `Vn`, `V1⊗V1`, `R`, `Ř`, `τ`,
   `Δ`, `ε`, `S`, `K`, `K⁻¹`, `[n]q`, `R12/R13/R23`, `p(e1)=p(e2)=0`, `p(e3)=1` gibi
   ifadeler **OMML (Word denklemi) olarak dolu** çıkıyor (boş/karesiz). Doğrulandı:
   önsöz ve SİMGE LİSTESİ dahil tüm sembol satırları dolu.
3. **İÇİNDEKİLER gerçek Word alanı.** Eski `[İçindekiler: ... "Alanı Güncelle" deyin.]`
   yer tutucu metni kaldırıldı. Gerçek `TOC` alanı `w:dirty="true"` ile işaretlendi ve
   belge düzeyinde `<w:updateFields val="true"/>` eklendi → Word/LibreOffice dosyayı
   **açarken İÇİNDEKİLER'i gerçek sayfa numaralarıyla otomatik doldurur**.
4. **PDF Türkçe metin katmanı temiz.** `pdftotext` ile doğrulandı: `TEKNİK`, `LİSANS`,
   `Danışman`, `doğrulama`, `İçindekiler`, `Şekil`, `Çizelge`, `Özgeçmiş` doğru;
   `˙ ¸ ˘` gibi bozuk birleşik karakter yok. Fontlar gömülü.
5. **Sayfa numaralandırma.** Ön sayfalar Romen (i, ii, …), Giriş'ten itibaren Arap
   (1, 2, …). İç kapak/önsöz numarası basılmıyor; sayfa numarası alt-ortada.
6. **Terminoloji tek standart: "Çizelge".** Tüm başlık/liste/atıflar "Çizelge"
   (ÇİZELGE LİSTESİ). Numaralandırma bölüm bazlı (`Şekil 8.1`, `Çizelge 10.1`), son
   rakamdan sonra nokta yok, numaradan sonra bir boşluk. Şekil açıklaması altta,
   çizelge açıklaması üstte. *(Karar gerekçesi → bkz. madde 3, manuel kontrol.)*
7. **Başlık biçimleri.** 1. derece 17,5 pt koyu, alt bölüm 14 pt koyu; her sözcüğün
   ilk harfi büyük; başlık numarasında nokta yok; ana bölümler yeni sayfadan başlar.
   Gövde 12 pt Times New Roman, 1,5 satır aralığı, iki yana yaslı, A4, sol 3,5 cm /
   diğer kenarlar 2,5 cm; girintiler temizlendi.
8. **Kaynakça ↔ atıf eşleştirildi.** Önceden 12 kaynaktan yalnız 4'ü atıf alıyordu.
   Metne doğal atıflar eklendi: `\cite{Drinfeld,Jimbo,KS}` (kuantum gruplarının
   doğuşu), `\cite{Kashiwara,HK}` (kristal taban), `\cite{Jones}` (Jones polinomu),
   `\cite{SymPy}`, `\cite{pytest}` (araçlar) ve Çelik & Çelik 2021 makalesine açık
   `\cite{CelikGL21}` atıfları. **Artık 12 kaynağın 12'si de atıf alıyor.** Kaynakça
   APA biçiminde, iki yana yaslı, 1 satır aralıklı.
9. **"Makale" → "tez/çalışma".** Tezin kendisine atıf yapan tüm ifadeler düzeltildi
   ("Makalenin akışı" → "Tezin akışı", "bu makalede" → "bu tezde", "makaleye eşlik
   eden" → "bu teze eşlik eden" vb.). Dış kaynağa (Çelik & Çelik 2021 makalesi) atıf
   yapan iki yer bilinçli olarak "makale" kaldı ve `\cite{CelikGL21}` ile netleştirildi.
10. **Turnitin kontrol notu** bu dosyaya eklendi; teze görünür ekleme yapılmadı.

---

## 2. Kılavuza göre kontrol edilen maddeler (KL-058 / FR-1925)

| Kılavuz maddesi | Durum |
|---|---|
| A4, sol 3,5 / diğer 2,5 cm kenar boşluğu | ✅ |
| 12 pt Times New Roman, 1,5 satır aralığı, iki yana yaslı | ✅ |
| Satır/paragraf sol kenardan, girinti yok | ✅ |
| 1. derece başlık 17,5 pt koyu, alt başlık 14 pt koyu | ✅ |
| Başlıklarda her sözcüğün ilk harfi büyük, numarada nokta yok | ✅ |
| Ana bölümler yeni sayfadan başlar | ✅ |
| Ön sayfa Romen, Giriş'ten itibaren Arap rakamı | ✅ |
| Şekil açıklaması altta, çizelge açıklaması üstte, ortalı | ✅ |
| Bölüm bazlı numaralandırma (Şekil/Çizelge N.M) | ✅ |
| Ön sayfa sırası (önsöz→içindekiler→simge→kısaltma→şekil→çizelge→özet→abstract) | ✅ |
| Özet sonunda **Anahtar Kelimeler** (koyu) | ✅ |
| Kaynakça APA, iki yana yaslı, 1 satır aralığı | ✅ |
| Kaynakçadaki her kaynak metinde atıf alıyor | ✅ |
| EKLER ve ÖZGEÇMİŞ bölümleri var | ✅ |
| İnternet kaynaklarında erişim tarihi | ✅ (SymPy, pytest) |

---

## 3. Hâlâ manuel kontrol gerektiren noktalar

1. **Öğrenci numarası** — bilinmiyor; kapakta "Öğrenci No: ……………" yer tutucusu var.
   **Gerçek numara elle girilmeli** (`_ytu_head.tex` içindeki `\OgrenciNo` makrosu).
2. **Çizelge / Tablo terminolojisi kararı** — KL-058 hem "Çizelge" hem "Tablo
   Listesi" tanımlar; FR-1925 "Tablo" kullanır. Bu tezde **"Çizelge"** seçildi
   (mevcut metnin tamamı bu terimi kullanıyordu, KL-058'in ağırlıklı kullanımı).
   Bölüm "Tablo" isterse `_assemble_ytu.py` ve `_ytu_head.tex` içinde terim
   değiştirilerek yeniden üretilmeli — **danışman onayı önerilir.**
3. **PDF kaynağı / sayfa numarası tutarlılığı** — Teslim PDF'i **LaTeX'ten** üretildi
   (en yüksek matematik/kod dizgi kalitesi, temiz Türkçe metin katmanı; 47 sayfa).
   DOCX ise pandoc/Word ile farklı dizgilendiğinden (≈55 sayfa) **İÇİNDEKİLER sayfa
   numaraları iki dosya arasında birebir aynı olmayabilir.** İçerik birebir aynıdır.
   Eğer sayfa numaralarının DOCX ile **tam** eşleşmesi şartsa, PDF'i DOCX'ten
   (LibreOffice/Word ile) üretmeyi tercih edin — `build_ytu.sh` adım 9 LibreOffice QA
   PDF'ini `/tmp/ytu_qa/` altına üretir. **Tercih danışmana bırakıldı.**
4. **İÇİNDEKİLER ilk açılışta güncellenir** — DOCX'i Word'de açınca alanlar otomatik
   güncellenir (gerekirse tümünü seçip **F9**). Teslimden önce bir kez açıp
   güncelleyip kaydetmeniz önerilir.
5. **Kapak dikey yerleşimi (DOCX)** — DOCX kapağında içerik doğru ve ortalı, ancak
   LaTeX PDF kapağındaki geniş dikey boşluklar pandoc'ta sıkışmıştır. İsteğe bağlı
   olarak Word'de kapak satır aralıkları açılabilir (PDF kapağı tam FR-1925
   düzenindedir).
6. **Logo doğrulaması** — Kapak logosu FR-1925 şablonundaki resmî YTÜ Fen-Edebiyat
   logosudur; istenirse bölümün güncel logosuyla değiştirilebilir.

---

## 4. Turnitin uyarısı

> **Turnitin benzerlik raporu ayrıca alınmalı ve benzerlik indeksi %30'u
> aşmamalıdır** (KL-058). Dosyalar içinde Turnitin raporu bulunmadığından benzerlik
> oranı **tahmin edilmemiştir**; teslim öncesi rapor mutlaka alınmalıdır.

---

## 5. DOCX / PDF tutarlılık kontrolü

- İçerik **birebir aynı kaynaktan** üretilir (`thesis.tex` → ortak gövde).
- Matematik: PDF'te LaTeX dizgisi, DOCX'te OMML (Word denklemi) — ikisi de tam ve
  okunabilir; DOCX'te boş/karesiz sembol yok (doğrulandı).
- Türkçe karakterler her iki çıktıda da doğru.
- **Sayfa sayısı farkı:** LaTeX PDF 47 sayfa, DOCX (Word/LibreOffice dizgisi) ≈55
  sayfa — farklı dizgi motorları nedeniyle beklenen durum (bkz. madde 3.3).

---

## 6. Kaynakça ve atıf kontrol sonucu

- **Tanımlı 12 kaynak:** ChariPressley, CelikGL21, Drinfeld, HK, Jimbo, Jones,
  Kashiwara, Kassel, KS, Lusztig, SymPy, pytest.
- **Metinde atıf alan:** 12/12 ✅ (`\cite` anahtarları ⊇ `\bibitem` anahtarları;
  pdflatex'te "undefined citation" uyarısı yok).
- Kaynakçada **metinde kullanılmayan kayıt kalmadı.** "Kontrol gerektirir" listesi
  oluşturmaya gerek kalmadı.
- Erişim tarihleri: SymPy/pytest internet kaynaklarında mevcut; **gelecek tarih
  yok** (en geç 3 Haziran 2026; hazırlık tarihi 4 Haziran 2026).
- Biçim: tek tip **APA**, iki yana yaslı, 1 satır aralığı.

---

## 7. Şekil / Çizelge / Tablo kontrol sonucu

- **Şekiller (9):** 4.1, 8.1, 8.2, 8.3, 9.1, 9.2, 9.3, 9.4, 9.5 — ŞEKİL LİSTESİ ile
  metindeki başlıklar eşleşiyor.
- **Çizelgeler (5):** 3.1, 6.1, 9.1, 10.1, B.1 — ÇİZELGE LİSTESİ ile eşleşiyor.
- Numaralandırma bölüm bazlı (`N.M`), son rakamdan sonra nokta yok, numaradan sonra
  bir boşluk; şekil açıklaması altta, çizelge açıklaması üstte, ortalanmış.
- Terminoloji tüm belgede tek tip "Şekil" / "Çizelge".
