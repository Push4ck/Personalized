# 🚀 Personalized

**AI-Enhanced Python CLI Tools to Supercharge Your Daily Productivity**

---

## 📌 Overview

**Personalized** is a curated collection of modular, command-line Python utilities designed to make your daily workflows smarter, faster, and more efficient. Each project in this repo is engineered for production readiness with clean code, proper structure, AI integration where useful, and intuitive CLI interfaces.

> Whether it's converting text to speech, merging PDFs, or setting reminders — this suite has you covered.

---

## 🧰 Tools Included

| Tool                         | Description                                                                            |
| ---------------------------- | -------------------------------------------------------------------------------------- |
| 📢 Text to Speech (`tts`)    | Convert any string of text into speech with support for multiple languages via `gTTS`. |
| 📚 Book Reader (`audiobook`) | Extract and read aloud content from PDFs using `pyttsx3` and `PyPDF2`.                 |
| 📌 PDF Merger (`pdf-merger`) | Merge multiple PDF files into one with a clean CLI-based workflow.                     |
| ⏰ Reminder (`reminder`)     | Set voice-enabled reminders with snooze and repeat intervals. Fully terminal-based.    |

> **AI-ready & CLI-first:** All tools are wrapped with `Typer` and support interactive usage or flags for automation.

---

## 📦 Project Structure

```
Personalized/
└── tools/
    ├── TTS/
    ├── AudioBook/
    ├── PdfMerger/
    └── Reminder/
```

Each folder contains:

- `cli.py` – Typer-based CLI entrypoint
- `core.py` – Business logic
- `README.md` – Usage documentation
- `tests/` – Unit tests
- `pyproject.toml` – Dependency and packaging config (Poetry)

---

## 🚀 Getting Started

### 1. Clone the Repo

```bash
git clone https://github.com/Push4ck/Personalized.git
cd Personalized/tools/<tool-name>
```

### 2. Install Dependencies

> We use **Poetry** for dependency management. It’s modern and keeps your builds reproducible.

```bash
poetry install
```

### 3. Run the Tool

```bash
poetry run python cli.py --help
```

For example, using the TTS tool:

```bash
poetry run python cli.py speak -t "Hello World" -p
```

---

## 💡 Why Personalized?

- ✅ Fully modular
- ✅ CLI-first UX
- ✅ Production-level folder structure
- ✅ Tests included
- ✅ AI integration ready
- ✅ Easy to contribute

---

## 🤝 Contributing

Contributions are welcome. Feel free to fork, open PRs, suggest features, or file issues. We follow standard contribution practices. Make sure to check the contributing guidelines in each tool’s folder if available.

---

## 🧐 What’s Coming Next?

- GitHub Pages-powered documentation
- Dockerized versions for quick execution
- GitHub Actions CI for testing
- AI-enhanced capabilities like voice detection, summarization, etc.

---

## 📬 Stay Connected

Star ⭐ the repo to show support and stay updated on future improvements.

> Built by [Push4ck](https://github.com/Push4ck) — designed to turn everyday Python scripts into professional-grade tools.
