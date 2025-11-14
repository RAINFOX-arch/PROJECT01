import requests
from config.settings import API_URL

def fetch_fact():
   
    response = requests.get(API_URL)

    if response.status_code == 200:
        data = response.json()
        return {
            "id": data["id"],
            "text": data["text"],
            "source": data["source_url"]
        }

    print("API request failed:", response.status_code)
    return None