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
def __init__(self) -> None:
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
def decode_code(self, code: str) -> str:
    """Follow a dot or dash path from the root to find one character"""
    node = self.tree
    for symbol in code:
        assert symbol in ".-"
        node = node.left if symbol == "." else node.right
        if node is None:
            return UNKNOWN
    # Internal nodes that are not the end of any code have no character
    return node.value if node.value is not None else UNKNOWN
```

If the path runs off the tree, or ends at a node that isn't a character, the
function returns the unknown-character symbol `□` instead of crashing.

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

### The Whole Tree

Here is the complete tree for every character in `CODES`. Each line shows the code
that leads to a node, followed by the character stored there. A node marked
`(no char)` is only a step on the way to other characters.

```
(root)
├── . E
│   ├── .. I
│   │   ├── ... S
│   │   │   ├── .... H
│   │   │   │   ├── ..... 5
│   │   │   │   └── ....- 4
│   │   │   └── ...- V
│   │   │       └── ...-- 3
│   │   └── ..- U
│   │       ├── ..-. F
│   │       └── ..-- (no char)
│   │           ├── ..--. (no char)
│   │           │   ├── ..--.. ?
│   │           │   └── ..--.- _
│   │           └── ..--- 2
│   └── .- A
│       ├── .-. R
│       │   ├── .-.. L
│       │   │   └── .-..- (no char)
│       │   │       └── .-..-. "
│       │   └── .-.- (no char)
│       │       └── .-.-. (no char)
│       │           └── .-.-.- .
│       └── .-- W
│           ├── .--. P
│           └── .--- J
│               └── .---- 1
│                   └── .----. '
└── - T
    ├── -. N
    │   ├── -.. D
    │   │   ├── -... B
    │   │   │   └── -.... 6
    │   │   │       └── -....- -
    │   │   └── -..- X
    │   │       └── -..-. /
    │   └── -.- K
    │       ├── -.-. C
    │       │   └── -.-.- (no char)
    │       │       ├── -.-.-. ;
    │       │       └── -.-.-- !
    │       └── -.-- Y
    │           └── -.--. (
    │               └── -.--.- )
    └── -- M
        ├── --. G
        │   ├── --.. Z
        │   │   ├── --... 7
        │   │   └── --..- (no char)
        │   │       └── --..-- ,
        │   └── --.- Q
        └── --- O
            ├── ---. (no char)
            │   └── ---.. 8
            │       └── ---... :
            └── ---- (no char)
                ├── ----. 9
                └── ----- 0
```

### Why the Tree Is Ordered This Way

Morse code was designed to be fast to send. The time to send a symbol depends on
its length, so the most common letters were given the shortest codes.

* **E and T come first.** They are the two most common letters in English, at
  roughly 13% and 9% of letters in ordinary text. Each gets a single signal: E is
  one dot, and T is one dash.
* **I, A, N, and M come next.** They are the next most common letters, and they
  take the two-symbol codes. The second level of the tree holds exactly these
  four letters.
* **Longer codes go to rarer letters.** The three-symbol codes go to letters such
  as S, U, R, W, D, K, G, and O. The four-symbol codes go to the least common
  letters, such as H, V, F, L, P, J, B, X, C, Y, Z, and Q.

So the depth of a node in the tree is roughly the rarity of its letter. Reading
the tree from the top, the common letters are near the root.

The assignments are not perfectly optimal. Some were chosen for other reasons, and
modern letter counts show small differences. The principle still holds: short codes
are given to common letters.

> **Possibly apocryphal:** The story is that Alfred Vail, who worked on Morse's
> telegraph system, counted the letters in a printer's type case to decide which
> letters needed the shortest codes. The details of this story are not verified,
> so treat it as a popular account rather than a documented fact.

---
