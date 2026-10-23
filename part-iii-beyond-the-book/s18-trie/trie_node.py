"""Module to model a node in a trie"""

#pylint: disable=too-few-public-methods
class TrieNode:
    """Models a node in a trie"""

    def __init__(self, size: int = 26) -> None:
        """Initialize"""
        self.children: list[TrieNode | None] = [None] * size
        self.word_end: bool = False
