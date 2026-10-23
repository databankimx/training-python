"""Morse code tree node"""

# pylint: disable=too-few-public-methods
class Node:
    """Defines a Morse code tree node"""
    def __init__(self, value: str | None, left: "Node | None" = None,
                 right: "Node | None" = None) -> None:
        self.value = value
        self.left = left
        self.right = right
