# 📄💬 PDF Chatbot

An AI-powered Retrieval-Augmented Generation (RAG) chatbot designed to extract, index, and answer questions seamlessly from uploaded PDF documents. Keep conversations localized, context-aware, and intelligent.

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
