def update_trailing_stop(
    highest_price,
    atr,
    current_stop,
    multiplier=2
):
    """
    Move stop upward only.

    Never move stop downward.
    """

    new_stop = round(

        highest_price - (atr * multiplier),

        2

    )

    return max(

        current_stop,

        new_stop

    )