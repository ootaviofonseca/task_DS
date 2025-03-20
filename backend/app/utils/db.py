from pymongo import MongoClient
from app.config import Config

client = MongoClient(Config.MONGO_URI)
db = client.get_database()  # Conect to the database

# Users collection
users_collection = db.users
