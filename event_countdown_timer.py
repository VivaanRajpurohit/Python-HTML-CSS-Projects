from datetime import datetime

def countdown(event_date):
    current_date = datetime.now()
    delta = event_date - current_date
    print(f"Days until event: {delta.days}")

event_Date = datetime(2025, 5, 24)
countdown(event_Date)
rew 