# Reminder CLI

🔔 A CLI tool to set audible reminders using natural language time.

## Features

- Natural time input: `"10:30 AM"`
- Snooze + repeat
- Audible reminder with TTS
- Configurable via CLI flags

## Usage

````bash
poetry run python reminder/cli.py remind --time-str "9:00 PM" --message "Workout time" --snooze 5 --repeat 60
yaml
Copy
Edit

---

## 🧪 `tests/test_core.py`

```python
from reminder.core import parse_reminder_time
import pytest

def test_valid_time_future():
    future = "11:59 PM"
    seconds = parse_reminder_time(future)
    assert seconds > 0

def test_invalid_format():
    with pytest.raises(ValueError):
        parse_reminder_time("25:00")
````
