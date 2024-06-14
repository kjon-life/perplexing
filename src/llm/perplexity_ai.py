import requests

url = "https://api.perplexity.ai/chat/completions"

payload = {
    "model": "mixtral-8x7b-instruct",
    "messages": [
        {
            "role": "system",
            "content": "Be precise and concise."
        },
        {
            "role": "user",
            "content": "How many stars are there in our galaxy?"
        }
    ],
    "max_tokens": 4000,
    "temperature": 0.5,
    "top_p": 1,
    "return_citations": False,
    "stream": False,
    "frequency_penalty": 1.5
}
headers = {
    "accept": "application/json",
    "content-type": "application/json"
}

response = requests.post(url, json=payload, headers=headers)

print(response.text)