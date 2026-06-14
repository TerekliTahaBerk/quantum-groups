# PDF-FINAL Kontrol Notları

Dosya: `Quantum Grup Yapıları - YTU Bitirme Tezi - PDF-FINAL.pdf`

## 1. Yapılan düzeltmeler

- PDF üretimi için ayrı ve yalnızca PDF hedefleyen `build_pdf_final.sh` akışı oluşturuldu.
- PDF metin katmanındaki Türkçe karakterlerin doğru çıkması için LuaLaTeX/Times New Roman tabanlı üretim kullanıldı.
- Uzun kod yolu ve uzun tablo başlığı kaynak LaTeX içinde düzenlenerek final logdaki `Overfull \hbox` uyarıları giderildi.
- EK A metni daha doğal bir tez eki üslubuyla yeniden düzenlendi; teknik komutlar korundu, kılavuz/şablon hissi veren ifadeler sadeleştirildi.
- FR-1925 kapak şablonundaki YTÜ Fen-Edebiyat Fakültesi logo görseli ve kapak satır sırası kullanıldı.
- `ÇİZELGE LİSTESİ/Çizelge` terminolojisi FR-1925 şablonuna uygun olarak `TABLO LİSTESİ/Tablo` biçimine alındı.
- Kılavuzdaki girintisiz paragraf ve soldan başlayan denklem kuralı için LaTeX kaynak ayarları güncellendi.
- Kullanıcı isteğiyle `ABSTRACT` ön sayfası kaldırıldı; Türkçe `ÖZET` bölümü korundu.
- PDF için otomatik kontrol betiği `qa_pdf_final.py` eklendi.
- Görsel QA için örnek sayfa PNG'leri `qa_pdf_pages/` dizinine üretildi.

## 2. Kılavuza göre PDF format kontrolü

- Kağıt boyutu: A4.
- PDF sayfa bilgisi: `595.276 x 841.89 pts (A4)`.
- Sayfa sayısı: 47.
- Üretici: LuaTeX 1.24.0.
- Ana metin Times/Times New Roman uyumlu serif font ile üretildi.
- Sayfa düzeni LaTeX kaynak ayarlarından korunmuştur: sol kenar 3.5 cm, diğer kenarlar 2.5 cm, 12 punto ve 1.5 satır aralığı.

## 3. Kapak kontrolü

- Kapakta FR-1925 şablonundaki YTÜ Fen-Edebiyat Fakültesi logo görseli ve Matematik Bölümü satırı yer alıyor.
- Tez başlığı: `Quantum Grup Yapılarının Python Ortamında Modellenmesi`.
- Öğrenci adı: `Taha Berk TEREKLİ`.
- Öğrenci numarası: `22025083` (FR-1925 şablonundaki gibi etiketsiz).
- Tez türü: `LİSANS BİTİRME TEZİ`.
- Danışman: `Prof. Dr. Salih ÇELİK`.
- Tarih: `Haziran, 2026`.
- Kapak görsel QA dosyası: `qa_pdf_pages/cover.png`.

## 4. Sayfa düzeni kontrolü

- Kapakta sayfa numarası görünmüyor.
- Ön sayfalar roman numaralandırmayla ilerliyor.
- Ana metin `Giriş` bölümüyle Arap rakamı sayfa numaralandırmasına geçiyor.
- Görsel kontrol edilen örnek sayfalarda taşma, üst üste binme veya kenar boşluğu ihlali görülmedi.

## 5. Ön sayfalar ve İçindekiler kontrolü

- `ÖNSÖZ`, `İÇİNDEKİLER`, `SİMGE LİSTESİ`, `KISALTMA LİSTESİ`, `ŞEKİL LİSTESİ`, `TABLO LİSTESİ` ve `ÖZET` bölümleri PDF içinde bulunuyor.
- İçindekiler tezdeki bölüm sayısı nedeniyle birden fazla sayfaya düzgün şekilde yayılmıştır.
- Görsel QA dosyaları: `qa_pdf_pages/icindekiler.png`, `qa_pdf_pages/simge-listesi.png`, `qa_pdf_pages/ozet.png`.

## 6. Başlık ve numaralandırma kontrolü

- Ana bölümler `1 Giriş` ile başlıyor ve sıralı ilerliyor.
- Bölüm/alt bölüm numaraları otomatik LaTeX sayaçlarıyla üretildi.
- PDF metin katmanında `??` veya çözülmemiş referans belirtisi bulunmadı.

## 7. Tanım/Teorem/Referans kontrolü

- Tez içindeki matematiksel yapı başlıkları, tanımlar ve referanslar LaTeX kaynaklarından tekrar derlenerek üretildi.
- Otomatik QA betiği kaynak dosyada atıf/kaynak eşleşmesini kontrol etti.
- Final derlemede çözülmemiş referans veya çözülmemiş atıf uyarısı kalmadı.

## 8. Matematik dizgisi kontrolü

- `U_q(sl_2)`, `GL_q(2|1)`, R-matrisi, Yang-Baxter bağıntıları ve tensör çarpımı ifadeleri PDF içinde okunur durumdadır.
- Matematiksel simgeler görsel olarak kontrol edilen sayfalarda taşma üretmedi.
- LuaLaTeX üretimiyle Türkçe metin katmanı korunurken matematik dizgisi de LaTeX tarafından yeniden üretildi.

## 9. Şekil/Tablo kontrolü

- Şekil ve tablo listeleri PDF içinde bulunuyor.
- Örnek şekil sayfası `qa_pdf_pages/sekil-4-1.png` ile kontrol edildi.
- Örnek tablo sayfası `qa_pdf_pages/tablo-3-1.png` ile kontrol edildi.
- Uzun tablo başlığı kaynakta düzenlenerek final PDF'de taşma yapmayacak hale getirildi.

## 10. Kod blokları ve ekler kontrolü

- Kod içeren uzun yol ifadesi kaynakta satır kırılmasına uygun biçime getirildi.
- Ek A ve Ek B bölümleri PDF içinde yer alıyor.
- EK A başlangıç sayfası ayrıca `qa_pdf_pages/ek-a.png` olarak görsel kontrolden geçirildi.
- Kod blokları ve ek sayfalarında çözülmemiş sayaç ya da referans göstergesi bulunmadı.

## 11. Kaynakça ve atıf kontrolü

- `KAYNAKLAR` bölümü PDF içinde yer alıyor.
- URL içeren kaynaklar satır kırılmasına uygun biçimde görünüyor.
- Kaynakça görsel QA dosyası: `qa_pdf_pages/kaynakca.png`.
- Otomatik kontrolde kaynakta bulunan atıflar ile bibliyografya anahtarları eşleşti.

## 12. Türkçe PDF metin katmanı kontrolü

Aşağıdaki kritik Türkçe metinler PDF metin katmanında doğru Unicode karakterlerle okundu:

- `MATEMATİK`
- `LİSANS`
- `Danışman`
- `ÇELİK`
- `İÇİNDEKİLER`
- `ŞEKİL`
- `TABLO`
- `ÖZGEÇMİŞ`
- `doğrulama`
- `bağıntı`
- `çalışma`

## 13. Overfull/Underfull LaTeX uyarıları

- Final QA sonucu: `PASS: Overfull hbox yok.`
- Final QA sonucu: `PASS: PDF-FINAL QA kontrolleri geçti.`
- Final derlemede `Overfull \hbox`, çözülmemiş referans veya çözülmemiş atıf kalmadı.
- Log içinde bazı `Underfull \hbox` ve `hyperref` PDF string uyarıları bulunuyor; bunlar sayfa taşması veya içerik kaybı üretmeyen tipografik/yer imi düzeyi uyarılardır.

## 14. Turnitin uyarısı

Turnitin benzerlik raporu ayrıca alınmalı ve benzerlik indeksi %30'u aşmamalıdır. Dosyalar içinde Turnitin raporu bulunmadığından oran tahmin edilmemiştir.

## 15. Manuel son kontrol listesi

- PDF dosyası açılıp kapak bilgileri tekrar gözle kontrol edilmeli.
- Danışman adı ve unvanı teslim öncesi okul kayıtlarıyla karşılaştırılmalı.
- Öğrenci numarası `22025083` olarak son kez doğrulanmalı.
- Turnitin raporu ayrıca alınmalı.
- Enstitü/fakülte teslim sistemi farklı bir dosya adı istiyorsa yalnızca dosya adı değiştirilmelidir; PDF içeriği kaynaklardan tekrar üretilmeden düzenlenmemelidir.
