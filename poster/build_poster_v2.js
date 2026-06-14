// YTÜ Bitirme Tezi Posteri — Quantum Grup Yapıları (lacivert+altın, kart tabanlı)
// 70x90 cm dikey. pptxgenjs ile sıfırdan tasarım.
const path = require("path");
const PptxGenJS = require("pptxgenjs");

const DIR = __dirname;
const FIG = (n) => path.join(DIR, "figures", n);
const LOGO = path.join(DIR, "assets", "ytu_logo.png");

// ---- Palet ----
const NAVY = "1B2A5B", GOLD = "BE9B57", ICE = "EEF2F9", CARDBG = "F5F8FD";
const CARDLN = "D6DEEE", TEXT = "222222", ICETEXT = "D7E0F2", GOLDBOX = "F7EFDC";
const FONT = "Calibri";

// ---- Sayfa (70x90 cm = 27.559 x 35.433 inç) ----
const PW = 27.559, PH = 35.433;
const M = 0.6;                       // yan kenar boşluğu
const colGap = 0.45;
const colW = (PW - 2 * M - colGap) / 2;   // sütun genişliği
const LX = M, RX = M + colW + colGap;     // sol/sağ sütun x

const pptx = new PptxGenJS();
pptx.defineLayout({ name: "POSTER", width: PW, height: PH });
pptx.layout = "POSTER";
const s = pptx.addSlide();
s.background = { color: "FFFFFF" };

const RR = (o) => s.addShape(pptx.ShapeType.roundRect, o);
const RECT = (o) => s.addShape(pptx.ShapeType.rect, o);
const T = (t, o) => s.addText(t, Object.assign({ fontFace: FONT, color: TEXT }, o));
const IMG = (n, x, y, w, h) => s.addImage({ path: FIG(n), x, y, w, h });

// Kart: arka plan + lacivert başlık çubuğu; iç içerik bölgesini döndürür
const HEAD = 1.0;
function card(x, y, w, h, title, titleSize = 30) {
  RR({ x, y, w, h, fill: { color: CARDBG }, line: { color: CARDLN, width: 1 }, rectRadius: 0.12 });
  RR({ x, y, w, h: HEAD, fill: { color: NAVY }, line: { type: "none" }, rectRadius: 0.12 });
  RECT({ x, y: y + HEAD - 0.14, w, h: 0.14, fill: { color: NAVY }, line: { type: "none" } }); // başlık çubuğu altını düzleştir
  T(title, { x: x + 0.32, y, w: w - 0.64, h: HEAD, fontSize: titleSize, bold: true, color: "FFFFFF", valign: "middle", align: "left" });
  return { ix: x + 0.36, iy: y + HEAD + 0.2, iw: w - 0.72 };
}
const cimg = (ic, w) => ic.ix + (ic.iw - w) / 2;  // kart içinde yatay ortala

// =================== ÜST BANT ===================
RECT({ x: 0, y: 0, w: PW, h: 4.3, fill: { color: NAVY }, line: { type: "none" } });
RECT({ x: 0, y: 4.18, w: PW, h: 0.12, fill: { color: GOLD }, line: { type: "none" } });
// logo beyaz chip üzerinde
RR({ x: 0.7, y: 0.5, w: 8.7, h: 1.5, fill: { color: "FFFFFF" }, line: { type: "none" }, rectRadius: 0.1 });
s.addImage({ path: LOGO, x: 0.98, y: 0.66, w: 8.1, h: 8.1 / 7.0078 });
T("Quantum Grup Yapılarının Python Ortamında Modellenmesi",
  { x: 0.7, y: 2.02, w: PW - 1.4, h: 1.05, fontSize: 40, bold: true, color: "FFFFFF", align: "center", valign: "middle" });
T("2025–2026 Bahar Yarıyılı   ·   Matematik Bölümü",
  { x: 0.7, y: 3.12, w: PW - 1.4, h: 0.48, fontSize: 24, bold: true, color: GOLD, align: "center" });
T([{ text: "Taha Berk TEREKLİ  ", options: { bold: true } },
   { text: "……………", options: {} },
   { text: "      ·      Danışman: ", options: {} },
   { text: "Prof. Dr. Salih ÇELİK", options: { bold: true } }],
  { x: 0.7, y: 3.58, w: PW - 1.4, h: 0.48, fontSize: 22, color: ICETEXT, align: "center" });

// =================== ÖZET (tam genişlik) ===================
let c = card(M, 4.6, PW - 2 * M, 2.85, "ÖZET");
T("Bu çalışma, Drinfeld–Jimbo kuantum grubu Uq(sl₂) ve GLq(2|1) kuantum süpergrubu için temel temsil-teorik ve Yang–Baxter tipi bağıntıları Python/SymPy ortamında yeniden üretilebilir biçimde modeller. Yöntemin çekirdeği, her cebirsel eşitliği açık sonlu boyutlu temsiller üzerinde bir kalıntı matrisine indirgemek ve matrisin tüm girdilerini sembolik olarak sadeleştirip sıfır olup olmadığını denetlemektir. Raporlanan her eşitlik pytest tabanlı bir teste bağlıdır.",
  { x: c.ix, y: c.iy, w: c.iw, h: 1.5, fontSize: 20, align: "justify", valign: "top", lineSpacingMultiple: 1.02 });

// =================== SÜTUNLAR ===================
const colTop = 7.65;
// ---- SOL: GİRİŞ ----
c = card(LX, colTop, colW, 4.7, "GİRİŞ ve MOTİVASYON");
T("Kuantum gruplar, evrensel sarmalayıcı cebir U(g)’nin tek-parametreli (q) deformasyonu olan; ne değişmeli ne de eş-değişmeli Hopf cebirleridir. Kalbinde, integrallenebilir sistemler ile düğüm değişmezlerini aynı çatıda buluşturan Yang–Baxter denklemi ve onun çözümü R-matrisi yatar. Amaç yeni bir kuantum grup tanımlamak değil; bilinen Uq(sl₂) ve GLq(2|1) yapılarını sonlu boyutlu temsiller üzerinde modüler, test edilebilir ve yeniden üretilebilir bir sembolik doğrulama altyapısına dönüştürmektir.",
  { x: c.ix, y: c.iy, w: c.iw, h: 3.3, fontSize: 20, align: "justify", valign: "top", lineSpacingMultiple: 1.02 });

// ---- SOL: KURAMSAL TEMEL ----
c = card(LX, colTop + 4.7 + 0.35, colW, 11.3, "KURAMSAL TEMEL");
let yy = c.iy;
T("Uq(sl₂); E, F, K, K⁻¹ üreteçleri ve dört tanımlayıcı bağıntı ile verilen bir Hopf cebridir:",
  { x: c.ix, y: yy, w: c.iw, h: 1.1, fontSize: 20, align: "justify", valign: "top" });
yy += 1.15;
RR({ x: c.ix, y: yy, w: c.iw, h: 1.5, fill: { color: GOLDBOX }, line: { color: GOLD, width: 1 }, rectRadius: 0.08 });
T([{ text: "K E K⁻¹ = q² E        K F K⁻¹ = q⁻² F\n", options: {} },
   { text: "[E , F] = (K − K⁻¹) / (q − q⁻¹)", options: {} }],
  { x: c.ix + 0.15, y: yy, w: c.iw - 0.3, h: 1.5, fontSize: 22, bold: true, color: NAVY, align: "center", valign: "middle", lineSpacingMultiple: 1.1 });
yy += 1.7;
T("(n+1)-boyutlu indirgenemez temsil Vn açık matrislerle kurulur; E katsayıları q-tamsayı çarpımları [k]q·[n−k+1]q ile q-deforme olur ve q→1 limitinde klasik sl₂ temsili geri gelir.",
  { x: c.ix, y: yy, w: c.iw, h: 1.7, fontSize: 20, align: "justify", valign: "top" });
yy += 1.85;
{ const w = 10.6, h = w / 2.1455; IMG("tikz_weight-1.png", cimg(c, w), yy, w, h);
  T("Şekil 1. V₄ temsilinin ağırlık diyagramı: F yükseltir, E q-katsayılarla taşır.",
    { x: c.ix, y: yy + h + 0.04, w: c.iw, h: 0.5, fontSize: 18, italic: true, color: NAVY, align: "center" }); }

// ---- SAĞ: YÖNTEM ----
c = card(RX, colTop, colW, 4.7, "YÖNTEM");
T("Her cebirsel eşitlik, açık temsiller üzerinde bir kalıntı matrisine indirgenir; matrisin tüm girdileri SymPy ile sembolik olarak sadeleştirilip sıfıra inip inmediği denetlenir. Aynı “kur ve girdi-bazlı sıfırla” deseni, Uq bağıntılarından GLq(2|1) graded Yang–Baxter hesabına dek değişmeden uygulanır. Yalnızca SymPy’ye bağlı modüler quantum_group paketi geliştirilmiş; her doğrulama bir pytest testine bağlanmıştır.",
  { x: c.ix, y: c.iy, w: c.iw, h: 3.3, fontSize: 20, align: "justify", valign: "top", lineSpacingMultiple: 1.02 });

// ---- SAĞ: BULGULAR ----
c = card(RX, colTop + 4.7 + 0.35, colW, 11.3, "BULGULAR");
const bullets = [
  "Uq(sl₂) için dört tanımlayıcı bağıntı ve dokuz Hopf aksiyomu seçilen temsillerde sembolik olarak doğrulandı.",
  "Tensör çarpımı Vm⊗Vn üzerinde eş-çarpımdan gelen eylem kuruldu; Clebsch–Gordan en yüksek ağırlık vektörleri q-deforme katsayılarla elde edildi.",
  "V₁⊗V₁ üzerinde R-matrisi, kuantum Yang–Baxter denklemi, örgü bağıntısı ve Hecke skein özdeşliği doğrulandı.",
].map((t, i) => ({ text: t, options: { bullet: { code: "2022", indent: 18 }, breakLine: true, paraSpaceAfter: 8 } }));
T(bullets, { x: c.ix, y: c.iy, w: c.iw, h: 4.0, fontSize: 20, align: "left", valign: "top", lineSpacingMultiple: 1.02 });
{ const w = 11.0, h = w / 1.7795, yi = c.iy + 4.15;
  IMG("R_sl2_V1-1.png", cimg(c, w), yi, w, h);
  T("Şekil 2. V₁⊗V₁ üzerinde Drinfeld R-matrisi ve örgülü Ř = τR.",
    { x: c.ix, y: yi + h + 0.04, w: c.iw, h: 0.5, fontSize: 18, italic: true, color: NAVY, align: "center" }); }

// =================== GLq(2|1) ÖZELLİK KARTI (tam genişlik) ===================
c = card(M, 24.15, PW - 2 * M, 6.25, "GLq(2|1) GRADED YANG–BAXTER");
const gx = c.ix;
T("Salih Çelik ve Sultan A. Çelik’in tanıttığı GLq(2|1) süpergrubunun 9×9 R-matrisi bağımsız kodlandı. p(e₁)=p(e₂)=0, p(e₃)=1 parite konvansiyonu ve süper permütasyonla R₁₃ yerleşimi kuruldu; graded Yang–Baxter kalıntısının tüm 27×27 girdisinin sıfır olduğu — yani R₁₂R₁₃R₂₃ = R₂₃R₁₃R₁₂ — sembolik olarak doğrulandı.",
  { x: gx, y: c.iy, w: 7.5, h: 4.6, fontSize: 20, align: "justify", valign: "top", lineSpacingMultiple: 1.05 });
{ const h = 4.35, w1 = h * 2.6141, w2 = h * 1.1373;
  const x1 = gx + 7.9, x2 = x1 + w1 + 0.35;
  IMG("ybe_products_27-1.png", x1, c.iy, w1, h);
  T("Şekil 3. Graded Yang–Baxter’in iki tarafı (27×27) özdeş; kalıntı tümüyle sıfırdır.",
    { x: x1, y: c.iy + h + 0.04, w: w1, h: 0.5, fontSize: 18, italic: true, color: NAVY, align: "center" });
  IMG("R_gl21_structure-1.png", x2, c.iy, w2, h);
  T("Şekil 4. GLq(2|1) için 9×9 R-matrisinin girdi-tipi haritası.",
    { x: x2, y: c.iy + h + 0.04, w: w2, h: 0.5, fontSize: 18, italic: true, color: NAVY, align: "center" }); }

// =================== SONUÇ + KAYNAKÇA (iki sütun) ===================
const botTop = 30.6, botH = 3.35;
c = card(LX, botTop, colW, botH, "SONUÇ");
T("Yüksek boyutlu Yang–Baxter tipi hesaplar, elle yürütülen cebirsel manipülasyonlardan test edilebilir ve yeniden üretilebilir sembolik doğrulama prosedürlerine taşınabilir. Parite bilgisi matris düzeyine gömülerek en hata-açık adım — işaret ve faktör sıralaması — otomatikleştirilmiştir.",
  { x: c.ix, y: c.iy, w: c.iw, h: botH - 1.3, fontSize: 20, align: "justify", valign: "top", lineSpacingMultiple: 1.02 });

c = card(RX, botTop, colW, botH, "KAYNAKÇA");
const refs = [
  [{ text: "[1] ", options: { bold: true } }, { text: "Çelik, S., Çelik, S. A., (2021). “A New Quantum Supergroup and its Gauss Decomposition”, Reports on Mathematical Physics, 88(2), 259–272.", options: {} }],
  [{ text: "[2] ", options: { bold: true } }, { text: "Kassel, C., (1995). Quantum Groups, Springer, New York.", options: {} }],
  [{ text: "[3] ", options: { bold: true } }, { text: "Chari, V., Pressley, A., (1994). A Guide to Quantum Groups, Cambridge University Press, Cambridge.", options: {} }],
].map((arr) => arr.map((r, i) => Object.assign(r, { options: Object.assign({}, r.options, i === arr.length - 1 ? { breakLine: true, paraSpaceAfter: 6 } : {}) }))).flat();
T(refs, { x: c.ix, y: c.iy, w: c.iw, h: botH - 1.3, fontSize: 18, align: "justify", valign: "top", lineSpacingMultiple: 1.0 });

// =================== FOOTER ===================
RECT({ x: 0, y: 34.1, w: PW, h: 0.95, fill: { color: NAVY }, line: { type: "none" } });
RECT({ x: 0, y: 34.1, w: PW, h: 0.08, fill: { color: GOLD }, line: { type: "none" } });
T([{ text: "Açık kaynak ve yeniden üretilebilir:  ", options: {} },
   { text: "github.com/TerekliTahaBerk/quantum-groups", options: { bold: true, color: GOLD } },
   { text: "        ·        YTÜ Fen-Edebiyat Fakültesi, Matematik Bölümü", options: {} }],
  { x: 0.6, y: 34.1, w: PW - 1.2, h: 0.95, fontSize: 18, color: "FFFFFF", align: "center", valign: "middle" });

pptx.writeFile({ fileName: path.join(DIR, "Quantum Grup Yapıları - Poster.pptx") })
  .then((f) => console.log("yazıldı:", f));
