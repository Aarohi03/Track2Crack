import pandas as pd
from datetime import datetime, timedelta
from motivation import get_motivational_quote

DATA_FILE = 'data/studylog.csv'
TOPICS = ['DSA', 'Aptitude', 'Soft Skills', 'Core Subjects']
THRESHOLD_HOURS = 5

def generate_weekly_report():
    try:
        df = pd.read_csv(DATA_FILE)
    except FileNotFoundError:
        print("❗ No data found. Please log study hours first.")
        return

    today = datetime.now()
    week_ago = today - timedelta(days=7)

    df['Date'] = pd.to_datetime(df['Date'])
    recent_data = df[df['Date'] >= week_ago]


    print(f"\n📊 Weekly Summary ({week_ago.strftime('%b %d')} – {today.strftime('%b %d')}):\n")

    for topic in TOPICS:
        topic_data = recent_data[recent_data['Topic'] == topic]
        total_hours = topic_data['Hours'].sum()
        avg_conf = topic_data['Confidence'].mean()

        if total_hours < THRESHOLD_HOURS:
            print(f"- {topic}: {total_hours} hrs, Avg Confidence: {round(avg_conf,1)} ⚠️ Needs more focus")
        else:
            print(f"- {topic}: {total_hours} hrs, Avg Confidence: {round(avg_conf,1)} ✅ Good progress!")

    print("\n💡 Tip: Try to spend at least 5 hrs/week per area.")
    print(f"\n🔥 Quote of the Week:\n\"{get_motivational_quote()}\"\n")