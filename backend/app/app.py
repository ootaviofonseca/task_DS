from flask import Flask
from flask_cors import CORS
from app.routes import get_users, create_user, edit_user, delete_user, home, get_user
def create_app():
    app = Flask(__name__)
    app.config.from_object('app.config.Config')

    #Cors for cross origin requests
    CORS(app)

    # Importing routes
    app.add_url_rule('/', view_func=home, methods=['GET'])
    app.add_url_rule('/api/users', view_func=get_users, methods=['GET'])
    app.add_url_rule('/api/users/<user_id>', view_func=get_user, methods=['GET'])
    app.add_url_rule('/api/users', view_func=create_user, methods=['POST'])
    app.add_url_rule('/api/users/<user_id>', view_func=edit_user, methods=['PUT'])
    app.add_url_rule('/api/users/<user_id>', view_func=delete_user, methods=['DELETE'])

    return app
