from datetime import datetime


def chatbot_response(user_input):
    user_input = user_input.lower().strip()

    # Greeting
    if user_input in ["hello", "hi", "hey", "hii",
                      "good morning", "good evening"]:
        return "Hello! 👋 Nice to meet you. How can I help you?"

    # How are you
    elif "how are you" in user_input:
        return "I'm doing great! 😊 Thanks for asking."

    # Chatbot information
    elif "your name" in user_input or "who are you" in user_input:
        return "My name is CodeBot 🤖. I am a simple Python rule-based chatbot."

    elif "what can you do" in user_input:
        return (
            "I can answer basic questions, tell you the date and time, "
            "perform simple calculations, and show chat history."
        )

    # Python information
    elif "python" in user_input:
        return (
            "Python is a popular programming language used in "
            "AI, Machine Learning, Web Development, Data Science and Automation."
        )

    # Internship information
    elif "internship" in user_input:
        return (
            "An internship gives students practical experience "
            "and helps develop technical and professional skills."
        )

    # Study and exam tips
    elif "study" in user_input or "exam" in user_input:
        return (
            "For effective study, make a timetable, practice regularly, "
            "revise important topics and take short breaks."
        )

    # Current time
    elif user_input == "time" or "current time" in user_input:
        current_time = datetime.now().strftime("%I:%M:%S %p")
        return f"The current time is {current_time} ⏰"

    # Current date
    elif user_input == "date" or "today's date" in user_input:
        current_date = datetime.now().strftime("%d-%m-%Y")
        return f"Today's date is {current_date} 📅"

    # Help command
    elif user_input == "help":
        return (
            "\nYou can ask me:\n"
            "1. Hello / Hi\n"
            "2. How are you?\n"
            "3. What is your name?\n"
            "4. What can you do?\n"
            "5. What is Python?\n"
            "6. Tell me about internship\n"
            "7. Give me study tips\n"
            "8. Time\n"
            "9. Date\n"
            "10. Calculate 25 + 15\n"
            "11. History\n"
            "12. Bye"
        )

    # Thank you
    elif "thank you" in user_input or "thanks" in user_input:
        return "You're welcome! 😊"

    # Calculator
    elif user_input.startswith("calculate"):
        try:
            expression = user_input.replace("calculate", "").strip()

            allowed_characters = "0123456789+-*/(). "

            if all(char in allowed_characters for char in expression):
                result = eval(expression)
                return f"The answer is: {result} 🧮"
            else:
                return "Please use only numbers and basic operators (+, -, *, /)."

        except:
            return "Sorry, I could not calculate that."

    # Unknown input
    else:
        return (
            "Sorry, I don't understand that. 😕\n"
            "Type 'help' to see what I can do."
        )


def show_history(history):
    print("\n========== CHAT HISTORY ==========")

    if not history:
        print("No conversation history yet.")
    else:
        for user_message, bot_message in history:
            print(f"You: {user_message}")
            print(f"Bot: {bot_message}")
            print("-" * 40)

    print("==================================")


def main():
    history = []

    print("=" * 55)
    print("              🤖 CODEBOT")
    print("=" * 55)
    print("Hello! I am CodeBot, your simple Python chatbot.")
    print("Type 'help' to see available commands.")
    print("Type 'bye' to exit.")
    print("=" * 55)

    while True:
        user_input = input("\nYou: ").strip()

        # Exit
        if user_input.lower() in ["bye", "exit", "quit"]:
            bot_message = "Goodbye! 👋 Have a great day!"
            print("Bot:", bot_message)
            history.append((user_input, bot_message))
            break

        # Chat history
        if user_input.lower() == "history":
            show_history(history)
            continue

        # Get response
        bot_message = chatbot_response(user_input)

        print("Bot:", bot_message)

        # Store conversation
        history.append((user_input, bot_message))


if __name__ == "__main__":
    main()
