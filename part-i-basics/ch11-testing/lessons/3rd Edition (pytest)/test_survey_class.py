"""Pytest tests for survey class"""

import pytest
from survey_class import AnonymousSurvey

@pytest.fixture
def language_survey():
    """A survey that will be available to all test functions."""
    question = "What language did you first learn to speak?"
    survey = AnonymousSurvey(question)
    return survey

# pylint: disable=redefined-outer-name
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
