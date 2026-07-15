from app.risk.time_stop import time_stop_hit
from app.risk.sell_signal import generate_sell_signal
from app.risk.stoploss import stop_loss_hit


def should_exit(
    score,
    current_price,
    stop_loss,
    buy_date,
    time_stop_days
):
    """
    Master Exit Decision
    """

    # ==========================
    # Technical SELL Signal
    # ==========================

    sell = generate_sell_signal(score)

    if sell["exit"]:

        return {

            "exit": True,

            "reason": "SELL_SIGNAL"

        }

    # ==========================
    # Stop Loss
    # ==========================

    stop = stop_loss_hit(

        stop_price=stop_loss,

        current_price=current_price

    )

    if stop["hit"]:

        return {

            "exit": True,

            "reason": "STOP_LOSS"

        }

    # ==========================
    # Time Stop
    # ==========================

    time = time_stop_hit(

        buy_date=buy_date,

        max_days=time_stop_days

    )

    if time["hit"]:

        return {

            "exit": True,

            "reason": "TIME_STOP"

        }

    # ==========================
    # Hold
    # ==========================

    return {

        "exit": False,

        "reason": "HOLD"

    }