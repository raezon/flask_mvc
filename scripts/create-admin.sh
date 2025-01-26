#!/bin/bash

# Variables for the admin user
ADMIN_NAME="Admin"
ADMIN_EMAIL="admin@example.com"
ADMIN_PASSWORD="adminpassword"

# Activate your Flask virtual environment (if needed)
# source path/to/your/virtualenv/bin/activate

# Create the admin user using Flask CLI (or directly from your Python application)
export FLASK_APP=your_flask_app.py
export FLASK_ENV=development  # Set to 'production' in production

# Run the script to create the admin user
flask shell << EOF
from app.services.user_service import create_user
from app import db

# Call the create_user function to create the admin user
create_user('$ADMIN_NAME', '$ADMIN_EMAIL', '$ADMIN_PASSWORD')

# Commit the changes to the database
db.session.commit()
EOF

echo "Admin user created successfully with email: $ADMIN_EMAIL"
