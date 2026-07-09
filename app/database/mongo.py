import os

from pymongo import MongoClient

MONGO_URI = os.getenv("MONGO_URI")

client = MongoClient(MONGO_URI)

db = client["atlas"]

positions_collection = db["positions"]
trades_collection = db["trades"]
run_lock_collection = db["run_lock"]
settings_collection = db["settings"]
