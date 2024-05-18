import random

# Dictionary of responses
responses = {
    "hello": ["Hello!", "Hi!", "Good day!"],
    "how are you?": ["I'm good, thank you!", "Fantastic!"],
    "what are you doing?": ["Answering your questions.", "Helping you."],
    "thank you": ["You're welcome!", "No problem!"],
    "goodbye": ["Goodbye!", "Take care!"],
    "name": ["My name is Sillo.", "You can call me Sillo."],
    "joke": ["Why couldn't the bicycle find its way home? Because it lost its bearings!", "I told my wife she should embrace her mistakes. She gave me a hug."],
    "help": ["How can I assist you?", "What do you need help with?"],
    "how was your day?": ["My day was good, thank you for asking!", "It's been a busy day, but I'm here to help you."],
    "tell me a fact": ["Did you know that the Eiffel Tower can be 15 cm taller during a summer due to thermal expansion?", "The first oranges weren't orange - they were actually green!"],
    "play me a song": ["I can't play music, but I can recommend some great playlists for you!", "I'm here for a chat, but let me know if you need help with anything else."],
}

def get_response(user_input):
    if user_input.lower() in responses:
        return random.choice(responses[user_input.lower()])
    else:
        return "Sorry, I don't understand your question. If you need help, feel free to ask."

def main():
    print("Hello! I'm Sillo, your virtual assistant.")
    while True:
        user_input = input("You: ")
        response = get_response(user_input)
        print("Sillo:", response)
