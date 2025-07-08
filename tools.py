from langchain_chroma import Chroma
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_core.tools import tool

embedding = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
vectordb = Chroma(persist_directory="chroma_store", embedding_function=embedding)
retriever = vectordb.as_retriever()

@tool
def retrieve_context(question: str) -> str:
    """Retrieve context from documents for a given question."""
    docs = retriever.invoke(question)
    if not docs:
        return "No relevant context found."
    return "\n\n".join(
        f"[{doc.metadata.get('file_name', 'Unknown')} - Chunk {doc.metadata.get('chunk_id', 'N/A')}]\n{doc.page_content}"
        for doc in docs
    )
