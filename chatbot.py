    def rule_based_chatbot(user_input):
        """
        A simple rule-based chatbot that responds to specific keywords.
        """
        user_input = user_input.lower()

        if "hello" in user_input or "hi" in user_input:
            return "Hello! How can I help you today?"
        elif "how are you" in user_input:
            return "I am doing well, thank you for asking!"
        elif "what is your name" in user_input:
            return "I am a rule-based chatbot."
        elif "help" in user_input:
        return "I can answer simple questions. Try asking 'Hello' or 'How are you?'"
    elif "bye" in user_input or "goodbye" in user_input:
        return "Goodbye! Have a great day!"                            
    else:
        return "I'm sorry, I don't understand. Can you please rephrase your question?"
        else:
            return "I can answer simple questions. Try asking 'Hello' or 'How are you?'"
        elif "bye" in user_input or "goodbye" in user_input:
            return "Goodbye! Have a great day!"                            
        else:
            return "I'm sorry, I don't understand. Can you please rephrase your question?"
    if __name__ == "__main__":
    print("Rule-Based ChatPre: Hello! Type 'bye' to exit.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == "bye":
            print("Rule-Based Chatbot: Goodbye!")
            break
        response = rule_based_chatbot(user_input)
        print("ChatPre:", response)
