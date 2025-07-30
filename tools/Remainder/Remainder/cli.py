import typer
from reminder.core import parse_reminder_time, wait_and_remind
import datetime
import time

app = typer.Typer()

@app.command()
def remind(
    time_str: str = typer.Option(..., help="Reminder time (e.g. '9:00 AM')"),
    message: str = typer.Option(..., help="Reminder message"),
    snooze: int = typer.Option(5, help="Snooze duration in minutes"),
    repeat: int = typer.Option(60, help="Repeat interval in minutes")
):
    """
    Set a reminder at a specific time, with snooze and repeat functionality.
    """
    try:
        while True:
            seconds = parse_reminder_time(time_str)
            reminder_time = datetime.datetime.now() + datetime.timedelta(seconds=seconds)
            typer.echo(f"Waiting until {reminder_time.strftime('%I:%M %p')} to remind...")

            wait_and_remind(seconds, message)

            while True:
                user_input = input(f"Enter 's' to snooze for {snooze} mins or 'x' to stop: ").strip().lower()
                if user_input == 's':
                    typer.echo(f"Snoozing for {snooze} mins...")
                    time.sleep(snooze * 60)
                    wait_and_remind(0, message)
                elif user_input == 'x':
                    typer.echo("Exiting reminder.")
                    raise typer.Exit()
                else:
                    typer.echo("Invalid input.")
            
            typer.echo(f"Repeating reminder in {repeat} mins...")
            time.sleep(repeat * 60)

    except ValueError as e:
        typer.echo(f"Error: {e}")
