import schedule
import time
import subprocess
def run_collector():
    subprocess.run(["python","fact_collector/main.py"])
    schedule.every().day.at("00:00").do(run_collector)
    print("自動排程啟動中...（按 Ctrl + C 結束）")
while True:
    schedule.run_pending()
    time.sleep(1)
