"""
ATLAS Strategy Test

Purpose:
- Test strategy pipeline only
- No MongoDB
- No Telegram
- No Scheduler
- No Market Hours
"""

from app.config.settings import (
    load_settings,
    load_watchlist
)

from app.market.fetcher import fetch_stock_data
from app.indicators import add_all_indicators

from app.analysis.analysis import analyze_stock
from app.decision.scoring import calculate_score
from app.decision.signal import generate_signal

from app.portfolio.manager import build_portfolio


def strategy_test():

    print("=" * 70)
    print("                 ATLAS STRATEGY TEST")
    print("=" * 70)

    settings = load_settings()
    watchlist = load_watchlist()

    all_stocks = []

    for symbol in watchlist:

        print(f"\nScanning {symbol}...")

        try:

            data = fetch_stock_data(
                symbol + ".NS",
                settings["default_period"],
                settings["default_interval"]
            )

            if data is None or data.empty:
                print("❌ No Data")
                continue

            data = add_all_indicators(data)

            latest = data.iloc[-1]

            analysis = analyze_stock(latest)

            score = calculate_score(analysis)

            signal = generate_signal(score["score"])

            stock = {

                "symbol": symbol,

                "price": round(float(latest["Close"]), 2),

                "atr": round(float(latest["ATR"]), 2),

                "decision": {

                    "score": score["score"],

                    "signal": signal["signal"],

                    "tradable": signal["tradable"]

                }

            }

            all_stocks.append(stock)

            print("-" * 50)
            print(f"Price      : ₹{stock['price']}")
            print(f"ATR        : {stock['atr']}")
            print(f"Score      : {score['score']}")
            print(f"Signal     : {signal['signal']}")
            print(f"Tradable   : {signal['tradable']}")

        except Exception as e:

            print(f"❌ Error scanning {symbol}")
            print(e)

    print("\n")
    print("=" * 70)
    print("BUILDING PORTFOLIO")
    print("=" * 70)

    portfolio = build_portfolio(

        all_stocks,

        settings["capital"]

    )

    if not portfolio:

        print("\nNo Buy Opportunities Found")
        return

    print("\n")
    print("=" * 70)
    print("FINAL PORTFOLIO")
    print("=" * 70)

    for i, stock in enumerate(portfolio, start=1):

        print(f"\nPosition {i}")

        print("-" * 40)

        print(f"Symbol         : {stock['symbol']}")
        print(f"Price          : ₹{stock['price']}")
        print(f"Score          : {stock['score']}")
        print(f"Signal         : {stock['signal']}")

        print(f"Allocation     : ₹{stock['allocation']}")
        print(f"Quantity       : {stock['quantity']}")
        print(f"Capital Used   : ₹{stock['capital_used']}")
        print(f"Remaining      : ₹{stock['remaining']}")
        print(f"Target         : ₹{stock['target']}")
        print(f"Reward/Share   : ₹{stock['reward_per_share']}")
        print(f"Risk Reward    : 1 : {stock['rr']}")

        if "atr" in stock:
            print(f"ATR            : {stock['atr']}")

        if "stop_loss" in stock:
            print(f"Stop Loss      : ₹{stock['stop_loss']}")

        if "risk_per_share" in stock:
            print(f"Risk/Share     : ₹{stock['risk_per_share']}")

    print("\n")
    print("=" * 70)
    print("TEST COMPLETED")
    print("=" * 70)


if __name__ == "__main__":

    strategy_test()