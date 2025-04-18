# 🧠 CompanyBrain

**CompanyBrain** ist ein lokal laufendes KI-System zur PDF-Analyse mit Vektorsuche und natürlicher Sprachverarbeitung – komplett ohne OpenAI oder API-Key.
Es liest Dokumente ein, extrahiert Inhalte und beantwortet semantische Fragen direkt aus den Textinhalten. Ideal für Firmen, die mit vertraulichen Daten arbeiten.

---

## 🚀 Features

- 📄 PDF-Upload mit automatischer Texterkennung
- ✂️ Text wird in semantisch sinnvolle Chunks zerlegt
- 🔍 Vektorsuche mit FAISS (lokal, performant)
- 🧠 Embeddings mit `sentence-transformers` (kein API nötig)
- 💬 Fragen stellen & automatisch Antwort erhalten
- 🔐 Komplett offline, DSGVO-freundlich & kostenlos
- 💻 Streamlit Web-GUI (optional)

---

## 🛠️ Tech-Stack

| Technologie           | Verwendung                             |
| --------------------- | -------------------------------------- |
| Python                | Core-Logik                             |
| PyMuPDF (`fitz`)      | PDF-Text-Extraktion                    |
| FAISS                 | Vektorspeicherung & Ähnlichkeitssuche  |
| sentence-transformers | Lokale Embeddings (`all-MiniLM-L6-v2`) |
| Streamlit             | Web-Interface                          |

---

## 📦 Installation

```bash
# Projekt klonen
cd C:/dev
mkdir CompanyBrain && cd CompanyBrain

# Virtuelle Umgebung erstellen
python -m venv venv
venv\Scripts\activate

# Requirements installieren
pip install -r requirements.txt
```

---

## 📄 Test-PDF erzeugen (optional)

```bash
python create_test_pdf.py
```

---

## ▶️ Ausführen (CLI-Version)

```bash
python main.py
```

---

## 💻 Streamlit Webinterface starten

```bash
streamlit run app.py
```

Dann öffnen: http://localhost:8501

---

## 📁 Projektstruktur

```bash
CompanyBrain/
├── data/
│   ├── uploads/        # Hochgeladene PDFs
│   └── index/          # FAISS Index & Metadaten
├── pdf_parser.py       # PDF in Text-Chunks zerlegen
├── embed_index.py      # Vektorisierung & Index-Aufbau
├── query_engine.py     # Frage → Ähnliche Chunks → Antwort
├── llm_local.py        # Dummy-KI-Antwort (lokal)
├── create_test_pdf.py  # Beispiel-PDF generieren
├── main.py             # CLI-Ablauf
├── app.py              # Streamlit-Frontend
├── requirements.txt    # Abhängigkeiten
└── README.md           # Diese Datei
```

---

## 💡 Beispiel-Antwort

> **Frage:** Was wurde zu Projekt X gesagt?
>
> 🧠 _"Das Dokument enthält Hinweise auf Projekt X und dessen Budgetplanung."_

---

## ✅ Vorteile für Firmen

- Keine API-Abhängigkeit oder Kosten
- DSGVO-konform, da alles lokal läuft
- Schnell erweiterbar mit echtem LLM oder UI
- Technisch sauber, sofort präsentierbar für Bewerbungen, Demos oder als internes Tool

---

## ✨ Mögliche Erweiterungen

- 🖼️ Upload-Drag-Drop & Mehr-Dokumenten-Unterstützung
- 🤖 Lokales Sprachmodell (Llama.cpp, GGUF)
- 🧠 Kontext-Follow-Up (Chatverlauf)
- 📊 Visuelle Analyse-Widgets

---

## 📂 .gitignore-Vorschlag

```bash
__pycache__/
*.pyc
venv/
data/index/*.pkl
*.faiss
*.pdf
.env
```

---

## 📋 GitHub-Empfehlung

```bash
git init
git add .
git commit -m "Initial commit: Lokaler PDF-KI-Assistent mit Web-GUI"
git remote add origin https://github.com/cann65/companybrain.git
git push -u origin main
```

---

**Autor:** Can Yildiz
**Projektstatus:** ✅ _Läuft lokal & ist erweiterbar_  
**Lizenz:** MIT oder Apache-2.0 (frei wählbar)

---

> Ready to impress. Made with ❤️ + KI + FAISS + Streamlit.
