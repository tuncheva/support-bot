from support_bot import create_thread_and_ask

question = "What's the price of the 'Pro' model, and what's the status of order #12345?"
reply, debug = create_thread_and_ask(question)

print("Q:", question)
print("A:", reply)
print("Debug:", debug)
