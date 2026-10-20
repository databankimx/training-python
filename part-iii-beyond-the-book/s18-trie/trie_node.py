"""Module to model a node in a trie"""

from dataclasses import dataclass

@dataclass
class TrieNode:
    """Models a node in a trie"""

    def __init__(self, size: int=26) -> None:
        """Initialize"""
        self.children: list[TrieNode] = [None] * size
        self.word_end: bool = False
