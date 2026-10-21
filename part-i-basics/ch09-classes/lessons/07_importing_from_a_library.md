## Importing from Libraries

Notes:

* The Python Standard Library (PSL) is a set of modules included with every
  Python installation.
* We can import and use these ready-made modules.

Importing from a library module is no different than importing from one of your own modules:  
`from library_module import function_or_class`

There is also a large and diverse collection of community-created open-source
libraries that are not included in the PSL. You'll find them at:  
[The Python Package Index (PyPI) - https://pypi.org/](https://pypi.org/)

---

### Importing `random` from the Python Standard Library

One of the most common tasks you'll need in your programs is generating a
random number.

The PSL includes a module called `random`, which exposes a number of functions
for random number generation and other randomization functionality.

For our example, we'll import the following functions from `random`:

* `randint()`: Generates a random integer between two integers (inclusive)
* `choice()`: Randomly selects an item from a collection

```python
from random import randint, choice

dice = [randint(1, 6), randint(1, 6)]
print(f"You rolled {sum(dice)}\n")

players = ["charles", "martina", "michael", "florence", "eli"]
first_up = choice(players)
print(f"First Up: {first_up.title()}")
```

Output:

```
You rolled 7

First Up: Martina
```

Note: Because we're using randomization, your values may differ on each run.

The `random` module is fine for games, simulations, and other fun projects.
Don't use it for anything security-related, such as generating passwords or
tokens. Python's `secrets` module is built for that job.

---

### Importing from a PyPI Library

Because PyPI libraries aren't included in the PSL, you have to install them
first.

We'll install and use a PyPI library that I created as an example:  
[sm-utils](https://pypi.org/project/sm-utils/)

In the terminal (preferably with an active virtual environment), run the
following command:

```pwsh
py -m pip install sm_utils
```

Once a library is installed, you can import from it, just like you can a PSL
library or a local module.

```python
from sm_utils import pause

# Wait until user hits enter to proceed
pause()
print("Done...")
```

Output:

```
Press <ENTER> to continue...
```

... terminal sits in IO wait until the user presses `<ENTER>` then continues

```
Done...
```

---
