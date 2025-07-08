from rag_agent import ask_with_context

def main():
    while True:
        question = input("Ask a question (or type 'exit'): ")
        if question.lower() in {"exit", "quit"}:
            break
        answer = ask_with_context(question)
        print("\nAnswer:\n", answer)

if __name__ == "__main__":
    main()
