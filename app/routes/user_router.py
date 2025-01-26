from flask import Blueprint, render_template, request, redirect, url_for, flash, session
from flask_jwt_extended import jwt_required, get_jwt_identity
from app.controllers.user_controller import handle_signup, handle_signin, handle_change_password, get_dashboard_user

user_blueprint = Blueprint("auth", __name__, template_folder="templates/auth")

# Route for Signup
@user_blueprint.route("/signup", methods=["GET", "POST"])
def signup():
    if request.method == "POST":
        name = request.form.get("name")
        email = request.form.get("email")
        password = request.form.get("password")

        try:
            handle_signup(name, email, password)
            flash("Signup successful! Please sign in.", "success")
            return redirect(url_for("auth.signin"))
        except ValueError as e:
            flash(str(e), "error")

    return render_template("auth/signup.html")

# Route for Signin
@user_blueprint.route("/signin", methods=["GET", "POST"])
def signin():
    if request.method == "POST":
        email = request.form.get("email")
        password = request.form.get("password")

        try:
            user, token = handle_signin(email, password)
            session["user_id"] = user.id
            session["jwt"] = token
            flash("Signin successful!", "success")
            return redirect(url_for("auth.dashboard"))
        except ValueError as e:
            flash(str(e), "error")

    return render_template("auth/signin.html")

# Route for Change Password
@user_blueprint.route("/change-password", methods=["GET", "POST"])
@jwt_required()
def change_password():
    if request.method == "POST":
        old_password = request.form.get("old_password")
        new_password = request.form.get("new_password")

        user_id = get_jwt_identity()
        
        try:
            handle_change_password(user_id, old_password, new_password)
            flash("Password updated successfully!", "success")
            return redirect(url_for("auth.dashboard"))
        except ValueError as e:
            flash(str(e), "error")

    return render_template("auth/change_password.html")

# Route for Dashboard
@user_blueprint.route("/dashboard")
@jwt_required()
def dashboard():
    user_id = get_jwt_identity()
    user = get_dashboard_user(user_id)
    return render_template("auth/dashboard.html", user=user)

# Route for Logout
@user_blueprint.route("/logout")
def logout():
    session.clear()
    flash("Logged out successfully.", "success")
    return redirect(url_for("auth.signin"))
