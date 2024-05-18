import random

# Dictionary of responses
responses = {
    "hello": ["Hello!", "Hi!", "Good day or moring!"],
    "how are you?": ["I'm good, thank you!", "Fantastic!"],
    "what are you doing?": ["Answering to your questions right now now.", "Talking with you, right now."],
    "thank you": ["You're welcome!", "No problem!"],
    "goodbye": ["Goodbye!", "Take care!"]
}

def get_response(user_input):
    if user_input.lower() in responses:
        return random.choice(responses[user_input.lower()])
     else:
         return "Sorry, But Sillo don't found any response message to your message, placeholder!"

def main():
    print("Hello! I'm Sillo, your virtual assistant.")
    while True:
        user_input = input("You: ")
        response = get_response(user_input)
        print("Sillo:", response)

if __name__ == "__main__":
    main()
