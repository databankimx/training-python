"""
The Learning Log's tables, written as Python classes.

Each class is a table. Each attribute with mapped_column is a column. A topic has many entries, and an entry belongs to one topic.
A user has a username and a password hash. The password itself is never stored.
"""

from datetime import datetime

from sqlalchemy import DateTime, ForeignKey, String, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship
from werkzeug.security import check_password_hash, generate_password_hash

from flask_log.database import Base


class User(Base):
    """A person who can sign in to the Learning Log."""

    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str] = mapped_column(String(50), unique=True)
    password_hash: Mapped[str] = mapped_column(String(255))

    def set_password(self, password: str) -> None:
        """Store a scrambled form of the password. The password itself is never kept."""
        self.password_hash = generate_password_hash(password)

    def check_password(self, password: str) -> bool:
        """True when the password matches the stored hash."""
        return check_password_hash(self.password_hash, password)


class Topic(Base):
    """A topic the learner is studying, such as Chess."""

    __tablename__ = "topics"

    id: Mapped[int] = mapped_column(primary_key=True)
    text: Mapped[str] = mapped_column(String(200))
    date_added: Mapped[datetime] = mapped_column(DateTime, default=datetime.now)

    entries: Mapped[list["Entry"]] = relationship(back_populates="topic", order_by="Entry.date_added.desc()")

    def __repr__(self) -> str:
        """Show the topic's text, which is handy when debugging."""
        return self.text


class Entry(Base):
    """Something specific the learner has learned about a topic."""

    __tablename__ = "entries"

    id: Mapped[int] = mapped_column(primary_key=True)
    topic_id: Mapped[int] = mapped_column(ForeignKey("topics.id"))
    text: Mapped[str] = mapped_column(Text)
    date_added: Mapped[datetime] = mapped_column(DateTime, default=datetime.now)

    topic: Mapped[Topic] = relationship(back_populates="entries")

    def __repr__(self) -> str:
        """Show the first 50 characters of the entry, like the Django version."""
        return f"{self.text[:50]}..." if len(self.text) > 50 else self.text
