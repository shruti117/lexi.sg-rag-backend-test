from langchain_community.document_loaders import PyMuPDFLoader, UnstructuredWordDocumentLoader
from langchain_community.vectorstores import Chroma
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings

import os
from pathlib import Path

DOCS_DIR = "Docs"
CHROMA_DIR = "chroma_store"

def load_documents():
    all_docs = []
    for file in Path(DOCS_DIR).glob("*"):
        ext = file.suffix.lower()
        if ext == ".pdf":
            loader = PyMuPDFLoader(str(file))
        elif ext == ".docx":
            loader = UnstructuredWordDocumentLoader(str(file))
        else:
            continue
        docs = loader.load()
        for doc in docs:
            doc.metadata["file_name"] = file.name
        all_docs.extend(docs)
    return all_docs

def chunk_documents(docs):
    splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
    chunks = splitter.split_documents(docs)
    for i, chunk in enumerate(chunks):
        chunk.metadata["chunk_id"] = i + 1
    return chunks

if __name__ == "__main__":
    documents = load_documents()
    chunks = chunk_documents(documents)
    if not chunks:
        raise ValueError("No valid content found in documents.")
    embedding = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
    vectordb = Chroma.from_documents(documents=chunks, embedding=embedding, persist_directory=CHROMA_DIR)
