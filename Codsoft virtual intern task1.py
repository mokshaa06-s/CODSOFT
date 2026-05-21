print("===================================")
print("      SIMPLE RULE-BASED CHATBOT")
print("===================================")
print("Type 'bye' to exit the chatbot.\n")


while True:

    
    user_input = input("You: ").lower()

    if user_input in ["hi", "hello", "hey"]:
        print("Alexa: Hello! How can I help you today?")

    elif "your name" in user_input:
        print("Alexa: I am a Rule-Based Chatbot created using Python.")

    elif "how are you" in user_input:
        print("Alexa: I am doing great! Thank you for asking.")

    elif "time" in user_input:
        from datetime import datetime
        current_time = datetime.now().strftime("%I:%M %p")
        print("Alexa: Current time is", current_time)

    elif "date" in user_input:
        from datetime import date
        today = date.today()
        print("Alexa: Today's date is", today)

    elif "python" in user_input:
        print("Alexa: Python is a popular programming language used for AI, Web Development, and Data Science.")

    elif "help" in user_input:
        print("Alexa: You can ask me about time, date, Python, or greetings.")

    elif user_input == "bye":
        print("Alexa: Goodbye! Have a nice day.")
        break
    
    else:
        print("Alexa: Sorry, I don't understand that.")
