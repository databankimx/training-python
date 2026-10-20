"""
Accounts for the Learning Log: registering, logging in and logging out.

Flask keeps a session for each visitor. After a successful login, the session stores the user's id. Each request reads that id
to find out who is signed in. The session is stored in a signed cookie, so the id can't be changed without the app's secret key.
"""

import re

from flask import Blueprint, current_app, redirect, render_template, request, session as flask_session, url_for

from flask_log.models import User

accounts = Blueprint("accounts", __name__, url_prefix="/accounts")

# Usernames use lowercase letters and digits, from 3 to 30 characters. This matches the admin account the build creates.
USERNAME_RULE = re.compile(r"^[a-z0-9]{3,30}$")
MIN_PASSWORD_LENGTH = 8


def registration_error(session, username: str, password: str, confirm: str) -> str | None:
    """Why a new account isn't allowed, or None when it's fine."""
    if not USERNAME_RULE.match(username):
        return "Usernames use lowercase letters and numbers only, from 3 to 30 characters."
    if len(password) < MIN_PASSWORD_LENGTH:
        return f"Passwords need at least {MIN_PASSWORD_LENGTH} characters."
    if password != confirm:
        return "The two passwords don't match."
    if session.query(User).filter_by(username=username).first() is not None:
        return "That username is already taken."
    return None


@accounts.route("/register/", methods=["GET", "POST"])
def register() -> str:
    """Show the registration form. On a POST, check the details, create the account, and sign the new user in."""
    error = None
    username = ""
    if request.method == "POST":
        username = request.form.get("username", "").strip()
        password = request.form.get("password", "")
        confirm = request.form.get("confirm", "")
        with current_app.extensions["session_factory"]() as db:
            error = registration_error(db, username, password, confirm)
            if error is None:
                new_user = User(username=username)
                new_user.set_password(password)
                db.add(new_user)
                db.commit()
                flask_session["user_id"] = new_user.id
                return redirect(url_for("index"))
    return render_template("accounts/register.html", error=error, username=username)


@accounts.route("/login/", methods=["GET", "POST"])
def login() -> str:
    """Show the login form. On a POST, check the username and password, then sign the user in."""
    error = None
    username = ""
    if request.method == "POST":
        username = request.form.get("username", "").strip()
        password = request.form.get("password", "")
        with current_app.extensions["session_factory"]() as db:
            user = db.query(User).filter_by(username=username).first()
            if user is not None and user.check_password(password):
                flask_session["user_id"] = user.id
                return redirect(url_for("index"))
        # The same message for an unknown username and a wrong password, so the form doesn't reveal which usernames exist.
        error = "That username and password don't match."
    return render_template("accounts/login.html", error=error, username=username)


@accounts.route("/logout/", methods=["POST"])
def logout() -> str:
    """Sign the user out by clearing the session, then go to the home page."""
    flask_session.clear()
    return redirect(url_for("index"))
