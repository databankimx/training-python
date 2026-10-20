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

    @app.route("/")
    def index() -> str:
        """The home page. It extends the shared layout in base.html."""
        return render_template("index.html")

    @app.route("/topics/")
    @login_required
    def topics() -> str:
        """The signed-in user's topics, in the order they were added. Other people's topics are never listed."""
        with app.extensions["session_factory"]() as session:
            my_topics = (session.query(Topic)
                         .filter_by(owner_id=current_user_id())
                         .order_by(Topic.date_added)
                         .all())
            return render_template("topics.html", topics=my_topics)

    @app.route("/topics/<int:topic_id>/")
    @login_required
    def topic(topic_id: int) -> str:
        """One of the user's topics, with its entries, newest first. Anyone else's topic gives the 404 page."""
        with app.extensions["session_factory"]() as session:
            topic_record = session.get(Topic, topic_id)
            if topic_record is None or topic_record.owner_id != current_user_id():
                abort(404)
            return render_template("topic.html", topic=topic_record)

    @app.route("/topics/new/", methods=["GET", "POST"])
    @login_required
    def new_topic() -> str:
        """Show the form for a new topic. On a POST, check the name against the user's own topics, then save it."""
        error = None
        text = ""
        if request.method == "POST":
            text = request.form.get("text", "").strip()
            with app.extensions["session_factory"]() as session:
                error = topic_name_error(session, current_user_id(), text)
                if error is None:
                    session.add(Topic(text=text, owner_id=current_user_id()))
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
    """The commands the build and the learner run: init-db, create-admin and load-seed."""

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
                                      date_added=datetime.fromisoformat(row["date_added"])))
                    added_topics += 1
            for row in data.get("entries", []):
                if session.get(Entry, row["id"]) is None:
                    session.add(Entry(id=row["id"], topic_id=row["topic_id"], text=row["text"],
                                      date_added=datetime.fromisoformat(row["date_added"])))
                    added_entries += 1
            session.commit()
        print(f"Loaded {added_topics} topics and {added_entries} entries from {path}.")
