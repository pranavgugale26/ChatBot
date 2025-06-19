from groq import Groq
from dotenv import load_dotenv
import os

load_dotenv()

API_KEY = os.getenv('GROQ_API_KEY')

client = Groq(api_key=API_KEY)  # Replace with your key

print("Chatbot is ready. Type 'exit' to quit.\n")

while True:
    user_input = input("You: ")
    if user_input.lower() == "exit":
        print("Bot: Goodbye! 👋")
        break

    completion = client.chat.completions.create(
        model="llama3-70b-8192",
        messages=[
            {"role": "system", "content": "you are a simple indian chatbot"},
            {"role": "user", "content": user_input}],
        temperature=1,
        max_completion_tokens=1024,
        top_p=1,
        stream=True,
        stop=None,
    )   

    print("Bot:", end=" ", flush=True)
    for chunk in completion:
        print(chunk.choices[0].delta.content or "", end="", flush=True)
    print("\n")