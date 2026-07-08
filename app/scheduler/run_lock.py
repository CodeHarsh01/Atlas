import json
from pathlib import Path
from datetime import datetime
from zoneinfo import ZoneInfo

LOCK_FILE = Path("run_lock.json")


def current_session():
    now = datetime.now(ZoneInfo("Asia/Kolkata"))

    if now.hour < 12:
        return "morning"

    return "afternoon"


def already_ran():
    today = datetime.now(
        ZoneInfo("Asia/Kolkata")
    ).strftime("%Y-%m-%d")

    session = current_session()

    if not LOCK_FILE.exists():
        return False

    with open(LOCK_FILE, "r") as file:
        data = json.load(file)

    return (
        data.get(today, {})
        .get(session, False)
    )


def mark_run():
    today = datetime.now(
        ZoneInfo("Asia/Kolkata")
    ).strftime("%Y-%m-%d")

    session = current_session()

    if LOCK_FILE.exists():

        with open(LOCK_FILE, "r") as file:
            data = json.load(file)

    else:
        data = {}

    if today not in data:
        data[today] = {}

    data[today][session] = True

    with open(LOCK_FILE, "w") as file:
        json.dump(data, file, indent=4)