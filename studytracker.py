import pandas as pd
import os
from datetime import datetime

DATA_FILE = 'data/studylog.csv'
TOPICS = ['DSA', 'Aptitude', 'Soft Skills', 'Core Subjects']

def init_data_file():
    if not os.path.exists('data'):
        os.makedirs('data')
    if not os.path.isfile(DATA_FILE):
        df = pd.DataFrame(columns=['Date', 'Topic', 'Hours', 'Confidence'])
        df.to_csv(DATA_FILE, index=False)

def add_daily_entry():
    init_data_file()
    today = datetime.now().strftime("%d-%m-%Y")
    entries = []

    print(f"\n📆 Logging study data for: {today}\n")
    for topic in TOPICS:
        try:
            hrs = float(input(f"⏱️ Hours spent on {topic}: "))
            conf = int(input(f"💪 Confidence level in {topic} (0–10): "))
            entries.append([today, topic, hrs, conf])
        except ValueError:
            print("❗ Invalid input. Skipping this topic.\n")

    df = pd.read_csv(DATA_FILE)
    new_df = pd.DataFrame(entries, columns=['Date', 'Topic', 'Hours', 'Confidence'])
    df = pd.concat([df, new_df], ignore_index=True)
    df.to_csv(DATA_FILE, index=False)

    print("\n✅ Entry saved successfully!\n")

if __name__ == "__main__":
    add_daily_entry()