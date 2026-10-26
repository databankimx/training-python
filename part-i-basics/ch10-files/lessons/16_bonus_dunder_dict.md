## Bonus Lesson: Classes and the `__dict__` Property

We previously discussed the various "magic" methods and properties provided in
Python. Now that we've covered classes and using JSON files to store data between
executions, it's worth revisiting one specific attribute: `__dict__`.

Every instance of a class has a `__dict__` attribute. It holds a dictionary of the
names and values of that instance's attributes.

But why do we need it?

---

### Classes Cannot Be Serialized

Consider this simple class:

```python
class Thing:
    """Models some thing"""

    def __init__(self, size: str, color: str) -> None:
        """Initialize the class attributes"""
        self.size = size
        self.color = color
```

I might wish to write a program that creates an instance of `Thing` and then retains
it in a file so that I can reload it the next time the program is executed.

Storing information as JSON is a common way to do this, and it can be easily loaded
using the `json` library.

But look at what happens if we try to do this with a class instance:

> Extra Bonus: Note the use of the `indent` keyword argument on `json.dumps`
> (also available on `json.dump`), which formats the JSON for ease of reading
> indenting child members by the number of spaces specified.

```python
import json

my_thing = Thing("Large", "Blue")
print(json.dumps(my_thing, indent=4))
```

Output:

```
Traceback (most recent call last):
  File "...\16_bonus_dunder_dict.py", line 35, in <module>
    main()
  File "...\16_bonus_dunder_dict.py", line 21, in main
    print(json.dumps(my_thing, indent=4))
  ...
  -- SNIP --
  ...
TypeError: Object of type Thing is not JSON serializable
```

The code file has this line commented out, so the rest of the file can run.
Uncomment it to see the error.

The error means `json` can't convert a `Thing` object into JSON.

---

### `__dict__` to the Rescue!

The `json.dump()` and `json.dumps()` functions can serialize data such as
dictionaries, lists, strings, and numbers. A `Thing` isn't one of those, but its
`__dict__` is a dictionary. So we can serialize the attributes of the object, even
though we can't serialize the class instance itself:

```python
import json

my_thing = Thing("Large", "Blue")
print(json.dumps(my_thing.__dict__, indent=4))
```

Output:

```
{
    "size": "Large",
    "color": "Blue"
}
```

---

### Improving the Code

We can further refine this by using `__dict__` as a value in a more detailed
dictionary:

```python
import json

my_thing = Thing("Large", "Blue")
print(json.dumps(
    {
        "type": "Thing",
        "name": "my_thing",
        "attributes": my_thing.__dict__
    },
    indent=4
))
```

Output:

```
{
    "type": "Thing",
    "name": "my_thing",
    "attributes": {
        "size": "Large",
        "color": "Blue"
    }
}
```

The code file comments out this improved example, so only the `__dict__` example above
runs. Uncomment it to see the output for yourself.

---
