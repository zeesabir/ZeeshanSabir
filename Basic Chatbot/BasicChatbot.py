def chatbot_response(user_input):
    # Convert user input to lowercase for case-insensitive matching
    user_input = user_input.lower()

    # Pre-defined responses based on keywords
    responses = {
        "hello": "Hello! How can I help you today?",
        "hi": "Hi there! What can I do for you?",
        "how are you": "I'm just a bot, but I'm here to help you!",
        "bye": "Goodbye! Have a great day!",
        "thank you": "You're welcome!",
        "name": "I am a simple chatbot created by a Python developer."
    }

    # Loop through the dictionary to find a keyword match
    for keyword, response in responses.items():
        if keyword in user_input:
            return response

    # Default response if no keyword is matched
    return "I'm sorry, I don't understand that. Can you please rephrase?"

# Simple loop to keep the chatbot running until the user says 'bye'
while True:
    user_input = input("You: ")
    if "bye" in user_input.lower():
        print("Bot: Goodbye! Have a great day!")
        break
    else:
        print("Bot:", chatbot_response(user_input))
