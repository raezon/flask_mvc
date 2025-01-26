import jwt
import datetime
from app.models.user import User
from app import db
import os


def create_user(name, email, password):
    if User.query.filter_by(email=email).first():
        return {"error": "Email already exists"}, 400

    # Create user with default role as 'USER'
    user = User(name=name, email=email, role='USER')  # Setting role to 'USER'
    user.set_password(password)
    db.session.add(user)
    db.session.commit()
    return {"message": "User created successfully"}, 201


def authenticate_user(email, password):
    user = User.query.filter_by(email=email).first()
    if user and user.check_password(password):
        token = jwt.encode(
            {
                "user_id": user.id,
                "exp": datetime.datetime.utcnow() + datetime.timedelta(hours=2),
                "role": user.role  # Adding role to the token
            },
            os.getenv("SECRET_KEY"),
            algorithm="HS256",
        )
        return {"token": token, "role": user.role}, 200
    return {"error": "Invalid credentials"}, 401


def change_user_password(user_id, old_password, new_password):
    user = User.query.get(user_id)
    if not user:
        return {"error": "User not found"}, 404

    if not user.check_password(old_password):
        return {"error": "Old password is incorrect"}, 403

    user.set_password(new_password)
    db.session.commit()
    return {"message": "Password updated successfully"}, 200
