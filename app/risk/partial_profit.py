def should_partial_book(
    current_price,
    target,
    partial_booked
):

    """
    Decide whether partial profit should be booked.
    """

    if partial_booked:
        return False

    return current_price >= target