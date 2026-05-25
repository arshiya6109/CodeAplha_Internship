import random
import datetime

print("=" * 60)
print("           CODEALPHA SMART CHATBOT")
print("=" * 60)
print("Hello! I am your virtual assistant.")
print("Type 'bye' to end the conversation.\n")

greetings = [
    "Hello!",
    "Hi there!",
    "Nice to see you!",
    "Hey!"
]

while True:

    user = input("You: ").lower().strip()

    if user == "bye":
        print("Bot: Goodbye! Have a wonderful day.")
        break

    elif any(word in user for word in ["hello", "hi", "hey"]):
        print("Bot:", random.choice(greetings))

    elif "how are you" in user:
        print("Bot: I'm doing great! How are you?")

    elif "internship" in user:
        print("Bot: Internships provide real-world experience, help develop professional skills, and improve career opportunities.")

    elif "python" in user:
        print("Bot: Python is a powerful programming language used in web development, AI, automation, data science, and machine learning.")

    elif "name" in user:
        print("Bot: My name is CodeAlpha Smart ChatBot.")

    elif "time" in user:
        current_time = datetime.datetime.now().strftime("%I:%M %p")
        print("Bot: The current time is", current_time)

    elif "date" in user:
        current_date = datetime.datetime.now().strftime("%d-%m-%Y")
        print("Bot: Today's date is", current_date)

    elif "study" in user or "student" in user:
        print("Bot: Consistent study and practice are the keys to academic success.")

    elif "hobby" in user:
        print("Bot: Hobbies help us relax and develop new skills. What is your favorite hobby?")

    elif "career" in user:
        print("Bot: Building skills, gaining experience, and continuous learning are important for a successful career.")

    elif "joke" in user:
        print("Bot: Why do programmers prefer Python? Because it's easy to 'byte' into!")

    elif "help" in user:
        print("Bot: You can ask me about Python, internships, careers, studies, hobbies, time, date, or tell me a joke.")

    elif any(word in user for word in ["good", "fine", "great"]):
        print("Bot: That's good to hear!")

    elif "thank" in user:
        print("Bot: You're welcome!")

    else:
        responses = [
            "That's interesting. Tell me more.",
            "I understand. What else would you like to share?",
            "Can you explain that a little more?",
            "That sounds interesting!",
            "Let's talk more about it."
        ]
        print("Bot:", random.choice(responses))