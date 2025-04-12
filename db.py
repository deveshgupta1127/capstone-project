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
