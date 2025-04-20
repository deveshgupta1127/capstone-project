<<<<<<< HEAD
import os
from pymongo import MongoClient

MONGO_URI = os.getenv('MONGO_URI', 'mongodb://localhost:27017')
client = MongoClient(MONGO_URI)

db = client['health_app']
users = db['users']
health_data = db['health_data']

def add_user(email, password):
    if users.find_one({'email': email}):
        return False
    users.insert_one({'email': email, 'password': password})
    return True

def find_user(email):
    return users.find_one({'email': email})

def validate_user(email, password):
    user = users.find_one({'email': email})
    if user and user['password'] == password:
        return True
    return False

def save_health_data(email, data):
    data['email'] = email
    health_data.insert_one(data)
=======
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
>>>>>>> 586fa6ad2e53dd92bb456fa21097f796060179a0
