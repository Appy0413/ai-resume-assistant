# 🤖 AI Resume Assistant (Offline LLM Project)
🚀 Built using a local LLM (Ollama) to demonstrate real-world AI integration without external APIs.
> ⚠️ Note: This project runs locally using Ollama. A live demo is not hosted.

## 📸 Demo
![App Screenshot](screenshot.png)

An AI-powered resume chatbot that analyzes resumes, answers questions, and provides improvement suggestions using a locally hosted LLM (Ollama).

---

## 🚀 Features

- 📄 Upload resume (PDF)
- 💬 Ask questions about your resume
- 📊 Get AI-based improvement suggestions
- 🤖 Uses local LLM (no API required)
- 🔒 Works completely offline

---

## 🛠️ Tech Stack

- Python
- Streamlit
- Ollama (Local LLM)
- pypdf

---

## 🧠 How it Works

1. Upload resume (PDF)
2. Extract text using pypdf
3. Send context to local LLM via Ollama
4. AI generates answers and suggestions

---

## ⚡ Setup Instructions

### 1. Install dependencies
```bash
pip install -r requirements.txt
2. Run local AI model (Ollama)
ollama run phi
3. Run the application
streamlit run app.py
📊 Features in Detail
🔹 Resume Q&A

Ask questions like:

What are my skills?

Summarize my experience

🔹 Resume Improvement

Suggestions for improvement

Missing skills detection

Job role recommendations

💡 Future Improvements

Job match scoring

Resume scoring system

Better LLM models (Mistral)

UI enhancements
## ❓ Example Questions

- What are my skills?
- Summarize my experience
- What roles suit me?
- How can I improve my resume?

📌 Author

Aprajita Singh
Aspiring Ai Engineer
