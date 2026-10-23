# Exercise 18-3: The Django API

## The exercise

When you write code to access the data in your project, you're writing a query. Skim through the documentation for querying your
data at https://docs.djangoproject.com/en/5.2/topics/db/queries/. Much of what you see will look new to you, but it will be very
useful as you start to work on your own projects.

## Running this exercise

Use the Django shell in the Learning Log project, to try the queries you read about.

1. Open the project with `python build_stage.py ch18 9`, or with the runner. The example data includes the Chess and Rock Climbing topics.
2. In the build folder, open the shell:

   ```pwsh
   cd build\ch18-getting-started-with-django-step-09
   python manage.py shell
   ```

3. Try these queries, pressing Enter after each one:

   ```python
   from learning_logs.models import Topic, Entry
   Topic.objects.all()
   Topic.objects.filter(text="Chess")
   Topic.objects.get(text="Chess")
   Topic.objects.order_by("text")
   Entry.objects.filter(topic__text="Chess")
   Entry.objects.count()
   ```

4. Read the documentation page, and try one query it describes that isn't listed above.

## What to look for

- **`all()`:** every row in the table.
- **`filter()`:** the rows that match a condition. It can return zero, one or many rows.
- **`get()`:** exactly one row. It raises an error if there's no match, or more than one.
- **`order_by()`:** sorts the rows. Put a minus sign before the field name to sort in reverse.
- **`topic__text`:** a double underscore follows a foreign key, so you can match on a field of the topic from an entry.

## Solution

There's no code to submit. Your check is that you can run each query above, and that you can explain what each one returns.

## Output

The shell's results for each query, such as the list of Chess and Rock Climbing topics.

---
