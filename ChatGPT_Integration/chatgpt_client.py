# chatgpt_client.py


import requests
from django.conf import settings

class ChatGPTClient:
    def __init__(self):
        self.api_key = settings.OPENAI_API_KEY
        self.headers = {
            'Authorization': f'Bearer {self.api_key}',
            'Content-Type': 'application/json'  # Explicitly set the Content-Type
        }
        self.endpoint = "https://api.openai.com/v1/chat/completions"#ensure endpoint is only accessed at form submission, not codebase reload when server active

    def get_response(self, messages):
        data = {
            'model': "gpt-3.5-turbo",
            'messages': messages,
            'temperature': 0.7
        }

        print("Sending request to OpenAI API:")
        print("Endpoint:", self.endpoint)
        print("Headers:", self.headers)
        print("Data:", data)

        try:
            response = requests.post(self.endpoint, headers=self.headers, json=data)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"An error occurred: {e}")
            return None

# Usage
client = ChatGPTClient()
messages = [{"role": "user", "content": "Say this is a test!"}]
response = client.get_response(messages)
if response:
    print(response)
else:
    print("No response received.")