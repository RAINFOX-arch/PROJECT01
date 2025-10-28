API_URL="https://uselessfacts.jsph.pl/random.json?language=en"
DATA_FILE="data/facts.json"
INTERVAL_MINUTES=1
import requests
from config.settings import API_URL
def fetch_fact():


    response=requests.get(API_URL)
    if response.status_code==200:
        data=response.json()
        return{
            "id":data["id"],
               "text":data["text"],
               "source":data["source_url"]
    }


    else:
        print("API request failed:",response.status.code)
    return None

fact=fetch_fact()
print(fact)