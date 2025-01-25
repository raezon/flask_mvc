from flask import Blueprint, jsonify
from app.models import User

main = Blueprint('main', __name__)

@main.route('/')
def home():
    return jsonify(message="Welcome to Flask with MySQL Boilerplate")

@main.route('/users', methods=['GET'])
def get_users():
    users = User.query.all()
    return jsonify(users=[{"id": user.id, "name": user.name, "email": user.email} for user in users])
