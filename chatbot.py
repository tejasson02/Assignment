import nltk
from nltk.chat.util import Chat, reflections

patterns = [
    (r'hi|hello|hey', ['Hello!', 'Hi there!', 'Hey!']),
    (r'how are you', ['I am good, thank you!', 'I am doing well.']),
    (r'what is your name', ['I am a chatbot.', 'You can call me ChatGPT.']),
    (r'quit|exit', ['Goodbye!', 'See you later.']),
]

chatbot = Chat(patterns, reflections)


def start_chat():
    print("Hello! I'm a simple chatbot. Type 'quit' to exit.")
    while True:
        user_input = input("You: ")
        if user_input.lower() in ['quit', 'exit']:
            print("Chatbot: Goodbye!")
            break
        else:
            response = chatbot.respond(user_input)
            print("Chatbot:", response)


if __name__ == "__main__":
    nltk.download('punkt')
    start_chat()

# ALSO WE CAN USE BELOW CODE


# import openai
#
# openai.api_key = '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'
#
#
# def ask_gpt3(prompt):
#     response = openai.Completion.create(
#         engine="text-davinci-002",
#         prompt=prompt,
#         max_tokens=150,
#         temperature=0.7,
#         stop=None,
#     )
#
#     return response.choices[0].text.strip()
#
#
# def main():
#     print("Hello! I'm an advanced chatbot powered by GPT-3.")
#     print("You can ask me anything. Type 'quit' to exit.")
#
#     while True:
#         user_input = input("You: ")
#         if user_input.lower() in ['quit', 'exit']:
#             print("Chatbot: Goodbye!")
#             break
#         else:
#             prompt = f"You: {user_input}\nChatbot:"
#             response = ask_gpt3(prompt)
#             print(response)
#
#
# if __name__ == "__main__":
#     main()
