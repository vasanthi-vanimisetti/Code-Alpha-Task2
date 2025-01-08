# Define a dictionary of FAQs and responses
FAQ_RESPONSES = {
    "what is your name": "I am FAQBot, here to help you with your questions!",
    "how can i reset my password": "To reset your password, go to the login page and click 'Forgot Password'.",
    "what are your working hours": "Our working hours are 9 AM to 5 PM, Monday to Friday.",
    "where are you located": "We are located at 1234 Elm Street, Springfield.",
    "how can i contact support": "You can contact support by emailing support@example.com or calling (123) 456-7890.",
}

# Function to process user input and find a matching FAQ response
def get_response(user_input):
    user_input = user_input.lower().strip()  # Normalize input
    for question, response in FAQ_RESPONSES.items():
        if question in user_input:  # Check for a match
            return response
    return "I'm sorry, I don't have an answer for that. Can you rephrase your question?"

# Main chatbot loop
def chatbot():
    print("Welcome to FAQBot! Type 'exit' to end the chat.")
    while True:
        user_input = input("\nYou: ")
        if user_input.lower() == "exit":
            print("FAQBot: Goodbye! Have a great day!")
            break
        response = get_response(user_input)
        print(f"FAQBot: {response}")

# Run the chatbot
chatbot()