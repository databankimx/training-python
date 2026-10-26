## Testing Classes

We can also use `pytest` to test classes. In order to accomplish this, we'll 
have to do a couple of extra tasks to give each test its own instance of the
class.

Let's imagine that we have the following class:

<details>
<summary>AnonymousSurvey Class</summary>

```python
class AnonymousSurvey:
    """Collect anonymous answers to a survey question."""
    
    def __init__(self, question: str) -> None:
        """Store a question, and prepare to store responses."""
        self.question = question
        self.responses = []
        
    def show_question(self) -> None:
        """Show the survey question."""
        print(self.question)
        
    def store_response(self, new_response: str) -> None:
        """Store a single response to the survey."""
        self.responses.append(new_response.lower())
        
    def show_results(self) -> None:
        """Show all the responses that have been given."""
        print("Survey results:")
        for response in set(self.responses):
            print(f"- {response.title()} ({self.responses.count(response)})")
```

</details>

---

### Setting Up the Test

We still construct a test case the same way we did for function testing, by
creating a `test_...` file.

However, now we will add a *fixture*: a function decorated with `@pytest.fixture`
that creates a resource for the tests to use. By default, pytest runs a fixture
before each test that asks for it, so each test gets a new instance of the class.

In this instance, we're creating an instance of our `AnonymousSurvey` class.

```python
import pytest
from survey_class import AnonymousSurvey

@pytest.fixture
def language_survey():
    """A survey that will be available to all test functions."""
    question = "What language did you first learn to speak?"
    survey = AnonymousSurvey(question)
    return survey
```

After that you add unit tests as normal, but the unit tests can use the
fixture by including it as an argument in the test case functions:

```python
def test_store_single_response(language_survey: AnonymousSurvey):
    """Test that a single response is stored properly."""
    language_survey.store_response("english")
    assert "english" in language_survey.responses

def test_store_three_responses(language_survey: AnonymousSurvey):
    """Test that three individual responses are stored properly."""
    responses = ['English', 'Spanish', 'Mandarin']
    for response in responses:
        language_survey.store_response(response.lower())

    for response in responses:
        assert response.lower() in language_survey.responses
```

> Note: the test file turns off a Pylint warning about the fixture name being
> redefined in the test functions. That comment stays in the test file.

### Testing

Run the tests for this class with:

```pwsh
pytest test_survey_class.py
```

Output:

```
==================== test session starts ====================
platform win32 -- Python 3.11.4, pytest-8.3.2, pluggy-1.5.0
rootdir: ...\3rd Edition (pytest)
collected 2 items

test_survey_class.py ..                                [100%]

===================== 2 passed in 0.02s =====================
```

Play around changing the expectations or the class behavior to see different
test results.

---

### Multiple Tests

When you run `pytest` without a file name, it looks in the folder for every file
whose name starts with `test_...`, and runs the tests in all of them.

With both of the tests from this chapter in place, we would have this output:

```
==================== test session starts ====================
platform win32 -- Python 3.11.4, pytest-8.3.2, pluggy-1.5.0
rootdir: ...\3rd Edition (pytest)
collected 4 items

test_name_function.py ..                               [ 50%]
test_survey_class.py ..                                [100%]

===================== 4 passed in 0.03s =====================
```

However, we can specify a given file. If we run this:

```pwsh
pytest test_survey_class.py
```

Only that file gets run:

```
==================== test session starts ====================
platform win32 -- Python 3.11.4, pytest-8.3.2, pluggy-1.5.0
rootdir: ...\3rd Edition (pytest)
collected 2 items

test_survey_class.py ..                                [100%]

===================== 2 passed in 0.01s =====================
```

---

### Verbose Logging

If we add the `-v` (verbose) switch to the command, `pytest` provides details
on passed tests as well as failed ones:

```pwsh
pytest -v test_survey_class.py
```

Output:

```
======================== test session starts ========================
platform win32 -- Python 3.11.4, pytest-8.3.2, pluggy-1.5.0
rootdir: ...\3rd Edition (pytest)
collected 2 items

test_survey_class.py::test_store_single_response PASSED        [ 50%]
test_survey_class.py::test_store_three_responses PASSED        [100%]

========================= 2 passed in 0.01s =========================
```

---

### Testing the Survey by Hand

The file `02_testing_classes.py` runs the survey from the keyboard. Enter
responses, then press `q` to see the results:

```python
def language_survey() -> None:
    """Manually Test Anonymous Surveys"""
    question = "What language did you first learn to speak?"
    my_survey = AnonymousSurvey(question)

    my_survey.show_question()
    print("Enter 'q' at any time to quit.\n")
    while True:
        response = input("Language: ")
        if response == "q":
            break
        my_survey.store_response(response)

    print("\nThank you to everyone who participated in the survey!")
    my_survey.show_results()
```

Run it from the terminal with `python 02_testing_classes.py`. A sample session
looks like this:

```
What language did you first learn to speak?
Enter 'q' at any time to quit.

Language: English
Language: Spanish
Language: english
Language: q

Thank you to everyone who participated in the survey!
Survey results:
- English (2)
- Spanish (1)
```

The order of the results can change from run to run, because a `set` doesn't
keep its items in order.

---
