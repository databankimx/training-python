"""Module to create and populate a trie"""

from pathlib import Path
from sm_utils import file_path, timer
from trie_node import TrieNode

class Trie:
    """Models a trie (alphabet only)"""

    def __init__(self, size: int=26, base_char: str="a") -> None:
        """Initialize"""
        self.size = size
        self.root = TrieNode(self.size)
        self.offset = ord(base_char)

    def insert(self, key: str) -> None:
        """Insert a string into the trie"""
        current_node = self.root
        for c in key.lower():
            index = ord(c) - self.offset
            if current_node.children[index] is None:
                current_node.children[index] = TrieNode(self.size)
            current_node = current_node.children[index]
        current_node.word_end = True

    def prefix_exists(self, key: str, get_node: bool=False) -> bool|TrieNode:
        """Check if prefix exists in the trie"""
        current_node = self.root
        for c in key.lower():
            if current_node.children[ord(c) - self.offset] is None:
                return None if get_node else False
            current_node = current_node.children[ord(c) - self.offset]
        return current_node if get_node else True

    @timer
    def search(self, key: str) -> bool:
        """Check if word exists in the trie"""
        current_node = self.root
        for c in key.lower():
            if current_node.children[ord(c) - self.offset] is None:
                return False
            current_node = current_node.children[ord(c) - self.offset]
        return current_node.word_end

    def delete(self, key: str) -> bool:
        """Remove word from trie"""
        current_node = self.root
        last_branch_node = None
        last_branch_char = "a"
        for c in key.lower():
            if current_node.children[ord(c) - self.offset] is None:
                return False
            count = 0
            for i in range(26):
                if current_node.children[i] is not None:
                    count += 1
            if count > 1:
                last_branch_node = current_node
                last_branch_char = c
            current_node = current_node.children[ord(c) - self.offset]
        count = 0
        for i in range(26):
            if current_node.children[i] is not None:
                count += 1
        if count > 0:
            current_node.word_end = False
            return True
        if last_branch_node is not None:
            last_branch_node.children[ord(last_branch_char) - self.offset] = None
            return True
        self.root.children[ord(key[0]) - self.offset] = None
        return True

    def list_words(self, prefix: str=None) -> None:
        """List all words in the trie that start with the given prefix"""
        current_node = self.root if prefix is None else self.prefix_exists(prefix, True)
        if current_node is None:
            return
        self.show_all_words(current_node, prefix)

    def show_all_words(self, current_node: TrieNode, prefix: str) -> None:
        """Recursive function to list all words in the trie"""
        if current_node.word_end:
            print(prefix)
        for i in range(self.size):
            node = current_node.children[i]
            if node is None:
                continue
            self.show_all_words(node, prefix + chr(i + self.offset))

    def load_words(self, file_name: str, folder: str = None) -> None:
        """Load words from a file into the trie"""
        words = Path(file_path(file_name, folder)).read_text(encoding="UTF-8").splitlines()
        for word in words:
            self.insert(word)
