from datetime import datetime
import json
from dataclasses import dataclass
from pymongo import MongoClient

# Dataclasses to represent the data
@dataclass
class UserPreferences:
    timezone: str
    
    def to_dict(self):
        # Convert to dictionary
        return {'timezone': self.timezone}

@dataclass
class User:
    username: str 
    password: str
    roles: list
    preferences: UserPreferences
    active: bool
    created_ts: float

# Conect to MongoDB
client = MongoClient("mongodb://localhost:27017/")
db = client["mydatabase"]
collection = db["users"]

# Function to parse roles
def parse_roles(data):
    roles = []
    if data.get("is_user_admin"):
        roles.append("admin")
    if data.get("is_user_manager"):
        roles.append("manager")
    return roles

# Function to convert timestamp to float 
def convert_timestamp(date_str):
    try:
        dt = datetime.strptime(date_str, "%Y-%m-%dT%H:%M:%SZ")  # ISO 8601
        return dt.timestamp()  # Convert to timestamp to float
    except ValueError:
        return None  # Return None if the date is invalid
    
# Import data from JSON file
with open("Data\data.json", "r") as file:#Open data.json in read mode
    users_data = json.load(file) #Convert the JSON data to a Python dictionary
    
    # Check if the data is valid in the JSON file
    if isinstance(users_data, dict) and "users" in users_data:
        users_data = users_data["users"]  
    else:
        print("Invalid JSON data")
        exit()
    users_to_insert = []

    # Insert data into MongoDB
    for data in users_data:
        user = User(
            username=data["user"],
            password=data["password"],
            roles=parse_roles(data),
            preferences=UserPreferences(timezone=data["user_timezone"]).to_dict(),
            active=True,
            created_ts=convert_timestamp(data["created_at"])
        )

        users_to_insert.append(user.__dict__) 

    collection.insert_many(users_to_insert)#Insert the data into the collection in MongoDB

print("Data inserted successfully")
