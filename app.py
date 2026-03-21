import streamlit as st
import ollama
from pypdf import PdfReader

st.title("🤖 AI Resume Assistant")

# Chat history
if "history" not in st.session_state:
    st.session_state.history = []

uploaded_file = st.file_uploader("Upload your resume (PDF)", type="pdf")

if uploaded_file:
    reader = PdfReader(uploaded_file)
    resume_text = ""

    for page in reader.pages:
        text = page.extract_text()
        if text:
            resume_text += text

    st.success("Resume uploaded successfully!")

    # ------------------ ASK QUESTION ------------------
    question = st.text_input("Ask something about your resume:")

    if st.button("Ask"):
        if question.strip() == "":
            st.warning("Please enter a question")
        else:
            prompt = f"""
You are a professional resume assistant.

ONLY use the information from the resume below.
If the answer is not in the resume, say "Not mentioned in resume".

Resume:
{resume_text}

Question:
{question}
"""

            response = ollama.chat(
                model="phi",
                messages=[
                    {"role": "user", "content": prompt}
                ]
            )

            answer = response["message"]["content"]

            st.session_state.history.append(("You", question))
            st.session_state.history.append(("AI", answer))

    # ------------------ IMPROVE RESUME ------------------
    if st.button("Improve My Resume"):
        improve_prompt = f"""
You are an expert resume reviewer.

Analyze the resume below and respond in this format:

1. Summary (2-3 lines)
2. Key strengths (bullet points)
3. Missing skills or sections
4. Specific improvements (bullet points)
5. Suggested job roles (3 roles)

IMPORTANT:
- Be specific
- Avoid generic advice
- If something is missing, clearly say "Missing"

Resume:
{resume_text}
"""

        response = ollama.chat(
            model="phi",
            messages=[
                {"role": "user", "content": improve_prompt}
            ]
        )

        improve_answer = response["message"]["content"]

        st.write("## 📊 Resume Analysis")
        st.write(improve_answer)

    # ------------------ CHAT HISTORY ------------------
    if st.session_state.history:
        st.write("## 💬 Chat History")
        for role, msg in st.session_state.history:
            st.write(f"**{role}:** {msg}")