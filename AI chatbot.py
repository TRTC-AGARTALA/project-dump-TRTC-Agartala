print("🤖 My AI Chatbot")
print("Type 'bye' to exit.")

while True:
    message = input("You: ").lower()

    if message == "hello":
        print("Bot: Hello! How are you?")

    elif message == "how are you":
        print("Bot: I'm doing great! 😊")

    elif message == "what is your name":
        print("Bot: My name is Python Bot.")

    elif message == "bye":
        print("Bot: Goodbye! 👋")
        break

    else:
        print("Bot: I don't understand that yet.")