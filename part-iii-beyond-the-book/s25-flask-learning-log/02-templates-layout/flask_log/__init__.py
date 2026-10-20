"""
The Learning Log Flask application.

create_app builds the application. The app keeps its database connection and its session factory, so each request can
read and write rows. The command-line commands at the bottom are what the build (and you) use to set up the database.
"""

import os

import click
from flask import Flask, render_template

from flask_log.database import Base, make_engine, make_session_factory

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

    register_commands(app)
    return app


def register_commands(app: Flask) -> None:
    """The commands the build and the learner run: init-db, create-admin and load-seed."""

    @app.cli.command("init-db")
    def init_db() -> None:
        """Create every table the models describe. It's safe to run again: existing tables are left alone."""
        # Importing the models registers their tables with Base, so create_all knows about them.
        Base.metadata.create_all(app.extensions["engine"])
        print("Database ready.")

    @app.cli.command("create-admin")
    def create_admin() -> None:
        """Create the admin account from STUDENT_ADMIN_USERNAME and STUDENT_ADMIN_PASSWORD. Accounts arrive in a later step."""
        print("No accounts exist yet, so no admin account was created.")

    @app.cli.command("load-seed")
    @click.argument("path")
    def load_seed(path: str) -> None:
        """Load example rows from a JSON file. Seed data arrives in a later step."""
        print(f"Nothing to load from {path} yet.")
