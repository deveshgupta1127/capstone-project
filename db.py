import pymongo
from datetime import datetime

# MongoDB setup
client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client['health_db']
users_collection = db['users']
health_data_collection = db['health_data']

def find_user(email):
    return users_collection.find_one({"email": email})

def add_user(email, password):
    users_collection.insert_one({"email": email, "password": password})

def validate_user(email, password):
    user = users_collection.find_one({"email": email})
    return user and user['password'] == password

def save_health_data(user_email, data):
    health_data_collection.insert_one({
        "email": user_email,
        "data": data,
        "timestamp": datetime.utcnow()
    })

# Optional: Fetch all data for a user (could be used in future)
def get_user_health_data(email):
    return list(health_data_collection.find({"email": email}))
