def calculate_atr_target(price, atr, multiplier=4):
    """
    Calculate ATR based profit target.

    Default:
    Target = Entry + (ATR × 4)
    """

    return round(
        price + (atr * multiplier),
        2
    )