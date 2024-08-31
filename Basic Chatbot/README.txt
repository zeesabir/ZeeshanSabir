Step-by-Step Explanation:
1. Defining the Function:

def chatbot_response(user_input):

Explanation: This line defines a function named chatbot_response. This function takes one argument (user_input), which will be the text input from the user. The function is responsible for handling the chatbot's responses.

2. Converting User Input to Lowercase:

user_input = user_input.lower()

Explanation: This line converts the user input to lowercase. This is done to make the input case-insensitive. For example, "Hello" and "hello" will be treated the same.

3. Defining Pre-Defined Responses:

responses = {
    "hello": "Hello! How can I help you today?",
    "hi": "Hi there! What can I do for you?",
    "how are you": "I'm just a bot, but I'm here to help you!",
    "bye": "Goodbye! Have a great day!",
    "thank you": "You're welcome!",
    "name": "I am a simple chatbot created by a Python developer."
}

Explanation: This block defines a dictionary responses. The dictionary contains key-value pairs where the keys are specific keywords (like "hello", "hi"), and the values are the corresponding responses that the chatbot will give.

4. Looping Through the Dictionary:

for keyword, response in responses.items():
    if keyword in user_input:
        return response

Explanation:
for keyword, response in responses.items(): This loop iterates through each key-value pair in the dictionary. keyword holds the dictionary's key (like "hello"), and response holds the corresponding response (like "Hello! How can I help you today?").
if keyword in user_input: This line checks whether any keyword is present in the user's input.
return response: If a keyword is found in the user input, the function immediately returns the corresponding response.

5. Default Response:

return "I'm sorry, I don't understand that. Can you please rephrase?"

Explanation: If the user's input does not match any of the keywords, the function returns this default response, which is a general message when the chatbot doesn't understand the user's input.

6. Chat Loop:

while True:
    user_input = input("You: ")
    if "bye" in user_input.lower():
        print("Bot: Goodbye! Have a great day!")
        break
    else:
        print("Bot:", chatbot_response(user_input))

Explanation:
while True: This is an infinite loop that allows the chatbot to continuously respond to user inputs.

user_input = input("You: ") This line captures input from the user. The prompt "You: " is displayed.

if "bye" in user_input.lower(): This condition checks if the user's input contains the keyword "bye". If it does, the chatbot gives a farewell message and the loop terminates.

print("Bot: Goodbye! Have a great day!") This line prints the farewell message if the keyword "bye" is detected.

break This breaks the loop and stops the chatbot when the user says "bye".

else: If the user doesn't say "bye", the chatbot passes the user input to the chatbot_response function and prints the response.

Summary:

Function Definition: The function is defined to handle the chatbot's responses.
Lowercasing: The user input is converted to lowercase to maintain case-insensitivity.
Responses Dictionary: A dictionary is used to store predefined responses.
Loop and Condition: The loop and conditions handle keyword matching and responses.
Infinite Chat Loop: The infinite loop provides a mechanism for the chatbot to interact with the user until they say "bye".