# Topics Model and Seed Data

## What this step does

The Learning Log needs somewhere to keep its topics and entries. This step describes them as two Python classes, `Topic` and `Entry`, and
SQLAlchemy turns them into tables. A topic has many entries, and each entry belongs to one topic.

The step also gives the app some example data. `load-seed` reads `seed.json`, which holds the Chess and Rock Climbing topics from the Django
chapters, with two chess entries. Running `load-seed` twice adds nothing new, because a row whose id already exists is skipped.

## If you're using the lesson runner

In the steps list, open **Part III · Beyond the Book**, then **S25 · Flask learning log**, then **Topics Model and Seed Data**, and click **Run**.
The build creates the tables, loads the seed data, and runs the nine tests. The browser opens at the home page, which looks as it did before, because
the topics page comes in the next step.

To see the data itself, open a second PowerShell window in the `web-applications` folder, and run these two lines. The first moves into the build folder, which is where `flask_app.py` lives, so the second one can find the app:

```pwsh
cd build\s25-flask-learning-log-step-03
..\..\.venv\Scripts\python.exe -m flask --app flask_app shell
```

At the `>>>` prompt, type these lines, pressing Enter after each one:

```python
s = app.extensions["session_factory"]()
from flask_log.models import Topic
[(t.text, len(t.entries)) for t in s.query(Topic).all()]
```

You should see `[('Chess', 2), ('Rock Climbing', 0)]`. Type `exit()` to leave the shell.

Press **Escape** to stop the server when you're done.

## For dummies: the quick version

1. In PowerShell, go to the `web-applications` folder.
2. Type `python build_stage.py s25 3 --run` and press Enter. You should see `Loaded 2 topics and 2 entries from seed.json.` and then `Ran 9 tests` and `OK`.
3. Press Ctrl+C to stop the server.

### Words you'll see

- **Model:** a Python class that describes a table. Each attribute is a column.
- **`mapped_column`:** SQLAlchemy's way to declare a column, with its type and any rules.
- **Relationship:** the link between two tables. `topic.entries` gives you the entries for a topic, and `entry.topic` gives you the topic for an entry.
- **Session:** SQLAlchemy's way to read and write rows. You add objects to it, then `commit` to save them.
- **Seed:** example data, loaded into the database so there's something to look at.

## The code

`flask_log/models.py` describes the two tables:

```python
class Topic(Base):
    __tablename__ = "topics"

    id: Mapped[int] = mapped_column(primary_key=True)
    text: Mapped[str] = mapped_column(String(200))
    date_added: Mapped[datetime] = mapped_column(DateTime, default=datetime.now)

    entries: Mapped[list["Entry"]] = relationship(back_populates="topic")
```

`Mapped[int]` gives the column its Python type, and `mapped_column` gives it its database rules. The `relationship` line doesn't create a
column. It tells SQLAlchemy how the two classes are linked.

`load-seed` opens a session, and adds each row that isn't already there:

```python
with app.extensions["session_factory"]() as session:
    for row in data.get("topics", []):
        if session.get(Topic, row["id"]) is None:
            session.add(Topic(id=row["id"], text=row["text"], ...))
    ...
    session.commit()
```

`session.get` looks a row up by its primary key, so the skip check is quick. `commit` saves everything added in the session, in one go.

The `__init__.py` file imports the models. That matters: `init-db` only creates tables for classes it knows about, and importing the models is how it
learns about them.

## Testing this step

The four new tests in `tests/test_models.py` check that a topic is saved and read back, that an entry belongs to its topic, that `load-seed` adds the
example data, and that running it twice adds nothing new. The build runs all nine tests, the five from earlier steps and these four.

## Output

No new page. The build output shows that the seed data loaded.

## Changed files

- `flask_log/models.py` (new): the Topic and Entry tables
- `flask_log/__init__.py`: imports the models, and `load-seed` loads the seed file
- `seed.json` (new): the example topics and entries
- `tests/test_models.py` (new): tests for the models and the seed command
