import ollama

MODEL = "CognitiveComputations/dolphin-llama3.1"

system_prompt = "You are an assistant who answers all kinds of questions."

question = input("Ask your question: ")

user_prompt = "Answer the question in a short and best summary possible: " + question

def message():
    return [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": user_prompt}
    ]

def llama():
    response = ollama.chat(
        model=MODEL,
        messages=message()
    )
    return response['message']['content']  # Extract the response text

# Call the function and print the output
print("\n🤖 AI Response:")
print(llama())
