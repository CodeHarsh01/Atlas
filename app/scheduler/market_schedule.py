from datetime import datetime
from zoneinfo import ZoneInfo


def should_run():

    now = datetime.now(
        ZoneInfo("Asia/Kolkata")
    )

    minutes = now.hour * 60 + now.minute

    morning_start = 9 * 60 + 15
    morning_end = 9 * 60 + 30

    afternoon_start = 15 * 60 + 30
    afternoon_end = 15 * 60 + 45

    return (

        morning_start <= minutes < morning_end

        or

        afternoon_start <= minutes < afternoon_end

    )