# Quantum Groups: U_q(sl_2)'nin Python ile Modellenmesi

Bu depo, kuantum grup **U_q(sl_2)**'yi sembolik olarak modelleyen, sonlu
boyutlu indirgenemez temsillerini açık matrislerle inşa eden, tanımlayıcı
bağıntılarını ve Hopf cebir aksiyomlarını matris düzeyinde doğrulayan,
tensör çarpımı/Clebsch-Gordan ayrışımı, R-matrisi, Yang-Baxter denklemi,
Hecke bağıntısı ve klasik/birim-kök limitlerini hesaplamalı olarak inceleyen
bir lisans tezi projesidir.

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
│   └── test_tensor.py
├── thesis/
│   ├── thesis.tex             # kapsamlı LaTeX tez metni
│   └── thesis.pdf             # Tectonic ile üretilen PDF
├── notebooks/
│   └── exploration.ipynb      # adım adım gösterim
├── main.py                    # uçtan uca demo
└── README.md
```

---

## 3. Kurulum

Python 3.10+ önerilir.

```bash
pip install sympy networkx matplotlib pytest
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
kristal yolları ve `outputs/V4_combined.png` diyagramı.

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

Beklenen sonuç: **97 passed**.

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

## 6. Genişletme Yönleri

- Tip 1 dışındaki temsiller (işaret kıvrımları)
- Birim kökünde kuantum grup (q^N = 1) ve sonlu boyutlu blok yapısı
- Jones polinomu hesaplaması için örgü temsili ve Markov izi
- Yüksek rank: U_q(sl_n), genel Cartan tipi
- Kristal tensör çarpımı B(m) ⊗ B(n)

---

## 7. Lisans ve Atıf

Bu proje akademik bir tez ürünüdür. SymPy, NetworkX ve Matplotlib
kütüphaneleri açık lisanslı olup kendi lisanslarına tabidir.
