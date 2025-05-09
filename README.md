# Kid-s-Language-Explorer

# English-Indic Language Translation Web Interface

This repository contains the code, datasets (where permissible), and evaluation scripts for the research project **“Evaluation and Deployment of Pretrained Multilingual Models for English to Hindi/Gujarati Translation”**.

## 🔍 Project Overview

This project compares three state-of-the-art multilingual translation models:

- **IndicTrans2** (ai4bharat/indictrans2-en-indic-1B)
- **mBART-50** (facebook/mbart-large-50)
- **NLLB-200** (facebook/nllb-200-distilled-600M)

The evaluation spans three benchmark datasets:

- **IN22-Gen** (IndicTrans2 Evaluation Benchmark)
- **FLORES+**
- **WMT14/WMT19**

We assess performance using **BLEU**, **chrF**, and **COMET** scores and deploy the best-performing model (IndicTrans2) in a web interface for real-time English-to-Hindi/Gujarati translation.

---

## 💻 Web Interface

The repository includes a lightweight Flask-based web application that allows users to input English text, select a target language (Hindi or Gujarati), and obtain translated output.

### To Run the Web Interface Locally:

1. Clone the repository:

```bash
git clone https://github.com/kapsedivya31/Kid-s-Language-Explorer.git
cd Kid-s-Language-Explorer
```

2. Install required packages:

```bash
pip install -r requirements.txt
```

3. Run the app:

```bash
python app.py
```

## 📁 Repository Structure

├── app.py                      # Flask web server
├── translator.py               # Model initialization and translation logic
├── templates/
│   └── index.html              # HTML template for web UI
├── static/
│   └── styles.css              # CSS styling
├── indictransbleuchrfcomet.ipynb # Script for BLEU, chrF, COMET evaluation
├── README.md                    # This file
└── requirements.txt             # Python dependencies

## 📚 Dataset Sources

•	**IN22-Gen:** https://huggingface.co/datasets/ai4bharat/IN22-Gen
•	**FLORES+**: https://huggingface.co/datasets/openlanguagedata/flores_plus
•	**WMT14/WMT19**: https://huggingface.co/datasets/wmt/wmt14 and https://huggingface.co/datasets/wmt/wmt19

## 📝 Citation

Coming soon

## 📬 Contact

For questions or collaborations, please contact: gdpk3112@gmail.com
