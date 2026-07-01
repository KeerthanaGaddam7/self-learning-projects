from pymongo import MongoClient

client = MongoClient(
    "mongodb://keerthana:admin123@localhost:27017/?authSource=admin"
)

try:
    print("Connected Databases:", client.list_database_names())
except Exception as e:
    print("Mongo Error:", e)

db = client["risk_library"]
risk_collection = db["risks"]