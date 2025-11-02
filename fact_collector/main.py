API_URL="https://uselessfacts.jsph.pl/random.json?language=en"
DATA_FILE="data/facts.json"
INTERVAL_MINUTES=1
from json.tool import main
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

import requests
import json
import os
from config.settings import API_URL

DATA_FILE="data/facts.json"
def load_facts():
    if not os.path.exists(DATA_FILE) or os.path.getsize(DATA_FILE) == 0:
        return []
    try:
        with open(DATA_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    except json.JSONDecodeError:
        # 檔案存在但內容不是合法 JSON 時
        return []
    #讀取資料段
def save_facts(facts):
    with open(DATA_FILE,"w",encoding="utf-8" )as f:
        json.dump(facts,f,indent=4,ensure_ascii=False)
        #save slot

    def fetch_fact():
     response = requests.get(API_URL)
     if response.status_code == 200:
        data = response.json()
        return {
            "id": data["id"],
            "text": data["text"],
            "source": data["source_url"]
        }
     else:
        print("API request failed:", response.status_code)
        return None
     def main():
         facts=load_facts()
         new_fact=fetch_fact()


         if new_fact:
             if not any(f["id"]==new_fact["id"]for f in facts ):
                 facts.append(new_fact)
                 save_facts(facts)
                 print("new facts added")
             else:
                 print("already had this,just skipped it")

if __name__=="__main__":
    main()


    import requests

response = requests.get(API_URL)
if response.status_code == 200 and response.text.strip():
    try:
        data = response.json()
    except ValueError:
        print("Received invalid JSON:", response.text)
        data = None
else:
    print("API request failed:", response.status_code)
    data = None

if data:
    fact = {
        "id": data.get("id"),
        "text": data.get("text"),
        "source": data.get("source_url")
    }
    print(fact)
else:
    print("No valid fact retrieved.")
