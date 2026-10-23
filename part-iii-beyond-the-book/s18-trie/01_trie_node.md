## The `TrieNode` Class

As a starting place, we need to define a class that represents a node in
the trie.

```python
class TrieNode:
    """Models a node in a trie"""

    def __init__(self, size: int = 26) -> None:
        """Initialize"""
        self.children: list[TrieNode | None] = [None] * size
        self.word_end: bool = False
```

Here:

* `children` is initialized as a list of empty slots, one for each character
  in the trie's character set.
    * I am using `None` to indicate that a child does not exist, but you
      can use any nothing-style value, like `0`, `False`, etc.
    * When populated, this will become a list of `TrieNode` objects
* `word_end` is set to `False` indicating that no words end at the current
  node.

---

There's not much else to say on this class. Being a data model, it does not
require any additional functionality.

---

### Trying It

The code for this example is in [01_trie_node.py](./01_trie_node.py):

```
Children: 26
First child: None
Word end: False
```

---
