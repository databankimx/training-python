"""Lesson 11.2 (2nd Edition)"""

import unittest

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

def main():
    """Run the tests"""
    print("Chapter 11:\nExercise 2 - Testing a Class\n")
    process = input("Test [a]utomatically or [m]anually\n> ")
    if process[0].lower() == "a":
        unittest.main()
    else:
        language_survey()

if __name__ == "__main__":
    main()
