"""
The Learning Log's tables, written as Python classes.

Each class is a table. Each attribute with mapped_column is a column. A topic has many entries, and an entry belongs to one topic.
"""

from datetime import datetime

from sqlalchemy import DateTime, ForeignKey, String, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship

from flask_log.database import Base


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
