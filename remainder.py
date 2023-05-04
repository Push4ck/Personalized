import time
import datetime
import pyttsx3

# Set up text-to-speech engine
engine = pyttsx3.init()

# Define function to get user input for reminder time
def get_reminder_time():
    while True:
        reminder_time_str = input("Enter the reminder time (e.g. '9:00 AM' or '12:00 PM'): ")
        try:
            reminder_time = datetime.datetime.strptime(reminder_time_str, '%I:%M %p')
            now = datetime.datetime.now()
            reminder_datetime = datetime.datetime.combine(now.date(), reminder_time.time())
            if reminder_datetime < now:
                print("Error: The reminder time specified is in the past.")
            else:
                time_to_wait = (reminder_datetime - now).total_seconds()
                return time_to_wait
        except ValueError:
            print("Error: Invalid time format. Please enter a time in the format '9:00 AM' or '12:00 PM'.")
        except OverflowError:
            print("Error: The reminder time specified is out of range.")

# Define function to get user input for snooze time
def get_snooze_time():
    while True:
        snooze_time_str = input("Enter the snooze time in minutes (e.g. '5' for 5 minutes): ")
        try:
            snooze_time = int(snooze_time_str)
            if snooze_time <= 0:
                print("Error: The snooze time must be a positive integer.")
            else:
                return snooze_time
        except ValueError:
            print("Error: Invalid snooze time. Please enter a positive integer.")

# Define function to get user input for reminder message
def get_reminder_message():
    reminder_message = input("Enter the reminder message: ")
    return reminder_message

# Define function to get user input for repeat frequency
def get_repeat_frequency():
    while True:
        repeat_frequency_str = input("Enter the repeat frequency in minutes (e.g. '60' for every hour): ")
        try:
            repeat_frequency = int(repeat_frequency_str)
            if repeat_frequency <= 0:
                print("Error: The repeat frequency must be a positive integer.")
            else:
                return repeat_frequency
        except ValueError:
            print("Error: Invalid repeat frequency. Please enter a positive integer.")

# Define function to set up and start the text-to-speech engine
def speak(text):
    engine.say(text)
    engine.runAndWait()

# Get user input for reminder time, snooze time, reminder message, and repeat frequency
reminder_time = get_reminder_time()
snooze_time = get_snooze_time()
reminder_message = get_reminder_message()
repeat_frequency = get_repeat_frequency()

# Loop through reminders
while True:
    # Calculate time until next reminder
    time_to_wait = get_reminder_time()
    reminder_time = datetime.datetime.now() + datetime.timedelta(seconds=time_to_wait)
    # Wait for time until next reminder
    time.sleep(time_to_wait)
    # Speak reminder message
    speak(reminder_message)
    # Check if user wants to snooze or stop reminders
    while True:
        snooze_or_stop = input("Enter 's' to snooze for {} minutes or 'x' to stop reminders: ".format(snooze_time))
        if snooze_or_stop == 's':
            reminder_time += datetime.timedelta(minutes=snooze_time)
            break
        elif snooze_or_stop == 'x':
            exit()
        else:
            print("Error: Invalid input. Please enter 's' or 'x'.")
