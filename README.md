# RANTAI ETHIKA ⚖️

Ethics & Bias Checker for Data & Models

ETHIKA is an open-source tool designed to detect bias, ensure fairness, and promote ethical awareness in data exploration and predictive modeling.
It complements the EXPLODA → BUSI → PREDI pipeline by acting as a check & balance system, making sure results are not only accurate but also responsible.

![License: MIT](https://img.shields.io/badge/License-MIT-brightgreen.svg)
![Python](https://img.shields.io/badge/Python-3.9%2B-blue.svg)
![Status](https://img.shields.io/badge/Status-Stable-brightgreen.svg)
![Contributions welcome](https://img.shields.io/badge/Contributions-welcome-blue.svg)

---

## ✨ Features

- Dataset Balance Scanner → visualize distribution across categories with traffic-light indicators.

- Bias in Prediction → compare model performance across groups.

- Fairness Metrics (Optional) → demographic parity, equal opportunity.

- Explainable Flags & Tips → suggests actionable next steps.

- Ethical Reflection Notes → prompt users to document insights.

---

## 🛠 Installation

```bash
git clone https://github.com/mrbrightsides/rantai-ethika.git
cd ethika
pip install -r requirements.txt
```

---

## 🚀 Usage

```bash
python ethika.py --data dataset.csv --model model.pkl
```

Results include:

- Balance chart (distribution)

- Bias flags (⚠️ or ❌ if imbalance detected)

- Reflection template for ethical notes

---

## 📚 Academic Value

- Built for education: teaches not only how to analyze but also why ethics matter.

- Sparks classroom discussions on AI fairness and responsible data science.

---

## 🧩 Position in RANTAI Communities

EXPLODA → BUSI → MODEL PREDI → ETHIKA

| Module      | Link | Status | Badge |
|-------------|------|--------|-------|
| EXPLODA   | [exploda.elpeef.com](https://exploda.elpeef.com/) | ✅ Stable | ![EXPLODA](https://img.shields.io/badge/rantai-exploda-blue) |
| BUSI   | [busi.elpeef.com](https://busi.elpeef.com/) | ✅ Stable | ![BUSI](https://img.shields.io/badge/rantai-busi-orange) |
| MODEL PREDI   | [predi.elpeef.com](https://predi.elpeef.com/) | ✅ Stable | ![MODEL PREDI](https://img.shields.io/badge/model-predi-crimson) |
| ETHIKA     | [ethika.elpeef.com](https://ethika.elpeef.com/) | ✅ Stable | ![ETHIKA](https://img.shields.io/badge/rantai-ethika-purple) |

---

## 🔄 Workflow

```mermaid
flowchart TD
  A["📂 Upload Dataset"] --> B["🔎 ETHIKA Scan Balance"]
  B --> X{"🙏 Apply Spiritual / Value Check?"}
  
  X -- "Yes" --> Y["📜 Ethical + Spiritual Review"]
  X -- "No" --> C{"⚖️ Bias Detected?"}
  Y --> C

  C -- "Yes" --> D["🚩 Flag Issue<br/>+ Tips for Improvement"]
  C -- "No" --> E["✅ All Clear<br/>Balanced Detected"]
  
  D --> H["📝 Reflection Notes<br/>(User Acknowledgement)"]
  E --> H
  
  H --> I["📊 ETHIKA Report Builder"]
  I --> J["💾 Save Report / Export<br/>(PDF, CSV, JSON)"]
  J --> K["📈 Compare with Previous Reports"]
  K --> L["🌐 Share Insights<br/>via RANTAI Communities"]
```

---

## 🌀 Hubungan ELPEEF, STC, RANTAI, dan ETHIKA

🌍 **ELPEEF** adalah sumber — titik awal gagasan, ruang lahirnya mimpi, tempat semua kolaboraksi dimulai. Dari sini, dua aliran besar tercipta:  
- ⚙️ **STC Ecosystem** → kumpulan tools, analytics, dan sistem yang memberi otot dan logika pada ekosistem.  
- 👥 **RANTAI Communities** → wadah manusia, refleksi, diskusi, dan gerakan sosial yang memberi jiwa dan napas.  

Keduanya tidak berdiri sendiri. Mereka saling tarik-menarik, saling isi, saling kritis. Tapi tetap saja, tanpa suatu penyeimbang, semua ini bisa kehilangan arah:  

☂️ **ETHIKA** hadir sebagai pusat gravitasi. Payung yang bukan sekadar pelindung, tapi pengingat. Bahwa setiap eksperimen, setiap tool, setiap komunitas, harus kembali ke nilai. Etika menjadi orbit yang menjaga agar STC dan RANTAI tidak melayang liar tanpa tujuan.  

✨ ELPEEF melahirkan.  
⚙️ STC membangun.  
👥 RANTAI menghidupkan.  
☂️ ETHIKA memayungi.

```mermaid
flowchart TD
    A["ELPEEF 🌍 (the root, the source)"]:::root
    A --> B["STC Ecosystem ⚙️ (tools, analytics)"]
    A --> C["RANTAI Communities 👥 (people, reflection)"]
    B --> D["ETHIKA ☂️ (the ethics umbrella)"]
    C --> D

    classDef root fill:#1a1a1a,stroke:#fff,color:#fff,font-weight:bold
    classDef default fill:#f8f8f8,stroke:#333,color:#000
```

```mermaid
flowchart LR
    A["STC Ecosystem"]:::left
    B["ETHIKA"]:::center
    C["RANTAI Communities"]:::right

    A --> B --> C
    B --> A
    C --> B

    classDef left fill:#f8f8f8,stroke:#333,color:#000
    classDef right fill:#f8f8f8,stroke:#333,color:#000
    classDef center fill:#1a1a1a,stroke:#fff,color:#fff,font-weight:bold
```

---

# 📜 License

MIT License – free to use, modify, and share.

