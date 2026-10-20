"""
The database for Learning Log.

SQLAlchemy describes the tables as Python classes, and talks to the database through a connection string. The connection string
decides which database is used: SQLite by default, or SQL Server or MySQL when the learner provides one.
"""

from sqlalchemy import create_engine
from sqlalchemy.engine import Engine
from sqlalchemy.orm import DeclarativeBase, sessionmaker


class Base(DeclarativeBase):
    """The parent class of every table. Each model class inherits from it."""


def make_engine(url: str) -> Engine:
    """Connect to the database at this connection string."""
    return create_engine(url)


def make_session_factory(engine: Engine) -> sessionmaker:
    """A factory that makes a session, which is how the app reads and writes rows."""
    return sessionmaker(bind=engine)
