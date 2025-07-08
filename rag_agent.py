from tools import retrieve_context
from ollama import Client

client = Client(host='http://localhost:11434')

def ask_with_context(query: str) -> str:
    context = retrieve_context.invoke(query)
    prompt = f"{context}\n\nAnswer the question based only on the above content:\n{query}"

    response = client.chat(
        model='gemma3:1b',
        messages=[{"role": "user", "content": prompt}]
    )
    return response['message']['content']
