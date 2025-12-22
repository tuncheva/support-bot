from support_bot import create_thread_and_ask
import sys


def run_once(question: str):
    response, _ = create_thread_and_ask(question)
    print("Question:", question)
    print("\nBot Response:\n", response)


def run_interactive():
    print("Interactive demo. Type 'exit' to quit.")
    while True:
        q = input("You: ").strip()
        if not q:
            continue
        if q.lower() in ("exit", "quit"):
            print("Goodbye")
            break
        response, _ = create_thread_and_ask(q)
        print("Bot:", response)


if __name__ == '__main__':
    # one-shot mode: pass question as CLI args
    if len(sys.argv) > 1:
        question = " ".join(sys.argv[1:])
        run_once(question)
    else:
        run_interactive()
