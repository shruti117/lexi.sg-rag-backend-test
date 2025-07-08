from fastapi import FastAPI
from pydantic import BaseModel
from rag_agent import ask_with_context

app = FastAPI()

class Query(BaseModel):
    question: str

@app.post("/ask")
def ask(query: Query):
    answer = ask_with_context(query.question)
    return {"answer": answer}
