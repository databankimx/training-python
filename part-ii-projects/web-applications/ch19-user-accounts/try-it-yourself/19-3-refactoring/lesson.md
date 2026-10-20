# Exercise 19-3: Refactoring

## The exercise

There are two places in `views.py` where we make sure the user associated with a topic matches the currently logged-in user. Put the code
for this check in a function called `check_topic_owner()`, and call this function where appropriate.

## About this exercise

Refactoring means changing how code is organized without changing what it does. The owner check is the same in several views, so moving it
into one function means a change to the rule only has to be made in one place.

The Learning Log has more than two of these checks by now. The topic page, the new entry page, the edit page, and the delete page each make the
same check, so the function is called in all four. The behavior stays the same, and the tests from chapter 19, step 5 cover it.

## Running this exercise

This is a code change in the Learning Log from chapter 19, step 5. There are no new files to run.

1. Open `learning_logs/views.py` in the step 5 project.
2. Add the function below, just above the first view that uses it. It needs `Http404`, which is already imported.
3. Replace each owner check with a call to the function.
4. Run the tests with `python manage.py test`. You should see `Ran 50 tests` and `OK`.

## The solution

The function raises the 404 page unless the topic belongs to the given user:

```python
def check_topic_owner(topic, owner) -> None:
    """Raise a 404 page unless the topic belongs to this user. This keeps each user's topics private."""
    if topic.owner != owner:
        raise Http404
```

The topic page then calls the function, instead of repeating the check:

```python
@login_required
def topic(request, topic_id):
    """Show one of the signed-in user's topics and all of its entries, newest first."""
    topic = get_object_or_404(Topic, id=topic_id)
    check_topic_owner(topic, request.user)
    entries = topic.entry_set.order_by("-date_added")
    context = {"topic": topic, "entries": entries}
    return render(request, "learning_logs/topic.html", context)
```

The new entry, edit entry and delete entry views change in the same way. For example, the start of `new_entry` becomes:

```python
@login_required
def new_entry(request, topic_id):
    """Add a new entry to one of the signed-in user's topics."""
    topic = get_object_or_404(Topic, id=topic_id)
    check_topic_owner(topic, request.user)
    --snip--
```

The edit and delete views work the same way. In those, the topic comes from the entry (`topic = entry.topic`), and the call is
`check_topic_owner(topic, request.user)`.

## Testing this exercise

Nothing about the behavior changes, so the existing tests are the check. Run `python manage.py test` and you should see `Ran 50 tests` and
`OK`. The tests that matter most here are the access tests in `AccessTests`, which check that another user gets a 404 page.

## Output

None. This exercise changes the code, not the pages. The tests show that it still works.
