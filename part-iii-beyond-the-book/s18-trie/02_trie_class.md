## The `Trie` Class

Now we can create the object class for the `Trie`. 

As we covered in the [intro](./00_intro.md), a new trie only has one
really important member: the `root` `TrieNode`.

I have implemented the class to default to the 26-character set we're using
in the example but to allow for specifying a different character set size
in the `size` member.

```python
"""Module to create and populate a trie"""

from trie_node import TrieNode

class Trie:
    """Models a trie (alphabet only)"""

    def __init__(self, size: int=26, base_char: str="a") -> None:
        """Initialize"""
        self.size = size
        self.root = TrieNode(self.size)
        self.offset = ord(base_char)
```

---

### Members

* `size`: Number of cells in each node's list
* `root`: Root `TrieNode`
* `offset`: Lowest ASCII character value in our character set
    * Used for calculating index of a given character in the node lists
    * Assumes that the character set is a contiguous ASCII block
        * 97 through 122 inclusive for lower case a-z, e.g.
        * If we were to use a non-contiguous character set, some
          refactoring would be required.

---

### Adding Functionality

Next up, we'll add the necessary functionality to make this a useful data
structure.

* [Insert](./03_insert.md)
* [Search](./04_search.md)
* [Delete](./05_delete.md)

---
