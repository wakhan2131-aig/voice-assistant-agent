HEAD
# 🤖 OpenChat Local AI

A lightweight, privacy-focused chatbot interface for interacting with local LLMs via **Ollama**.

## ⚡ Quick Start

### 1. Prerequisites
Install [Ollama](https://ollama.com) and pull a model:
```bash
ollama pull gemma3:1b
```

### 2. Installation
```bash
git clone <repo-url>
cd openchat
pip install -r requirements.txt  # or 'uv sync'
```

### 3. Run it
Choose your preferred interface:

**🌐 Web Interface (Recommended)**
```bash
streamlit run app.py
```

**💻 CLI Interface**
```bash
python main.py
```

---

## 🛠️ Technical Overview

| Component | Technology | Purpose |
| :--- | :--- | :--- |
| **Frontend** | Streamlit | Interactive Web UI with streaming support |
| **CLI** | Python | Minimalist terminal-based interaction |
| **Engine** | Ollama | Local LLM orchestration & API |
| **Logic** | `openchat.llm` | Shared abstraction for chat & model management |

## ✨ Key Features
- **100% Local**: No API keys, no data leaves your machine.
- **Dynamic Model Switching**: Change models on-the-fly via the Web UI.
- **Streaming**: Real-time token generation for a responsive experience.
- **Dual Interface**: Flexible usage via Browser or Terminal.

## 📂 Project Structure
- `app.py`: Streamlit web application.
- `main.py`: CLI entry point.
- `src/openchat/llm.py`: Core logic for Ollama API communication.

# voice-assistant-agent
0a04253c2921210f86acb699f1a6ff3886762476
