"""
Stop Loss Engine

Uses the stored stop-loss price.
Supports:
- ATR Stop
- Break-even Stop
- Trailing Stop
"""


def stop_loss_hit(
    stop_price,
    current_price
):
    """
    Returns True if current price
    falls below the stored stop price.
    """

    return {

        "stop_price": stop_price,

        "hit": current_price <= stop_price

    }