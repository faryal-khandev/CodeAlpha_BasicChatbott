def chatbot():
    print("===================================")
    print("          BASIC CHATBOT")
    print("===================================")
    print("Chatbot: Hello! I am a simple chatbot.")
    print("Chatbot: You can say hello, ask how I am, or say bye.")
    print()

    while True:
        user_input = input("You: ").lower()

        if user_input == "hello":
            print("Chatbot: Hi!")

        elif user_input == "how are you":
            print("Chatbot: I'm fine, thanks!")

        elif user_input == "bye":
            print("Chatbot: Goodbye!")
            break

        else:
            print("Chatbot: Sorry, I don't understand that.")


chatbot()

