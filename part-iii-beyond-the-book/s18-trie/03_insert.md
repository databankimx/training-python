## Inserting a New Key

We have already reviewed the insert algorithm, but for review here is a
summary.

To insert a word (also called a *key*), starting from the *root* node:

1. Locate the child index for the first letter, and if it is not 
   populated, create a new node.
2. Move to the next node.
3. Repeat steps 1 and 2 until you reach the last letter
4. Mark the node for the final letter as a word end

```python
## -- SNIP --

    def insert(self, key: str) -> None:
        """Insert a string into the trie"""
        current_node = self.root
        for c in key.lower():
            index = ord(c) - self.offset # locate the child index
            if current_node.children[index] is None:
                current_node.children[index] = TrieNode(self.size)
            current_node = current_node.children[index]
        current_node.word_end = True
```

---

### Trying It

The code for this example is in [03_insert.py](./03_insert.py). It inserts
"and", then "ant", and checks the nodes along the way. The check uses
`prefix_exists()`, which we cover in the search lesson:

```
Node for 'a' exists: True
Node for 'an' exists: True
'and' is a word end: True
'ant' is a word end: True
'an' is a word end: False
```

---
