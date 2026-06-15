# 📄💬 PDF Chatbot

An AI-powered Retrieval-Augmented Generation (RAG) chatbot designed to extract, index, and answer questions seamlessly from uploaded PDF documents. Keep conversations localized, context-aware, and intelligent.

---

## Preview

          <img width="300" height="500" alt="image" src="https://github.com/user-attachments/assets/dd6d41fc-cd33-4565-afbb-2c596176f7b7" />

          <img width="300" height="500" alt="image" src="https://github.com/user-attachments/assets/a785f85d-193b-4e4a-be69-fc445b4f117b" />

---

## 🌟 Features

- **Multi-PDF Support:** Upload multiple PDF files simultaneously and query across all of them at once.
- **Smart Text Chunking:** Dynamically splits large documents into optimized semantic chunks to retain context while meeting LLM token limitations.
- **Vector Embeddings & Storage:** Generates vector embeddings for high-speed, relevant similarity matching utilizing an integrated semantic search database.
- **Conversational Memory:** Remembers historical queries during the session to provide contextually fluid follow-up responses.
- **Interactive UI:** A modern, minimal, and highly interactive user interface designed for immediate user feedback.

---

## 🛠️ Tech Stack & Architecture

- **Web Framework (Backend):** Flask (Python)
- **Frontend / Templating:** HTML5, CSS3, JavaScript
- **LLM Orchestration:** LangChain
- **LLM Model:** openai/gpt-oss-120b:free
- **Embeddings:** OpenAIEmbeddings 
- **Vector Database:** ChromaDB 

---

## 🚀 Getting Started

Follow these instructions to set up and run the PDF Chatbot locally on your machine.

### Prerequisites

Make sure you have Python 3.9 or higher installed. You can check your version by running:
```bash
python --version
