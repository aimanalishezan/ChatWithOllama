import ollama
import requests

MODEL=""

system_prompt="you are a assistant who ans all kind of questions"
question=input("Ask your qestion")

user_prompt="answer the questions in short and best summary possible"+question

def message():
    return[
        {"role":"system","content":system_prompt},
        {"role":"user","content":user_prompt}
    ]

def llama():
    response=ollama.chat(
        model=MODEL,
        messages=message()

    )
