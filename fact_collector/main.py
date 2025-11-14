
from core.fetcher import fetch_fact
from core.storage import load_facts, save_facts
from core.validator import is_duplicate

def main():
    facts = load_facts()
    new_fact = fetch_fact()

    if not new_fact:
        print("❌ 無法取得資料，略過")
        return

    if is_duplicate(new_fact, facts):
        print("⚠️ 重複資料，跳過")
    else:
        facts.append(new_fact)
        save_facts(facts)
        print("✅ 新資料已新增！")
        print(new_fact)

if __name__ == "__main__":
    main()