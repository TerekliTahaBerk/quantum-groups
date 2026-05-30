# Quantum Groups and Supergroups: U_q(sl_2) ve GL_q(2|1)'nin Python ile Modellenmesi

Bu depo iki yapıyı bir arada sembolik ve hesaplamalı olarak modeller. Bir
yandan kuantum grup **U_q(sl_2)**'yi inceler: sonlu boyutlu indirgenemez
temsillerini açık matrislerle inşa eder, tanımlayıcı bağıntılarını ve Hopf
cebir aksiyomlarını matris düzeyinde doğrular, tensör çarpımı/Clebsch-Gordan
ayrışımı, R-matrisi, Yang-Baxter denklemi, Hecke bağıntısı ve klasik/birim-kök
limitlerini hesaplar. Öte yandan Çelik & Çelik'in *A New Quantum Supergroup
and Its Gauss Decomposition* makalesinde tanıtılan kuantum süpergrup
**GL_q(2|1)** için **bilgisayar destekli graded Yang–Baxter doğrulaması**
sunar: makaledeki 9×9 R-matrisi, süper permütasyon matrisi ve 27×27 kalıntı
matrisi üzerinden graded YBE eşitliği tüm girdiler düzeyinde sembolik olarak
doğrulanır. Proje bir lisans tezi ürünüdür.

Proje hem **matematiksel bir tez bölümü** hem de **modüler bir Python
paketi** olarak tasarlanmıştır.

---

## 1. Matematiksel Arka Plan (Özet)

q sıfırdan farklı, ±1 dışında bir parametre olsun. Kuantum grup
**U_q(sl_2)**, dört üreteç E, F, K, K^{-1} ile aşağıdaki bağıntılara tabi
birleşmeli Q(q)-cebridir:

```
(R1)  K K^{-1} = K^{-1} K = 1
(R2)  K E K^{-1} = q^{ 2} E
(R3)  K F K^{-1} = q^{-2} F
(R4)  [E, F] = (K - K^{-1}) / (q - q^{-1})
```

q → 1 limitinde klasik U(sl_2) elde edilir.

Her n ≥ 0 için (n+1)-boyutlu **indirgenemez en yüksek ağırlık temsili V_n**
vardır; baz {v_0, …, v_n} üzerinde:

```
K . v_k = q^{n-2k} v_k
F . v_k = v_{k+1}              (F . v_n = 0)
E . v_k = [k]_q [n-k+1]_q v_{k-1}   (E . v_0 = 0)
```

burada `[m]_q = (q^m − q^{-m}) / (q − q^{-1})` q-tamsayısıdır. q → 0
limitinde V_n'nin "kombinatoryal gölgesi" olan **kristal taban B(n)**
ortaya çıkar; bu, b_0 → b_1 → … → b_n yönlü yolu olarak modellenir.

Tam teorik bölüm (gruplar → Lie cebirleri → Hopf cebirleri → kuantum
gruplar → temsiller → kristaller → R-matris ve limitler) tezde verilmiştir.

---

## 2. Dosya Yapısı

```
quantum-groups/
├── quantum_group/             # Python paketi
│   ├── __init__.py
│   ├── quantum_group_sl2.py   # QuantumGroupSL2 cephe sınıfı
│   ├── generators.py          # E, F, K, K^{-1}, q sembolleri
│   ├── relations.py           # bağıntı motoru ve doğrulama
│   ├── representations.py     # V_n matrislerini inşa eder
│   ├── hopf.py                # eş-çarpım, eş-birim, antipot ve Hopf aksiyomları
│   ├── tensor.py              # tensör çarpımı ve Clebsch-Gordan hesapları
│   ├── r_matrix.py            # V_1 ⊗ V_1 R-matrisi, QYBE ve Hecke doğrulamaları
│   ├── supergroup_gl21.py     # GL_q(2|1), graded YBE ve V^{⊗n} R_ij yerleşimleri
│   ├── limits.py              # q→1 ve birim kök analizleri
│   ├── crystal.py             # B(n) kristal grafiği
│   ├── visualization.py       # ağırlık & kristal diyagramları
│   └── utils.py               # q-tamsayı, q-faktöriyel, q-binom
├── tests/                     # pytest test paketi
│   ├── test_hopf.py
│   ├── test_limits.py
│   ├── test_r_matrix.py
│   ├── test_relations.py
│   ├── test_representations.py
│   ├── test_supergroup_gl21.py
│   └── test_tensor.py
├── thesis/
│   ├── thesis.tex             # kapsamlı LaTeX tez metni
│   └── thesis.pdf             # Tectonic ile üretilen PDF
├── notebooks/
│   └── exploration.ipynb      # adım adım gösterim
├── main.py                    # uçtan uca demo
├── requirements.txt           # Python bağımlılıkları
└── README.md
```

---

## 3. Kurulum

Python 3.10+ önerilir.

```bash
pip install -r requirements.txt
```

(Opsiyonel: SageMath kullanmak isterseniz `quantum_group` paketi yalnızca
SymPy'ye bağımlıdır; SageMath ortamında da değişiklik yapmadan
çalışacaktır.)

---

## 4. Çalıştırma

### Demo betiği

```bash
python3 main.py
```

Çıktı: q-aritmetik tabloları, dört bağıntı, V_0..V_4 doğrulamaları,
kristal yolları, `outputs/V4_combined.png` diyagramı ve GL_q(2|1) graded YBE
doğrulama özeti.

### Etkileşimli kullanım

```python
from quantum_group import QuantumGroupSL2, plot_combined

Uq = QuantumGroupSL2()
rep = Uq.representation(3)        # V_3 (boyut 4)
checks = Uq.verify(rep)
assert all(c.holds for c in checks.values())

fig = plot_combined(3)
fig.savefig("V3.png")
```

### Notebook

```bash
jupyter notebook notebooks/exploration.ipynb
```

### Testler

```bash
python3 -m pytest tests/ -q
```

Beklenen sonuç: tüm testlerin geçmesi.

---

## 5. Örnek Çıktılar

```
[3]_q  = q^2 + 1 + 1/q^2        (q→1 limit: 3)
[4]_q! = (q^2 + 1)(q^8 − 1)(...)  (q→1 limit: 24)

V_4: boyut=5, tüm bağıntılar = True
    K-ağırlıkları: [q^4, q^2, 1, 1/q^2, 1/q^4]

B(4): b_0 -f-> b_1 -f-> b_2 -f-> b_3 -f-> b_4
```

`main.py` `outputs/V4_combined.png` dosyasında V_4'ün ağırlık diyagramını
ve B(4) kristal grafiğini üretir.

---

## 6. GL_q(2|1) ve Graded Yang–Baxter Doğrulaması

Proje artık yalnızca **U_q(sl_2)** ile sınırlı değildir; Çelik & Çelik
(*A New Quantum Supergroup and Its Gauss Decomposition*, Rep. Math. Phys.
**88** (2021), 259) makalesinde tanıtılan yeni kuantum süpergrubu
**GL_q(2|1)** için de bilgisayar destekli bir doğrulama içerir.

- Makalede verilen **9×9 R-matrisi** kodlanmıştır (`R_matrix_GLq21`).
- **Süper permütasyon matrisi** P, parite `[0, 0, 1]` ile inşa edilmiştir
  (`super_permutation_matrix`). Bu matris klasik takas matrisinden yalnızca
  odd–odd bileşeninde (P[8,8] = −1) ayrılır.
- V ⊗ V ⊗ V üzerinde **R12, R13, R23** matrisleri 27×27 matrisler olarak
  oluşturulur:
  - `R12 = R ⊗ I3`
  - `R23 = I3 ⊗ R`
  - `R13 = (P ⊗ I3) R23 (P ⊗ I3)`
- Kod, kalıntı matrisinin

  ```
  Y(q) = R12 R13 R23 − R23 R13 R12
  ```

  tüm girdilerinin sembolik olarak sıfır olduğunu doğrular. Böylece elle
  yapıldığında çok uzun olan graded Yang–Baxter hesabı yeniden üretilebilir
  hâle gelir.

Örnek kullanım:

```python
from quantum_group import graded_yang_baxter_holds_GLq21
assert graded_yang_baxter_holds_GLq21()
```

**Genel çoklu tensör yerleşimi.** Ana ispat V ⊗ V ⊗ V üzerindeki 27×27
denklemdir. Buna ek olarak kod, aynı R-matrisinin V^{⊗4} üzerine
yerleştirilmesini de destekler: R12, R13, R14, R23, R24, R34 operatörleri
81×81 matrisler olarak üretilebilir (`all_Rij_GLq21(4)`); uzak komütativite
`R12 R34 = R34 R12` (`braid_far_commutativity_residual_GLq21`) ve dört
faktörlü uzaydaki tüm üçlü alt-YBE kontrolleri
(`local_ybe_on_four_tensor_GLq21`) otomatik yapılır. Bu, yöntemin tek bir
denklem doğrulaması değil, daha genel bir graded örgü/Yang–Baxter hesap
altyapısı olduğunu gösterir.

### Metodolojik Katkı

Bu çalışmadaki yeni katkı, GL_q(2|1) için verilen R-matrisinin graded
Yang–Baxter denklemine ilişkin doğrudan hesaplamasını Python/SymPy üzerinde
modellenebilir, test edilebilir ve tekrar üretilebilir bir doğrulama
prosedürüne dönüştürmektir. Böylece klasik elle hesap yöntemi ile bilgisayar
destekli sembolik cebir yöntemi birleştirilmiştir.

Testler hâlâ aşağıdaki komutla çalışır:

```
python3 -m pytest tests/ -q
```

---

## 7. Genişletme Yönleri

- Tip 1 dışındaki temsiller (işaret kıvrımları)
- Birim kökünde kuantum grup (q^N = 1) ve sonlu boyutlu blok yapısı
- Jones polinomu hesaplaması için örgü temsili ve Markov izi
- Yüksek rank: U_q(sl_n), genel Cartan tipi
- Kristal tensör çarpımı B(m) ⊗ B(n)
- GL_q(2|1) için Gauss ayrışımı ve Hopf süpercebir eşlemelerinin kodla doğrulanması

---

## 8. Lisans ve Atıf

Bu proje akademik bir tez ürünüdür. SymPy, NetworkX ve Matplotlib
kütüphaneleri açık lisanslı olup kendi lisanslarına tabidir.
