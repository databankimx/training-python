"""Morse code tree node"""

# pylint: disable=too-few-public-methods
class Node:
    """Defines a Morse code tree node"""
    def __init__(self, value, left = None, right = None):
        self.value = value
        self.left = left
        self.right = right
