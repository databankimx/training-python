"""
The Learning Log Flask application.

create_app builds the application. The app keeps its database connection and its session factory, so each request can
read and write rows. The command-line commands at the bottom are what the build (and you) use to set up the database.
"""

import json
import os
from datetime import datetime

import click
from flask import Flask, abort, redirect, render_template, request, session as flask_session, url_for
from sqlalchemy import func

from flask_log.accounts import accounts, current_user_id, login_required
from flask_log.database import Base, make_engine, make_session_factory
from flask_log.models import Entry, Topic, User

DEFAULT_DATABASE_URL = "sqlite:///learning_log.db"
DEFAULT_SECRET_KEY = "dev-only-secret-key-change-before-deploying"
MAX_TOPIC_LENGTH = 200


def create_app(config: dict | None = None) -> Flask:
    """Build the Learning Log app. Tests pass their own config, such as an in-memory database."""
    app = Flask(__name__)
    app.config["DATABASE_URL"] = os.environ.get("DATABASE_URL", DEFAULT_DATABASE_URL)
    # Flask signs each session with this key. A live site sets LL_SECRET_KEY, so the key isn't in the code.
    app.config["SECRET_KEY"] = os.environ.get("LL_SECRET_KEY", DEFAULT_SECRET_KEY)
    # Debug mode shows detailed errors. It's on locally, and a live site sets LL_DEBUG to 0.
    debug = os.environ.get("LL_DEBUG", "1") == "1"
    app.config["DEBUG"] = debug
    # Recorded here as well, because Flask's command-line tools reset app.debug from FLASK_DEBUG, not LL_DEBUG.
    app.config["DEBUG_SWITCH"] = debug
    # A secure cookie is sent only over HTTPS. Locally the site runs over plain HTTP, so it's off while debugging.
    app.config["SESSION_COOKIE_SECURE"] = not debug
    if config:
        app.config.update(config)

    engine = make_engine(app.config["DATABASE_URL"])
    app.extensions["engine"] = engine
    app.extensions["session_factory"] = make_session_factory(engine)
    app.register_blueprint(accounts)

    @app.context_processor
    def inject_current_user() -> dict:
        """Make the signed-in user's name available to every template, or None when nobody is signed in."""
        user_id = current_user_id()
        username = None
        if user_id is not None:
            with app.extensions["session_factory"]() as db:
                user = db.get(User, user_id)
                username = user.username if user is not None else None
        return {"current_username": username}

    @app.errorhandler(404)
    def page_not_found(error):
        """The friendly page for an address that doesn't exist. It's used in debug mode too, so it's seen while building."""
        return render_template("404.html"), 404

    @app.errorhandler(500)
    def server_error(error):
        """The friendly page for an unexpected error. Debug mode shows the traceback instead, so this runs when debug is off."""
        return render_template("500.html"), 500

    @app.route("/")
    def index() -> str:
        """The home page. It lists the public topics, which anyone can read."""
        with app.extensions["session_factory"]() as session:
            public_topics = (session.query(Topic)
                             .filter_by(public=True)
                             .order_by(Topic.date_added)
                             .all())
            return render_template("index.html", public_topics=public_topics)

    @app.route("/topics/")
    @login_required
    def topics() -> str:
        """The signed-in user's topics, in the order they were added. Other people's topics are never listed here."""
        with app.extensions["session_factory"]() as session:
            my_topics = (session.query(Topic)
                         .filter_by(owner_id=current_user_id())
                         .order_by(Topic.date_added)
                         .all())
            return render_template("topics.html", topics=my_topics)

    @app.route("/topics/<int:topic_id>/")
    def topic(topic_id: int) -> str:
        """A topic and its entries. Anyone can read a public topic. A private topic is for its owner only."""
        with app.extensions["session_factory"]() as session:
            topic_record = session.get(Topic, topic_id)
            if topic_record is None:
                abort(404)
            is_owner = current_user_id() == topic_record.owner_id
            if not topic_record.public and not is_owner:
                if current_user_id() is None:
                    # A visitor who isn't signed in is asked to log in, then returned to this page.
                    return redirect(url_for("accounts.login", next=request.path))
                # A signed-in user who isn't the owner gets the same 404 page as for a topic that doesn't exist.
                abort(404)
            return render_template("topic.html", topic=topic_record, is_owner=is_owner)

    @app.route("/topics/new/", methods=["GET", "POST"])
    @login_required
    def new_topic() -> str:
        """Show the form for a new topic. On a POST, check the name, then save it, public if the box was ticked."""
        error = None
        text = ""
        if request.method == "POST":
            text = request.form.get("text", "").strip()
            with app.extensions["session_factory"]() as session:
                error = topic_name_error(session, current_user_id(), text)
                if error is None:
                    is_public = request.form.get("public") == "on"
                    session.add(Topic(text=text, owner_id=current_user_id(), public=is_public))
                    session.commit()
                    return redirect(url_for("topics"))
        return render_template("new_topic.html", error=error, text=text)

    @app.route("/topics/<int:topic_id>/new_entry/", methods=["GET", "POST"])
    @login_required
    def new_entry(topic_id: int) -> str:
        """Show the form for a new entry under one of the user's topics. On a POST, check the text, then save it."""
        error = None
        text = ""
        with app.extensions["session_factory"]() as session:
            topic_record = session.get(Topic, topic_id)
            if topic_record is None or topic_record.owner_id != current_user_id():
                abort(404)
            if request.method == "POST":
                text = request.form.get("text", "").strip()
                error = entry_text_error(text)
                if error is None:
                    session.add(Entry(topic_id=topic_id, text=text))
                    session.commit()
                    return redirect(url_for("topic", topic_id=topic_id))
            return render_template("new_entry.html", topic=topic_record, error=error, text=text)

    @app.route("/entries/<int:entry_id>/edit/", methods=["GET", "POST"])
    @login_required
    def edit_entry(entry_id: int) -> str:
        """Show an entry's text in the form, if its topic is the user's. On a POST, check the new text, then save it."""
        error = None
        with app.extensions["session_factory"]() as session:
            entry_record = session.get(Entry, entry_id)
            if entry_record is None or entry_record.topic.owner_id != current_user_id():
                abort(404)
            text = entry_record.text
            if request.method == "POST":
                text = request.form.get("text", "").strip()
                error = entry_text_error(text)
                if error is None:
                    entry_record.text = text
                    session.commit()
                    return redirect(url_for("topic", topic_id=entry_record.topic_id))
            return render_template("edit_entry.html", entry=entry_record, error=error, text=text)

    @app.route("/entries/<int:entry_id>/delete/", methods=["GET", "POST"])
    @login_required
    def delete_entry(entry_id: int) -> str:
        """Ask for confirmation first. On a POST, delete the entry and go back to its topic. Only the topic's owner can do this."""
        with app.extensions["session_factory"]() as session:
            entry_record = session.get(Entry, entry_id)
            if entry_record is None or entry_record.topic.owner_id != current_user_id():
                abort(404)
            topic_id = entry_record.topic_id
            if request.method == "POST":
                session.delete(entry_record)
                session.commit()
                return redirect(url_for("topic", topic_id=topic_id))
            return render_template("delete_entry.html", entry=entry_record)

    register_commands(app)
    return app


def topic_name_error(session, owner_id: int, text: str) -> str | None:
    """Why a topic name isn't allowed, or None when it's fine. The check is per user, and capital letters don't count."""
    if not text:
        return "Please enter a topic name."
    if len(text) > MAX_TOPIC_LENGTH:
        return f"Topic names can be at most {MAX_TOPIC_LENGTH} characters."
    clash = (session.query(Topic)
             .filter(Topic.owner_id == owner_id, func.lower(Topic.text) == text.lower())
             .first())
    if clash is not None:
        return "You already have a topic with this name."
    return None


def entry_text_error(text: str) -> str | None:
    """Why an entry isn't allowed, or None when it's fine. An entry can't be blank."""
    if not text:
        return "Please write something for this entry."
    return None


def register_commands(app: Flask) -> None:
    """The commands the build and the learner run: init-db, create-admin, load-seed and check-settings."""

    @app.cli.command("init-db")
    def init_db() -> None:
        """Create every table the models describe. It's safe to run again: existing tables are left alone."""
        Base.metadata.create_all(app.extensions["engine"])
        print("Database ready.")

    @app.cli.command("create-admin")
    def create_admin() -> None:
        """Create the admin account from STUDENT_ADMIN_USERNAME and STUDENT_ADMIN_PASSWORD, if it doesn't exist yet."""
        username = os.environ.get("STUDENT_ADMIN_USERNAME")
        password = os.environ.get("STUDENT_ADMIN_PASSWORD")
        if not username or not password:
            print("No admin details were given, so no admin account was created.")
            return
        with app.extensions["session_factory"]() as session:
            if session.query(User).filter_by(username=username).first() is not None:
                print(f"The admin account {username} already exists.")
                return
            admin = User(username=username)
            admin.set_password(password)
            session.add(admin)
            session.commit()
        print(f"Admin account {username} created.")

    @app.cli.command("load-seed")
    @click.argument("path")
    def load_seed(path: str) -> None:
        """Load topics and entries from a JSON file. A row whose id already exists is skipped, so running it twice is harmless."""
        with open(path, encoding="utf-8") as seed_file:
            data = json.load(seed_file)

        added_topics = added_entries = 0
        with app.extensions["session_factory"]() as session:
            for row in data.get("topics", []):
                if session.get(Topic, row["id"]) is None:
                    session.add(Topic(id=row["id"], text=row["text"], owner_id=row["owner_id"],
                                      public=row.get("public", False),
                                      date_added=datetime.fromisoformat(row["date_added"])))
                    added_topics += 1
            for row in data.get("entries", []):
                if session.get(Entry, row["id"]) is None:
                    session.add(Entry(id=row["id"], topic_id=row["topic_id"], text=row["text"],
                                      date_added=datetime.fromisoformat(row["date_added"])))
                    added_entries += 1
            session.commit()
        print(f"Loaded {added_topics} topics and {added_entries} entries from {path}.")

    @app.cli.command("check-settings")
    def check_settings() -> None:
        """List anything that isn't ready for a live site. Nothing is changed; you fix the settings and run it again."""
        problems = []
        if app.config["SECRET_KEY"] == DEFAULT_SECRET_KEY:
            problems.append("LL_SECRET_KEY isn't set, so the default secret key is in use.")
        if app.config["DEBUG_SWITCH"]:
            problems.append("Debug mode is on. Set LL_DEBUG to 0 before the site goes live.")
        if not app.config["SESSION_COOKIE_SECURE"]:
            problems.append("The session cookie isn't marked secure, because debug mode is on.")
        if problems:
            for problem in problems:
                print(f"- {problem}")
        else:
            print("Settings look ready for a live site.")
