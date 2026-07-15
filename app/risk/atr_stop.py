def calculate_atr_stop(
    buy_price,
    atr,
    multiplier=2
):
    """
    Calculate ATR based stop loss.
    """

    stop_loss = buy_price - (atr * multiplier)

    return round(stop_loss, 2)