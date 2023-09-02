import requests
import os

# Here the example used is the 'Roberta' model for sentiment analysis in english
# https://huggingface.co/cardiffnlp/twitter-roberta-base-sentiment-latest

API_URL = "https://api-inference.huggingface.co/models/cardiffnlp/twitter-roberta-base-sentiment-latest"
headers = {"Authorization": f"Bearer {os.environ.get('HUGGINGFACE_API_KEY')}"}


def query(payload):
    response = requests.post(API_URL, headers=headers, json=payload)
    return response.json()


tweet = "Just woke up to the most beautiful sunrise 🌅☀️ Feeling incredibly grateful for the simple joys in life. Let's make today amazing, everyone! 💪😄 #Gratitude #PositiveVibes"
output = query({"inputs": tweet})
print(output[0])
