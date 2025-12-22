from dotenv import load_dotenv

load_dotenv()

from support_bot import handle_user_query

print("Smart Customer Support Bot")
print("Ask about products or order status (ORD123)")
print("Type 'exit' to quit\n")

while True:
    user_input = input("You: ")

    if user_input.lower() == "exit":
        print("Goodbye!")
        break

    response = handle_user_query(user_input)
    print("Bot:", response)
