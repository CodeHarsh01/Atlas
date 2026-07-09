import os
from pymongo import MongoClient

# MONGO_URI = os.getenv("MONGO_URI")
MONGO_URI = "mongodb+srv://Atlas:Atlas12345@cluster0.frwnial.mongodb.net/?appName=Cluster0"

client = MongoClient(MONGO_URI)

db = client["Atlas"]

# Collections
positions = db["positions"]
trades = db["trades"]
run_lock = db["run_lock"]
settings = db["settings"]

print("✅ MongoDB Connected")
