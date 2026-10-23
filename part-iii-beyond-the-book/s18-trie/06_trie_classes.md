## The Trie Classes

So far we have described the trie in general, and then added one method at a
time. This lesson puts the two classes together and explains all of their code.

A trie is a tree of nodes. Each node has a list of children, one for each
letter of the alphabet, and a flag that says whether a word ends at that node.
The root node is empty, and each path from the root spells out a prefix. Words
that share a prefix share the nodes for that prefix, which is what makes
searching by prefix fast.

The trie is built from two classes:

* `TrieNode` models one node in the tree.
* `Trie` owns the root node and provides the operations: insert, search,
  delete, and listing words.

The code for both classes is in the `s18-trie` folder, in
[trie_node.py](./trie_node.py) and [trie.py](./trie.py).

---

### The `TrieNode` Class

Here is the complete `TrieNode` class:

```python
"""Module to model a node in a trie"""

class TrieNode:
    """Models a node in a trie"""

    def __init__(self, size: int = 26) -> None:
        """Initialize"""
        self.children: list[TrieNode | None] = [None] * size
        self.word_end: bool = False
```

* `size` is the number of child slots. It defaults to 26, one for each letter
  of the English alphabet.
* `children` is a list of `size` entries, all `None` at first. Entry `i` holds
  the child node for the `i`-th letter, or `None` if there is no such child.
* `word_end` is `False` until a word ends at this node. It is what separates a
  word from a prefix: "an" is a prefix of "and", but only "and" has
  `word_end` set.

---

### The `Trie` Class

Here is the complete `Trie` class:

```python
"""Module to create and populate a trie"""

from pathlib import Path
from sm_utils import file_path, timer
from trie_node import TrieNode

class Trie:
    """Models a trie (alphabet only)"""

    def __init__(self, size: int = 26, base_char: str = "a") -> None:
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

    def prefix_exists(self, key: str, get_node: bool = False) -> bool | TrieNode | None:
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
            for i in range(self.size):
                if current_node.children[i] is not None:
                    count += 1
            if count > 1:
                last_branch_node = current_node
                last_branch_char = c
            current_node = current_node.children[ord(c) - self.offset]
        if not current_node.word_end:
            return False
        count = 0
        for i in range(self.size):
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

    def list_words(self, prefix: str | None = None) -> None:
        """List all words in the trie that start with the given prefix"""
        prefix = prefix or ""
        current_node = self.root if not prefix else self.prefix_exists(prefix, True)
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

    def load_words(self, file_name: str, folder: str | None = None) -> None:
        """Load words from a file into the trie"""
        words = Path(file_path(file_name, folder)).read_text(encoding="UTF-8").splitlines()
        for word in words:
            self.insert(word)
```

#### Members and Setup

* `size` and `offset` describe the alphabet. The `offset` is the code of the
  first letter, `ord("a")`, which is 97. The index for any letter is its code
  minus `offset`, so `a` is 0 and `z` is 25.
* `root` is the empty `TrieNode` that every path starts from.

#### Insert

`insert()` walks the word one letter at a time. For each letter it finds the
index, creates the child if it is missing, and moves into it. After the last
letter, it sets `word_end`. The `key.lower()` call makes the trie
case-insensitive, so "Any" and "any" are stored the same way.

#### Prefix and Search

`prefix_exists()` walks the same path as `insert()`, but it never creates
nodes. It returns `False` as soon as a letter is missing. It has an extra
argument, `get_node`. When it is `True`, the function returns the node at the
end of the path instead of `True`. `list_words()` uses this to start listing
from the right place, and the lessons use it to check `word_end` on a node.

`search()` also walks the path, but it returns `word_end` at the end. That is
the difference between a word and a prefix. It is wrapped in the `@timer`
decorator, which is why its calls print an execution time line first.

#### Delete

`delete()` walks the path and records the last node that has more than one
child. That node is the last point where the word could be cut off without
affecting another word. The method then handles three cases:

1. The word is not in the trie, because the path is missing or the last node
   is not a word end. It returns `False`.
2. The last node has children, so other words continue past it. Only its
   `word_end` flag is cleared.
3. The last node has no children. The chain of nodes after the last branch is
   removed, or, if there was no branch, the link from the root is removed.

The lesson on [deleting a word](./05_delete.md) explains the reasoning in more
detail.

#### Listing Words

`list_words()` finds the node for the prefix, with `prefix_exists(prefix, True)`,
and then passes it to `show_all_words()`. If the prefix is missing, it returns
without printing anything.

`show_all_words()` is recursive. It prints the current prefix if a word ends
there, and then visits each child in index order. Index order is alphabetical,
so the words come out sorted. This is the reason a trie makes sorted output
easy, a point the [intro](./00_intro.md) mentioned.

#### Loading Words

`load_words()` reads a file with one word per line, and inserts each word. It
uses `file_path()` from `sm_utils`, so the file is found relative to the
project, not the current directory.

---

### Trying It

Run the [interactive program](./main.py). Its first screen lists the words that
start with `appall`, which is `list_words()` at work. Then type a word to test
with `search()`, or type `-` followed by a word to test `delete()`:

```
List of words that start with 'appall':

appall
appalled
appalling
appallingly
appallingness
appallment
appalls
```

---

### Putting It Together

The [interactive program](./main.py) uses both classes. Its `initialize_trie()`
function creates a `Trie` and calls `load_words()` on the dictionary file. The
main loop then calls `list_words()` for the prefix `appall`, and calls `search()`
for each word the user enters. A word with a leading `-` is passed to
`delete()` instead.

---
