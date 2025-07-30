import time
import datetime
import pyttsx3

engine = pyttsx3.init()

def speak(text: str):
    engine.say(text)
    engine.runAndWait()

def parse_reminder_time(time_str: str) -> float:
    try:
        reminder_time = datetime.datetime.strptime(time_str, '%I:%M %p')
        now = datetime.datetime.now()
        reminder_datetime = datetime.datetime.combine(now.date(), reminder_time.time())
        if reminder_datetime < now:
            raise ValueError("Reminder time is in the past.")
        return (reminder_datetime - now).total_seconds()
    except ValueError:
        raise

def wait_and_remind(time_to_wait: float, message: str):
    time.sleep(time_to_wait)
    speak(message)
