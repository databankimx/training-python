"""
The Learning Log Flask application.

create_app builds the application. The app keeps its database connection and its session factory, so each request can
read and write rows. The command-line commands at the bottom are what the build (and you) use to set up the database.
"""

import json
import os
from datetime import datetime

import click
from flask import Flask, render_template

from flask_log.database import Base, make_engine, make_session_factory
from flask_log.models import Entry, Topic

DEFAULT_DATABASE_URL = "sqlite:///learning_log.db"


def create_app(config: dict | None = None) -> Flask:
    """Build the Learning Log app. Tests pass their own config, such as an in-memory database."""
    app = Flask(__name__)
    app.config["DATABASE_URL"] = os.environ.get("DATABASE_URL", DEFAULT_DATABASE_URL)
    if config:
        app.config.update(config)

    engine = make_engine(app.config["DATABASE_URL"])
    app.extensions["engine"] = engine
    app.extensions["session_factory"] = make_session_factory(engine)

    @app.route("/")
    def index() -> str:
        """The home page. It extends the shared layout in base.html."""
        return render_template("index.html")

    @app.route("/topics/")
    def topics() -> str:
        """Every topic, in the order it was added. The session is closed once the rows are read."""
        with app.extensions["session_factory"]() as session:
            all_topics = session.query(Topic).order_by(Topic.date_added).all()
            return render_template("topics.html", topics=all_topics)

    register_commands(app)
    return app


def register_commands(app: Flask) -> None:
    """The commands the build and the learner run: init-db, create-admin and load-seed."""

    @app.cli.command("init-db")
    def init_db() -> None:
        """Create every table the models describe. It's safe to run again: existing tables are left alone."""
        Base.metadata.create_all(app.extensions["engine"])
        print("Database ready.")

    @app.cli.command("create-admin")
    def create_admin() -> None:
        """Create the admin account from STUDENT_ADMIN_USERNAME and STUDENT_ADMIN_PASSWORD. Accounts arrive in a later step."""
        print("No accounts exist yet, so no admin account was created.")

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
                    session.add(Topic(id=row["id"], text=row["text"],
                                      date_added=datetime.fromisoformat(row["date_added"])))
                    added_topics += 1
            for row in data.get("entries", []):
                if session.get(Entry, row["id"]) is None:
                    session.add(Entry(id=row["id"], topic_id=row["topic_id"], text=row["text"],
                                      date_added=datetime.fromisoformat(row["date_added"])))
                    added_entries += 1
            session.commit()
        print(f"Loaded {added_topics} topics and {added_entries} entries from {path}.")
