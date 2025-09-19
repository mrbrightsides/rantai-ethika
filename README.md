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
| EXPLODA   | [rantai-exploda.streamlit.app](https://rantai-exploda.streamlit.app/) | ✅ Stable | ![EXPLODA](https://img.shields.io/badge/rantai-exploda-blue) |
| BUSI   | [rantai-busi.streamlit.app](https://rantai-busi.streamlit.app/) | ✅ Stable | ![BUSI](https://img.shields.io/badge/rantai-busi-orange) |
| MODEL PREDI   | [rantai-model-predi.streamlit.app](https://rantai-model-predi.streamlit.app/) | ✅ Stable | ![MODEL PREDI](https://img.shields.io/badge/model-predi-crimson) |
| ETHIKA     | [rantai-ethika.streamlit.app](https://rantai-ethika.streamlit.app/) | ✅ Stable | ![ETHIKA](https://img.shields.io/badge/rantai-ethika-purple) |

---

## 🔄 Workflow

```mermaid
flowchart LR
  A["Upload Dataset"] --> B["ETHIKA Scan Balance"]
  B --> C{"Bias Detected?"}
  C -- Yes --> D["Flag & Tips"]
  C -- No --> E["All Clear ✅"]
  D --> F["Reflection Notes"]
  E --> F
  F --> G["Save Report / Export"]
```

---

# 📜 License

MIT License – free to use, modify, and share.

