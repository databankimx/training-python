# Exercise 19-4: Protecting new_entry

## The exercise

Currently, a user can add a new entry to another user's learning log by entering a URL with the ID of a topic belonging to another user.
Prevent this attack by checking that the current user owns the entry's topic before saving the new entry.

## About this exercise

In the course project, this check is already in place. It was added in chapter 19, step 3, and the refactoring in exercise 19-3 moved it into
`check_topic_owner()`. This exercise page shows the check, and how to confirm it works.

The important part is that the check happens before anything is saved. If another user's topic is given in the address, the view raises a 404
page, and the entry is never created.

## The solution

In `learning_logs/views.py`, the `new_entry` view checks the owner straight after it loads the topic, before it looks at the form or saves
anything:

```python
@login_required
def new_entry(request, topic_id):
    """Add a new entry to one of the signed-in user's topics."""
    topic = get_object_or_404(Topic, id=topic_id)
    check_topic_owner(topic, request.user)

    if request.method != "POST":
        form = EntryForm()
    else:
        form = EntryForm(data=request.POST)
        if form.is_valid():
            new_entry = form.save(commit=False)
            new_entry.topic = topic
            new_entry.save()
            return redirect("learning_logs:topic", topic_id=topic.id)

    context = {"topic": topic, "form": form}
    return render(request, "learning_logs/new_entry.html", context)
```

Because the check comes first, a POST to another user's topic returns a 404 page before the form is read. Nothing is saved.

## Checking it

The tests in `learning_logs/tests.py` cover this in `AccessTests`. The test called `test_another_users_topic_cannot_get_a_new_entry` signs in one user,
then sends a POST to another user's topic, and checks two things: the response is a 404 page, and the note doesn't exist in the database.

To try it yourself, run the step 5 project's tests, or run only this test:

```pwsh
python manage.py test learning_logs.tests.AccessTests.test_another_users_topic_cannot_get_a_new_entry
```

You should see `Ran 1 test` and `OK`.

## Output

None. This exercise is about checking code that's already in place. The test result is the proof.

---
