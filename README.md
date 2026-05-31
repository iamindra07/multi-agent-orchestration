# 📄 PDF RAG Chatbot with Answer Validation

A Retrieval-Augmented Generation (RAG) chatbot built using **FastAPI**, **ChromaDB**, **Sentence Transformers**, and **Google Gemini**.

The application allows users to upload PDF documents, automatically extracts and embeds the content, stores it in a vector database, retrieves relevant context for user questions, generates answers using Gemini, and performs a second AI-based validation step to improve answer quality.

---

## 🚀 Features

### 📂 PDF Upload

* Upload PDF files through FastAPI endpoints.
* Extracts text from uploaded documents using PyPDF2.

### ✂️ Text Chunking

* Splits extracted text into smaller chunks.
* Removes empty chunks before processing.

### 🧠 Embeddings

* Uses Sentence Transformers (`all-MiniLM-L6-v2`) to convert text into vector embeddings.

### 🗄️ Vector Database

* Stores document chunks and embeddings inside ChromaDB.
* Enables semantic search instead of keyword matching.

### 🔍 Context Retrieval

* Finds the most relevant chunks based on user questions.
* Returns contextual information from uploaded PDFs.

### 🤖 Gemini-Powered Answer Generation

* Uses Google Gemini API to answer questions based on retrieved context.

### ✅ Answer Validation Agent

A second Gemini call reviews the generated answer and:

* Checks whether it is grounded in the retrieved context.
* Identifies hallucinations.
* Suggests an improved answer if necessary.

---

## 🛠️ Tech Stack

* Python
* FastAPI
* ChromaDB
* Sentence Transformers
* Google Gemini API
* PyPDF2
* Uvicorn

---

## 📁 Project Structure

```text
pdf-document-rag/
│
├── main.py
├── requirements.txt
├── .env
├── .gitignore
├── chroma_db/
└── uploaded_pdfs/
```

---

## ⚙️ Installation

### Clone Repository

```bash
git clone https://github.com/yourusername/pdf-document-rag.git
cd pdf-document-rag
```

### Create Virtual Environment

```bash
python -m venv venv
```

### Activate Environment

Windows:

```bash
venv\Scripts\activate
```

Linux/Mac:

```bash
source venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 🔑 Environment Variables

Create a `.env` file:

```env
GEMINI_API_KEY=your_api_key_here
```

---

## ▶️ Run Application

```bash
uvicorn main:app --reload
```

Open Swagger UI:

```text
http://127.0.0.1:8000/docs
```

---

## API Endpoints

### Upload PDF

```http
POST /upload
```

Uploads a PDF, extracts text, generates embeddings, and stores chunks in ChromaDB.

### Ask Question

```http
POST /chat
```

Request:

```json
{
  "question": "What is RAM?"
}
```

Response:

```json
{
  "Question": "What is RAM?",
  "Context": "...",
  "Answer": "...",
  "Revised Answer": "..."
}
```

---

## Example Workflow

1. Upload a PDF document.
2. Text is extracted and chunked.
3. Chunks are converted into embeddings.
4. Embeddings are stored in ChromaDB.
5. User asks a question.
6. Relevant chunks are retrieved.
7. Gemini generates an answer.
8. Gemini validates and improves the answer.

---

## Future Improvements

* PDF chunk overlap
* Multiple document support
* Persistent document storage
* Chat history memory
* Hybrid search (keyword + semantic)
* Frontend UI using React or Streamlit
* Multi-agent orchestration

---

## Learning Outcomes

This project helped me understand:

* Retrieval-Augmented Generation (RAG)
* Vector Databases
* Text Embeddings
* Semantic Search
* FastAPI APIs
* LLM Integration
* Prompt Engineering
* Answer Grounding and Validation

---

## Author

**Indranil Majumder**

Aspiring AI/ML Engineer focused on Python, FastAPI, RAG Systems, LLM Applications, and AI Engineering.
