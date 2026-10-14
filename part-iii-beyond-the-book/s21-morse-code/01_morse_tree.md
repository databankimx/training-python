## Morse Code as a Binary Tree

Each Morse code is a path through a binary tree. Starting at the root, a dot
means "go left" and a dash means "go right". The character sits at the node
where the path ends.

```
            (root)
           /      \
         E          T
        / \        / \
       I   A      N   M
```

So `E` is a single dot, `T` is a single dash, `A` is a dot then a dash (`.-`),
and `N` is a dash then a dot (`-.`).

---

### Building the Tree

Rather than writing out each node by hand, `Morse.__init__()` walks each
character's code from the root, creating nodes as it goes:

```python
def __init__(self):
    """Build the tree by walking each character's code from the root"""
    self.tree = Node(None)
    for char, code in CODES.items():
        node = self.tree
        for symbol in code:
            attr = "left" if symbol == "." else "right"
            if getattr(node, attr) is None:
                setattr(node, attr, Node(None))
            node = getattr(node, attr)
        node.value = char
```

`CODES` is a single dictionary that holds the code for every character. The
tree is built from it, so you only have to edit the table to change the
encoder and decoder.

---

### Decoding

To decode a code, follow its symbols down the tree. The value at the end of
the path is the character:

```python
def decode_code(self, code):
    """Follow a dot or dash path from the root to find one character"""
    node = self.tree
    for symbol in code:
        node = node.left if symbol == "." else node.right
    return node.value
```

`decode()` splits the message into words and letters. Words are separated by
`_` (or by the `■` that the encoder writes for a space), and letters are
separated by spaces. The unknown-character symbol `□` is kept as-is.

---

### Encoding

Encoding goes the other way. The tree has no link back to its parent, so
`get_code()` searches the tree from the root. It builds the code on the way
back up: each step that goes left adds a dot to the front, and each step that
goes right adds a dash.

```python
if self.get_code(node.left, character, code):
    code.insert(0, ".")
```

Characters that are not in the table are replaced with `□`. A space becomes
`■`, so the words stay visibly separated.

---
