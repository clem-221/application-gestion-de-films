from flask import Blueprint, render_template, request, redirect, url_for, session, flash
from app.services.UserServices import UserServices
from app.models.UserDAO import UserDAO

users_bp = Blueprint("users", __name__, template_folder="templates")

user_dao = UserDAO("app/movies.db")
user_service = UserServices(user_dao)


@users_bp.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        user = user_service.authenticate(username, password)
        if user:
            session["logged"] = True
            session["username"] = user.username
            session["user_id"] = user.id
            return redirect(url_for("index.index"))
        flash("Identifiants incorrects.")
    return render_template("login.html", metadata={"title": "Login", "pagename": "login"})


@users_bp.route("/signin", methods=["GET", "POST"])
def signin():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        firstname = request.form["firstname"]
        lastname = request.form["lastname"]
        student_id = request.form["student_id"]
        success, error = user_service.register(username, password, firstname, lastname, student_id)
        if success:
            return redirect(url_for("users.login"))
        flash(error)
    return render_template("signin.html", metadata={"title": "Inscription", "pagename": "signin"})

@users_bp.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("index.index"))


@users_bp.route("/profile")
def users():
    return render_template("users_view.html", metadata={"title": "Profile", "pagename": "profile"})