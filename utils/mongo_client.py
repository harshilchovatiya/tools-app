from pymongo import MongoClient
from config import config

print("Connecting to MongoDB...")  # Debug line
client = MongoClient(config.MONGO_URI)
print("Connected to MongoDB.")  # Debug line

db = client['tools_db']
urls_collection = db['urls']

print("urls_collection is ready.")  # Debug line
