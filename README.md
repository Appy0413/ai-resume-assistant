# 🤖 AI Resume Assistant (Offline LLM Project)

🚀 Built using a local LLM (Ollama) to demonstrate real-world AI integration without external APIs.

> ⚠️ Note: This project runs locally using Ollama. A live demo is not hosted.

---

## 📸 Demo

![Front Screen](https://github.com/Appy0413/ai-resume-assistant/raw/main/front.png)
![Resume Analysis](https://github.com/Appy0413/ai-resume-assistant/raw/main/resume%20analysis.png)
![Ask Questions](https://github.com/Appy0413/ai-resume-assistant/raw/main/ask%20questions.png)

---

## 🚀 Features

- 📄 Upload resume (PDF)
- 💬 Ask questions about your resume
- 📊 Get AI-based improvement suggestions
- 🤖 Uses local LLM (no API key required)
- 🔒 Works completely offline — privacy friendly

---

## 🛠️ Tech Stack

| Tool | Purpose |
|---|---|
| Python | Core language |
| Streamlit | Web UI |
| Ollama (phi model) | Local LLM inference |
| pypdf | PDF text extraction |

---

## 🧠 How it Works

1. Upload your resume (PDF format)
2. Text extracted using `pypdf`
3. Text sent as context to local LLM via Ollama
4. AI generates answers, suggestions and analysis

---

## ⚙️ Setup Instructions

### 1. Clone the repository
```bash
git clone https://github.com/Appy0413/ai-resume-assistant.git
cd ai-resume-assistant
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Start local AI model
```bash
ollama run phi
```

### 4. Run the application
```bash
streamlit run app.py
```

---

## ❓ Example Questions to Ask

- "What are my key skills?"
- "Summarize my work experience"
- "What roles suit my profile?"
- "How can I improve my resume?"
- "What skills am I missing for a Data Scientist role?"

---

## 💡 Key Learning

This project demonstrates running AI completely offline using a local LLM — no API keys, no cost, full privacy. Shows practical integration of PDF parsing, prompt engineering, and Streamlit UI.

---

## 📌 Author

**Aprajita Singh** — Aspiring AI/ML Engineer  
[GitHub](https://github.com/Appy0413)
