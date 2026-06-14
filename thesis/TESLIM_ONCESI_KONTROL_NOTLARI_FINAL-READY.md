# Teslim Öncesi Kontrol Notları — FINAL-READY

**Tez:** Quantum Grup Yapılarının Python Ortamında Modellenmesi  
**Öğrenci:** Taha Berk TEREKLİ — **Öğrenci No:** 22025083  
**Danışman:** Prof. Dr. Salih ÇELİK — **Tarih:** Haziran, 2026

## 1. Yapılan Son Düzeltmeler

- DOCX için kısa satır içi matematikler metin çıkarımında okunabilir olacak biçimde düz metin fallback’e çevrildi.
- İçindekiler alan güncellemesine bağımlı kalmayacak şekilde görünür, statik metin olarak üretildi.
- Teorem/tanım/cross-reference numaraları DOCX tarafında düz metne sabitlendi.
- PDF için `glyphtounicode` ve `cmap` ayarları eklendi; Türkçe metin katmanı ham ve normalize extraction ile kontrol edildi.
- `qa_final_ready.py` eklendi ve build sonuna bağlandı.

## 2. DOCX İçindekiler Materialization Sonucu

DOCX İçindekiler görünür ve doludur. İçindekiler statik metin olarak yazıldığı için Word/LibreOffice alan güncellemesinin Tanım/Teorem sayaçlarını bozma riski yoktur.

Görünen ana başlıklar: `1 Giriş`, `2 Teorik Arka Plan`, `3 Kuantum Grup Uq(sl2)'nin Tanımı`, `11 Sonuç ve Öneriler`, `KAYNAKLAR`, `EKLER`, `ÖZGEÇMİŞ`.

READY DOCX render sonucu 56 sayfadır; `ÖZGEÇMİŞ` gerçek render başlangıcına göre sayfa 56 olarak yazılmıştır.

## 3. DOCX Matematik Text Fallback Sonucu

Kısa inline semboller metin çıkarımında bulunabilir hale getirildi. Kontrol edilen kritik semboller:

`Uq(sl2)`, `GLq(2|1)`, `Vn`, `V1`, `R13`, `p(e1)=p(e2)=0`, `p(e3)=1`, `Δ`, `ε`, `τ`, `[n]q`.

Uzun blok denklemler görsel matematik olarak korunmuştur.

## 4. DOCX Sayaç/Cross-Reference Sonucu

Doğru sayaçlar bulundu: `Tanım 2.1`, `Tanım 2.2`, `Tanım 2.3`, `Teorem 2.4`, `Tanım 2.5`, `Örnek 2.6`, `Tanım 3.1`, `Teorem 4.1`, `Çizelge 3.1`, `Şekil 4.1`, `Bölüm 10`.

Yanlış sayaçlar bulunmadı: `Tanım 7.1`, `Tanım 8.1`, `Teorem 9.1`, `Bölüm 15`, `Çizelge 8.1`.

## 5. PDF Türkçe Metin Katmanı Sonucu

PDF görsel olarak doğru kalmıştır. Ham `pdftotext` çıktısı bazı Türkçe karakterleri
ayrışmış Unicode dizileriyle vermeye devam eder; bu nedenle doğrudan ham arama tam
geçmez. NFC normalize edilmiş metin üzerinde Türkçe terimler geçmiştir: `TEKNİK`,
`LİSANS`, `Danışman`, `ÇELİK`, `İÇİNDEKİLER`, `ÖZGEÇMİŞ`.

## 6. PDF Sayaç ve İçerik Sonucu

PDF’de öğrenci no `22025083`, İçindekiler, doğru tanım/teorem sayaçları, `Bölüm 10`, `Çizelge 3.1`, `Şekil 4.1`, `Uq(sl2)` ve `GLq(2|1)` içerikleri korunmuştur. `Bölüm 15` yoktur.

## 7. Öğrenci Numarası Durumu

Öğrenci numarası `22025083` hem DOCX hem PDF kapakta yer almaktadır.

## 8. Kaynakça-Atıf Kontrolü

Metindeki `\cite{...}` anahtarları ile kaynakçadaki `\bibitem{...}` anahtarları eşleşmektedir.

## 9. Makale İfadeleri Kontrolü

Tezin kendisine “makale” denmemektedir. “Makale” anlamı yalnız dış kaynak bağlamında korunmuştur.

## 10. Şekil/Çizelge Kontrolü

Şekil ve Çizelge terminolojisi korunmuştur. Numaralandırma bölüm bazlıdır: örnekler `Şekil 4.1`, `Çizelge 3.1`.

## 11. Başlık ve Sayfa Düzeni Kontrolü

Kapak FR-1925 düzenine uygundur: logo, bölüm, tez başlığı, öğrenci, öğrenci no, danışman ve tarih görünürdür. Ana başlıklar ve bölüm başlıkları KL-058 düzenine göre korunmuştur.

## 12. DOCX/PDF Sayfa Sayısı ve Sayfa Numarası Notu

Ana teslim PDF’i LaTeX kaynaklıdır. DOCX farklı dizgi motoruyla açıldığından sayfa sayısı ve sayfa numaraları birebir aynı olmayabilir. Gerekirse `FINAL-READY-DOCX-RENDER.pdf` DOCX dizgisine karşılaştırma amacıyla kullanılabilir.

## 13. Turnitin Uyarısı

Turnitin benzerlik raporu ayrıca alınmalı ve benzerlik indeksi %30’u aşmamalıdır. Dosyalar içinde Turnitin raporu bulunmadığından oran tahmin edilmemiştir.

## 14. Manuel Kontrol Gerektiren Noktalar

- Turnitin raporu ayrıca alınmalıdır.
- Teslim öncesinde kurumun DOCX ve PDF sayfa numarası birebir eşleşmesi isteyip istemediği kontrol edilmelidir.

| Kontrol                                                       | Durum |
| ------------------------------------------------------------- | ----- |
| Kapak logo                                                    | geçti |
| Öğrenci no 22025083                                           | geçti |
| DOCX İçindekiler görünür dolu                                 | geçti |
| DOCX İçindekiler sayfa numaraları yeniden güncellendi         | geçti |
| DOCX sayaçları doğru                                          | geçti |
| DOCX yanlış sayaç yok                                         | geçti |
| DOCX kritik matematik sembolleri text extraction’da bulunuyor | geçti |
| DOCX matematikler görsel olarak dolu                          | geçti |
| PDF sayaçları doğru                                           | geçti |
| PDF Türkçe metin katmanı ham/normalize kontrolü               | normalize geçti |
| Kaynakça-atıf eşleşmesi                                       | geçti |
| Makale ifadeleri                                              | geçti |
| Şekil/Çizelge standardı                                       | geçti |
| Turnitin notu                                                 | geçti |
