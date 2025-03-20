from flask import request, jsonify
from app.utils.db import users_collection
from datetime import datetime
from bson import ObjectId  

def home():
    return 'Hello, World!'

# Get All Users
def get_users():
    users = users_collection.find()
    result = []
    for user in users:
        user['_id'] = str(user['_id'])
        result.append(user)
    return jsonify(result)

# Get one User
def get_user(user_id):
    user_object_id = ObjectId(user_id)
    user = users_collection.find_one({'_id': user_object_id})
    if user:
        user['_id'] = str(user['_id'])
        return jsonify(user)
    return jsonify({'message': 'User not found'}), 404
    
# Create User
def create_user():
    data = request.get_json()

    # Data validation to check if username and password are present
    if not data.get('username') or not data.get('password'):
        return jsonify({'message': 'Username and password are required'}), 400

    user_data = {
        'username': data['username'],
        'password': data['password'],
        'roles': data.get('roles', []),
        'preferences': data.get('preferences', {}),
        'active': data.get('active', True),
        'created_ts': datetime.utcnow().timestamp()
    }

    # Insert user data into the database
    users_collection.insert_one(user_data)

    return jsonify({'message': 'User created successfully'}), 201

# Edit User
def edit_user(user_id):
    data = request.get_json()
    
    # Uptade user data
    updated_data = {
        'username': data['username'],
        'password': data['password'],
        'roles': data.get('roles', []),
        'preferences': data.get('preferences', {}),
        'active': data.get('active', True),
        'updated_ts': datetime.utcnow().timestamp()
    }
    object_id = ObjectId(user_id)
    # Update in the database
    result = users_collection.update_one({'_id': object_id}, {'$set': updated_data})

    if result.matched_count == 0:
        return jsonify({'message': 'User not found'}), 404

    return jsonify({'message': 'User updated successfully'})

# Delete user
def delete_user(user_id):

    # Converte o user_id para ObjectId
    user_object_id = ObjectId(user_id)
    

    result = users_collection.delete_one({'_id': user_object_id})

    if result.deleted_count == 0:
        return jsonify({'message': 'User not found'}), 404

    return jsonify({'message': 'User deleted successfully'})
