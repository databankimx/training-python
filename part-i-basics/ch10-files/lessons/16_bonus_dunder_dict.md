## Bonus Lesson : Classes and the `__dict__` Property

We previously discussed the various "magic" methods and properties provided in
Python, but now that we've discussed classes and the use of JSON files to store data between executions, it's worth revisiting one specific property:
`__dict__`.

This property is exposed by default on every class in Python and resolves to a
dictionary containing the names and values of the class's attributes.

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

Typically, the efficient way to do this is to store information as JSON, which
can be easily loaded using the `json` library.

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
  File "...\16_bonus_dunder_dict.py", line 26, in <module>
    main()
  ...
  -- SNIP --
  ...
TypeError: Object of type Thing is not JSON serializable
```

Basically, this is telling us that we cannot create a JSON string representing 
the instance of `Thing`

---

### `__dict__` to the Rescue!

Since the `dump` and `dumps` methods expect a dictionary as an argument, we
can serialize the attributes of the object, even though we can't serialize the
class type itself:

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
        "name": "thing",
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

---

