"""Lesson 11.2 (3rd Edition)"""

from survey_class import AnonymousSurvey

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

def main() -> None:
    """Main process"""
    language_survey()

if __name__ == "__main__":
    main()
