import json
import os
from datetime import datetime
from zoneinfo import ZoneInfo

LOCK_FILE = "app/scheduler/run_lock.json"


def _load():

    if not os.path.exists(LOCK_FILE):

        return {

            "morning": "",

            "afternoon": ""

        }

    with open(LOCK_FILE, "r") as file:

        return json.load(file)


def _save(data):

    with open(LOCK_FILE, "w") as file:

        json.dump(data, file, indent=4)


def already_ran():

    data = _load()

    now = datetime.now(

        ZoneInfo("Asia/Kolkata")

    )

    today = now.strftime("%Y-%m-%d")

    hour = now.hour

    minute = now.minute

    # Morning Session
    if 9 <= hour < 10:

        return data["morning"] == today

    # Afternoon Session
    if 15 <= hour < 16:

        return data["afternoon"] == today

    return False


def mark_run():

    data = _load()

    now = datetime.now(

        ZoneInfo("Asia/Kolkata")

    )

    today = now.strftime("%Y-%m-%d")

    hour = now.hour

    if 9 <= hour < 10:

        data["morning"] = today

    elif 15 <= hour < 16:

        data["afternoon"] = today

    _save(data)