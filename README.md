---
title: DocuMind-AI
emoji: 📄
colorFrom: blue
colorTo: purple
sdk: docker
pinned: false
---

# 📄 DocuMind-AI

An intelligent document assistant powered by RAG, LangChain, Groq LLaMA 3, and FAISS. Upload any PDF and chat with it using state-of-the-art AI — built for real-world enterprise use.

## 🚀 Features
- Upload any PDF
- Ask questions in natural language
- Get accurate answers powered by LLaMA 3
- Chat history support

---
title: DocuMind-AI
emoji: 📄
colorFrom: blue
colorTo: purple
sdk: docker
pinned: false
---

# 📄 DocuMind-AI — Intelligent Document Assistant

An enterprise-grade RAG (Retrieval Augmented Generation) chatbot that allows users to upload any PDF and interact with it using natural language. Built with LangChain, Groq LLaMA 3, FAISS, and Streamlit.

🔗 Live Demo: [huggingface.co/spaces/Yugadharshini/DocuMind-AI](https://huggingface.co/spaces/Yugadharshini/DocuMind-AI)
🔗 GitHub: [github.com/skrYugadharshini/DocuMind-AI](https://github.com/skrYugadharshini/DocuMind-AI)

---

## 🚀 Features

- Upload any PDF document
- Ask questions in natural language
- Semantic search using FAISS vector store
- Fast and accurate answers powered by Groq LLaMA 3
- Chat history support
- Clean and intuitive Streamlit UI
- Deployed on Hugging Face Spaces using Docker

---

## 🛠️ Tech Stack

| Technology | Purpose |
|---|---|
| Python | Core programming language |
| LangChain | LLM orchestration framework |
| Groq LLaMA 3 | Large Language Model for answer generation |
| FAISS | Vector store for semantic search |
| HuggingFace Sentence Transformers | Text embeddings (all-MiniLM-L6-v2) |
| Streamlit | Frontend UI |
| PyPDF | PDF loading and parsing |
| Docker | Containerization for deployment |
| Hugging Face Spaces | Cloud deployment |

---

## ⚙️ Full Technical Process

### Step 1 — PDF Loading
- User uploads any PDF through the Streamlit UI
- PyPDF loads and extracts text from all pages

### Step 2 — Text Chunking
- Document split into chunks of 500 characters
- 50 character overlap between chunks to preserve context
- Uses LangChain RecursiveCharacterTextSplitter

### Step 3 — Vector Embeddings
- Each chunk converted to a 384-dimensional vector
- Uses HuggingFace sentence-transformers (all-MiniLM-L6-v2)
- Captures semantic meaning of text

### Step 4 — Vector Store
- All vectors stored in FAISS index
- Enables fast similarity search across all chunks
- Finds most relevant chunks for any question

### Step 5 — RAG Chain
- User asks a question
- Question converted to vector
- FAISS retrieves top 4 most relevant chunks
- Chunks + question sent to Groq LLaMA 3
- LLaMA 3 generates accurate answer based on context

### Step 6 — Response
- Answer displayed in Streamlit chat UI
- Chat history maintained during session

---


## 🛠️ Built With
- LangChain
- Groq (LLaMA 3)
- FAISS Vector Store
- HuggingFace Embeddings
- Streamlit

## ⚙️ How to Run
1. Clone the repo
2. Install dependencies: `pip install -r requirements.txt`
3. Add your Groq API key in `.env`
4. Run: `streamlit run app.py`

## 🎯 Future Improvements

- Add chat history memory across sessions
- Support multiple PDF uploads
- Highlight source chunks in the PDF
- Add support for other document types (DOCX, TXT)
- Fine-tune chunk size for better accuracy
- Add user authentication

---

## 👩‍💻 Author

**Yugadharshini**
- GitHub: [@skrYugadharshini](https://github.com/skrYugadharshini)
- Hugging Face: [@Yugadharshini](https://huggingface.co/Yugadharshini)