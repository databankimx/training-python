## Testing Classes

We can also use `unittest` to test classes. In order to accomplish this, we'll 
have to do a couple of extra tasks to ensure that the tests use a shared 
instance of the class.

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

## Setting Up the Test

We still construct a test case the same way we did for function testing, by
creating a `TestCase` class.

However, now we will add a special function to the class: `setUp()`.

The `setUp()` method allows you to create your test case variables once and
use them globally in all your unit tests.

In this instance, we're creating an instance of our `AnonymousSurvey` class
and test data to populate its results.

After that you add unit tests as normal, but the unit tests can use the shared
attributes created in the `setUp()` function.

```python
class AnonymousSurveyTestCase(unittest.TestCase):
    """Tests for the class AnonymousSurvey"""
    
    def setUp(self):
        """
        Create a survey and a set of responses for use in all test methods.
        """
        question = "What language did you first learn to speak?"
        self.my_survey = AnonymousSurvey(question)
        self.responses = ["English", "Spanish", "Mandarin"]

    def test_store_single_response(self):
        """Test that a single response is stored properly."""
        self.my_survey.store_response(self.responses[0].lower())
        self.assertIn(self.responses[0].lower(), self.my_survey.responses)

    def test_store_three_responses(self):
        """Test that three individual responses are stored properly."""
        for response in self.responses:
            self.my_survey.store_response(response)
        for response in self.responses:
            self.assertIn(response.lower(), self.my_survey.responses)
```

## Testing

Add in a little code to run the tests:

```python
def main():
    unittest.main()
    
if __name__ == "__main__":
    main()
```

And we have a successful test run.

Output:

```
..
----------------------------------------------------------------------
Ran 2 tests in 0.000s

OK
```

Play around changing the expectations or the class behavior to see different
test results.

> Note: The script in this folder asks whether to run the tests automatically
> or manually. Choose `m` to run the `language_survey()` function instead, which
> lets you enter responses from the keyboard and then shows the results.

---

