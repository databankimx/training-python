"""The entry point for Flask: `flask --app flask_app run` starts the site, and the build uses the same file."""

from flask_log import create_app

app = create_app()
