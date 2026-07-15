from datetime import datetime


def time_stop_hit(
    buy_date,
    max_days
):

    buy = datetime.strptime(
        buy_date,
        "%Y-%m-%d"
    )

    today = datetime.now()

    days = (today - buy).days

    return {

        "days": days,

        "hit": days >= max_days

    }