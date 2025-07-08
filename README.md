
# 🧠 Local RAG Q&A System (FastAPI + Ollama + LangChain)

This project implements a Retrieval-Augmented Generation (RAG) system using:

- 🗃️ **ChromaDB** for vector storage  
- ✨ **LangChain** for document loading and retrieval  
- 🧠 **Ollama** running **Gemma3:1b** (or any local LLM)  
- ⚡ **FastAPI** to expose the Q&A as an API  

---

## ⚙️ Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/local-rag-api.git
cd local-rag-api
```

### 2. Install Python Dependencies

Ensure you're using Python 3.9–3.11:

```bash
pip install -r requirements.txt
```

### 3. Install and Run Ollama

Install from [https://ollama.com/download](https://ollama.com/download)

Then pull and run the Gemma model:

```bash
ollama run gemma3:1b
```

This will keep the LLM running locally on `http://localhost:11434`.

### 4. Prepare Your Documents

Put your `.pdf` or `.docx` files inside the `Docs/` directory.

Then run:

```bash
python vector.py
```

This will chunk, embed, and store your documents in `chroma_store/`.

### 5. Start the API Server

```bash
uvicorn app:app --reload
```

API will be available at: [http://127.0.0.1:8000](http://127.0.0.1:8000)  
Swagger UI: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

---

## 🧪 How to Test the API

### Endpoint: `POST /ask`

**Request:**

```
POST http://localhost:8000/ask
Content-Type: application/json
```

**Body:**

```json
{
  "question": "Explain the electricity theft case."
}
```

**Response:**

```json
{
  "answer": "[Dakshin Haryana Bijli Vs. Sirohi Medical - Chunk 2]\n...\n\nBased on the above content..."
}
```

Use the Swagger UI for easier testing:  
📍 [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

---

## 🧠 Example Input/Output

### ✅ Input:

```json
{
  "question": "What did the court say about multiplier for deceased?"
}
```

### ✅ Output:

```json
{
  "answer": "[Amrit Bhanu Vs. NIC - Chunk 1]\nThe court ruled that the multiplier should be based on the age of the deceased, not the parents..."
}
```

---

## 📦 Project Structure

```
├── Docs/               # Your source documents (PDF/DOCX)
├── chroma_store/       # Generated vector DB (auto-created)
├── vector.py           # Loads + embeds documents
├── tools.py            # Retrieval logic
├── rag_agent.py        # Core agent with local LLM (Ollama)
├── main.py             # CLI testing (optional)
├── app.py              # FastAPI app
├── requirements.txt    
└── README.md           
```

---

## ✅ Requirements

- Python 3.9–3.11
- Ollama (for local LLMs)
- pip install -r requirements.txt

---

## 📬 Contact

For issues or improvements, open an issue or PR.
