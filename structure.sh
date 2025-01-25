#!/bin/bash

# Define project structure
PROJECT_NAME="flask_mysql_boilerplate"
APP_DIR="${PROJECT_NAME}/app"
MIGRATIONS_DIR="${PROJECT_NAME}/migrations"

# Create project directories
echo "Creating project directories..."
mkdir -p $APP_DIR
mkdir -p $MIGRATIONS_DIR

# Create placeholder files
echo "Creating placeholder files..."
touch $PROJECT_NAME/run.py
touch $PROJECT_NAME/requirements.txt

# Files in app/
touch $APP_DIR/__init__.py
touch $APP_DIR/models.py
touch $APP_DIR/routes.py
touch $APP_DIR/config.py

# Add boilerplate code to files

echo "Adding boilerplate code to files..."

# __init__.py
cat > $APP_DIR/__init__.py <<EOL
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# Initialize the database
db = SQLAlchemy()

def create_app():
    app = Flask(__name__)

    # Load configurations
    app.config.from_object('app.config.Config')

    # Initialize plugins
    db.init_app(app)

    # Register blueprints/routes
    from app.routes import main
    app.register_blueprint(main)

    return app
EOL

# config.py
cat > $APP_DIR/config.py <<EOL
class Config:
    SQLALCHEMY_DATABASE_URI = 'mysql+mysqlconnector://username:password@localhost/db_name'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
EOL

# models.py
cat > $APP_DIR/models.py <<EOL
from app import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

    def __repr__(self):
        return f"<User {self.name}>"
EOL

# routes.py
cat > $APP_DIR/routes.py <<EOL
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
EOL

# run.py
cat > $PROJECT_NAME/run.py <<EOL
from app import create_app, db

app = create_app()

if __name__ == '__main__':
    with app.app_context():
        db.create_all()  # Create tables
    app.run(debug=True)
EOL

# requirements.txt
cat > $PROJECT_NAME/requirements.txt <<EOL
Flask
Flask-SQLAlchemy
mysql-connector-python
EOL

echo "Project structure and boilerplate code generated successfully!"
