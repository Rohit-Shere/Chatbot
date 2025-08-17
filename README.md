# 🤖 AI Chatbot — LangGraph + Google Gemini + Streamlit

A compact, production-ready multi-turn chatbot using **LangGraph** for orchestration, **Google Gemini** (via `langchain_google_genai`) as the LLM, and **Streamlit** for the UI.

---

## Demo
Add your demo URL or GIF here (e.g., Streamlit Cloud or Hugging Face Space).

---

## Key Features
- Multi-turn conversations with session memory  
- LangGraph `StateGraph` orchestration  
- Gemini via `langchain_google_genai` for generation  
- Streamlit UI with markdown rendering  
- Simple, modular backend/frontend separation

---

## Tech
Python 3.9+, LangGraph, LangChain, `langchain_google_genai`, Streamlit, python-dotenv

---

## Quick Start
```bash
git clone https://github.com/Rohit-Shere/Chatbot.git
cd chatbot-project

python -m venv venv
# activate venv:
# Windows: venv\Scripts\activate
# macOS/Linux: source venv/bin/activate

pip install -r requirements.txt
cp .env.example .env
# edit .env -> set GOOGLE_API_KEY

streamlit run chatbot_ui.py
