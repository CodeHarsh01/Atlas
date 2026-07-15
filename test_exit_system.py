from app.risk.exit_manager import should_exit

print("=" * 70)
print("ATLAS EXIT ENGINE TEST")
print("=" * 70)


def run_test(name, position):

    decision = should_exit(

        score=position["score"],

        current_price=position["current_price"],

        stop_loss=position["stop_loss"],

        buy_date=position["buy_date"],

        time_stop_days=20

    )

    print()

    print("=" * 50)
    print(name)
    print("=" * 50)

    print(f"Score          : {position['score']}")
    print(f"Current Price  : {position['current_price']}")
    print(f"Stop Loss      : {position['stop_loss']}")
    print(f"Buy Date       : {position['buy_date']}")

    print()

    print("Decision")

    print(decision)

    print()


# ==========================================
# TEST 1
# HOLD
# ==========================================

run_test(

    "TEST 1 : HOLD",

    {

        "score": 90,

        "current_price": 200,

        "stop_loss": 180,

        "buy_date": "2026-07-10"

    }

)


# ==========================================
# TEST 2
# STOP LOSS
# ==========================================

run_test(

    "TEST 2 : STOP LOSS",

    {

        "score": 90,

        "current_price": 175,

        "stop_loss": 180,

        "buy_date": "2026-07-10"

    }

)


# ==========================================
# TEST 3
# SELL SIGNAL
# ==========================================

run_test(

    "TEST 3 : SELL SIGNAL",

    {

        "score": 10,

        "current_price": 220,

        "stop_loss": 180,

        "buy_date": "2026-07-10"

    }

)


# ==========================================
# TEST 4
# TIME STOP
# ==========================================

run_test(

    "TEST 4 : TIME STOP",

    {

        "score": 85,

        "current_price": 210,

        "stop_loss": 180,

        "buy_date": "2026-06-01"

    }

)

print("=" * 70)
print("TEST COMPLETE")
print("=" * 70)