import json

def load_settings():
    with open(
        "app/config/settings.json",
        "r",
        encoding="utf-8"
    ) as file:

        settings = json.load(file)

    return settings

def load_watchlist():
    with open(
        "app/config/watchlist.json",
        "r",
        encoding="utf-8"
    ) as file:

        watchlist = json.load(file)

    return watchlist["stocks"]

    