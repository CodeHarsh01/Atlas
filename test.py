from pymongo import MongoClient

uri = "mongodb+srv://Atlas:Atlas12345@cluster0.frwnial.mongodb.net/?appName=Cluster0"

client = MongoClient(uri)

try:
    client.admin.command("ping")
    print("✅ Connected successfully")
except Exception as e:
    print(e)