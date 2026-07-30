import schedule
import time
import subprocess
import os
from datetime import datetime

# Project directory
PROJECT_DIR = os.path.dirname(os.path.abspath(__file__))


def generate_report():
    print(f"\n[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] Generating Shift Handover Report...")

    try:
        subprocess.run(
            ["python3", "main.py"],
            cwd=PROJECT_DIR,
            check=True
        )

        print("✅ Report Generated Successfully.")

    except subprocess.CalledProcessError as e:
        print(f"❌ Report Generation Failed: {e}")


# Shift timings
schedule.every().day.at("06:00").do(generate_report)
schedule.every().day.at("14:00").do(generate_report)
schedule.every().day.at("22:00").do(generate_report)

print("=" * 60)
print("NOC SHIFT HANDOVER BOT SCHEDULER STARTED")
print("=" * 60)
print("Scheduled Times:")
print(" • 06:00 AM")
print(" • 02:00 PM")
print(" • 10:00 PM")
print("=" * 60)

while True:
    schedule.run_pending()
    time.sleep(30)
