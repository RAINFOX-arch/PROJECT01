import json
import os
from config.settings import DATA_FILE

def load_facts():
   
    os.makedirs("data", exist_ok=True)

    if not os.path.exists(DATA_FILE) or os.path.getsize(DATA_FILE) == 0:
        return []

    try:
        with open(DATA_FILE, "r", encoding="utf-8") as f:
            content = f.read().strip()

        if not content:
            return []

        return json.loads(content)

    except json.JSONDecodeError:
        print("⚠️ facts.json 格式毀損，重置為空白狀態")
        return []


def save_facts(facts):
    """將資料寫回 facts.json"""
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(facts, f, indent=4, ensure_ascii=False)