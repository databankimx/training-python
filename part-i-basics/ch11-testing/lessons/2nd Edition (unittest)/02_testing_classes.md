## Testing Classes

We can also use `unittest` to test classes. In order to accomplish this, we'll 
have to do a couple of extra tasks to set up each test with a fresh instance
of the class.

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
creating a `TestCase` class.

However, now we will add a special function to the class: `setUp()`.

The `setUp()` method runs before every test method. Each test gets its own new
set of attributes, which it reaches through `self`, so the tests can't affect
each other's data.

In this instance, we're creating an instance of our `AnonymousSurvey` class
and test data to populate its results.

After that you add unit tests as normal, and the unit tests can use the
attributes created in the `setUp()` function.

```python
class AnonymousSurveyTestCase(unittest.TestCase):
    """Tests for the class AnonymousSurvey"""
    
    def setUp(self) -> None:
        """
        Create a survey and a set of responses for use in all test methods.
        """
        question = "What language did you first learn to speak?"
        self.my_survey = AnonymousSurvey(question)
        self.responses = ["English", "Spanish", "Mandarin"]

    def test_store_single_response(self) -> None:
        """Test that a single response is stored properly."""
        self.my_survey.store_response(self.responses[0].lower())
        self.assertIn(self.responses[0].lower(), self.my_survey.responses)

    def test_store_three_responses(self) -> None:
        """Test that three individual responses are stored properly."""
        for response in self.responses:
            self.my_survey.store_response(response)
        for response in self.responses:
            self.assertIn(response.lower(), self.my_survey.responses)
```

### Testing

Add in a little code to run the tests, or to run the survey by hand:

```python
def main():
    """Run the tests"""
    process = input("Test [a]utomatically or [m]anually\n> ")[:1].lower()
    if process == "a":
        unittest.main()
    else:
        language_survey()

if __name__ == "__main__":
    main()
```

Choosing `a` runs the unit tests, and we have a successful test run.

Output:

```
..
----------------------------------------------------------------------
Ran 2 tests in 0.000s

OK
```

Play around changing the expectations or the class behavior to see different
test results.

### Testing the Survey by Hand

Choosing `m` runs `language_survey()`. It lets you enter responses from the
keyboard, and then it shows the results:

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

> Note: The script in this lesson asks whether to run the tests automatically
> or manually. Choose `m` to run the `language_survey()` function instead, which
> lets you enter responses from the keyboard and then shows the results.

---
