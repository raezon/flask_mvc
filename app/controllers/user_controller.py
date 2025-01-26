from flask import Blueprint, render_template, request, redirect, url_for, flash, session
from app.services.user_service import create_user, authenticate_user, change_user_password
from app.models.user import User
from flask_jwt_extended import jwt_required, get_jwt_identity
from app import db

auth_bp = Blueprint("auth", __name__, template_folder="templates/auth")


@auth_bp.route("/signup", methods=["GET", "POST"])
def handle_signup():
    if request.method == "POST":
        name = request.form.get("name")
        email = request.form.get("email")
        password = request.form.get("password")

        try:
            create_user(name, email, password)
            flash("Signup successful! Please sign in.", "success")
            return redirect(url_for("auth.signin"))
        except ValueError as e:
            flash(str(e), "error")

    return render_template("auth/signup.html")


@auth_bp.route("/signin", methods=["GET", "POST"])
def handle_signin():
    if request.method == "POST":
        email = request.form.get("email")
        password = request.form.get("password")

        try:
            user, token = authenticate_user(email, password)
            session["user_id"] = user.id
            session["jwt"] = token
            flash("Signin successful!", "success")
            return redirect(url_for("auth.dashboard"))
        except ValueError as e:
            flash(str(e), "error")

    return render_template("auth/signin.html")


@auth_bp.route("/change-password", methods=["GET", "POST"])
@jwt_required()
def handle_change_password():
    if request.method == "POST":
        old_password = request.form.get("old_password")
        new_password = request.form.get("new_password")

        user_id = get_jwt_identity()
        user = User.query.get(user_id)

        try:
            change_user_password(user, old_password, new_password)
            flash("Password updated successfully!", "success")
            return redirect(url_for("auth.dashboard"))
        except ValueError as e:
            flash(str(e), "error")

    return render_template("auth/change_password.html")


@auth_bp.route("/dashboard")
@jwt_required()
def get_dashboard_user():
    user_id = get_jwt_identity()
    user = User.query.get(user_id)
    return render_template("dashboard.html", user=user)


@auth_bp.route("/logout")
def logout():
    session.clear()
    flash("Logged out successfully.", "success")
    return redirect(url_for("auth/auth.signin"))
