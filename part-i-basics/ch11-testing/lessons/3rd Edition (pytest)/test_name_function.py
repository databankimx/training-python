"""Pytest tests for formatted name function"""

from name_function import formatted_name

def test_first_last_name():
    """Do names like 'Janis Joplin' work?"""
    name = formatted_name("janis", "joplin")
    assert name == "Janis Joplin"

def test_first_last_middle_name():
    """Do names like 'Wolfgang Amadeus Mozart' work?"""
    name = formatted_name("wolfgang", "mozart", "amadeus")
    assert name == "Wolfgang Amadeus Mozart"
