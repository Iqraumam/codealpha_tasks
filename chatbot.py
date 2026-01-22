

def get_reply(message):
    message = message.lower()

    if "hello" in message or "hi" in message:
        return "Hello! Nice to talk to you 🙂"

    elif "how are you" in message:
        return "I'm doing well. Hope you are too!"

    elif "name" in message:
        return "I'm a simple chatbot made using Python."

    elif "college" in message:
        return "College life teaches a lot beyond books!"

    elif "bye" in message or "exit" in message:
        return "Goodbye! Take care 👋"

    else:
        return "I'm still learning. Try asking something else."

print("🤖 Chatbot started. Type 'exit' to end.\n")

while True:
    user_text = input("You: ")
    bot_reply = get_reply(user_text)
    print("Bot:", bot_reply)

    if "bye" in user_text.lower() or "exit" in user_text.lower():
        break
