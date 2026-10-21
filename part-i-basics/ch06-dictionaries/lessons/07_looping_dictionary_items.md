## Looping Dictionary Items

Python offers several ways to loop over a dictionary. The `items()` method gives you a view of
its key-value pairs. Each pair comes back as a tuple:

* Key: `tuple[0]`
* Value: `tuple[1]`

```python
user = {
    "username": "efermi",
    "first": "enrico",
    "last": "fermi",
}
print(user.items())
```

Output:

```
dict_items([('username', 'efermi'), ('first', 'enrico'), ('last', 'fermi')])
```

The result is a `dict_items` object. It's a live view of the dictionary's pairs, and you can loop
over it, but it isn't a list.

---

### Looping with `items()`

The most straightforward way to loop over `items()` is to unpack each tuple into two variables:

```python
user = {
    "username": "efermi",
    "first": "enrico",
    "last": "fermi",
}
for key, value in user.items():
    print(f"Key:   {key}")
    print(f"Value: {value}\n")
```

Output:

```
Key:   username
Value: efermi

Key:   first
Value: enrico

Key:   last
Value: fermi
```

> **A note on names:** `key` and `value` are only names. Python doesn't care what you call the two
> variables, as long as there are two of them to match each tuple. Instead of `key, value`, you could
> just as easily write:
>
> ```python
> for tom, jerry in user.items():
>     print(f"{tom}: {jerry}")
> ```
>
> The loop runs the same way, and `tom` holds each key while `jerry` holds each value. The names
> are for the human reading the code, so choose ones that make sense to them.

We'll cover looping over just the keys and just the values in lessons 6.8 and 6.11.

---

### Using Meaningful Names

`key` and `value` are conventional names, but they aren't required. Often, a name that says what
the data is will make your code much easier to read.

```python
favorite_languages = {
    "jen": "python",
    "sarah": "c",
    "edward": "ruby",
    "phil": "python",
}
for name, language in favorite_languages.items():
    print(f"{name.title()}'s favorite language is {language.title()}.")
```

Output:

```
Jen's favorite language is Python.
Sarah's favorite language is C.
Edward's favorite language is Ruby.
Phil's favorite language is Python.
```

Here's the same loop with the generic names. It works, but it tells you less:

```python
for key, value in favorite_languages.items():
    print(f"{key.title()}'s favorite language is {value.title()}.")
```

Output:

```
Jen's favorite language is Python.
Sarah's favorite language is C.
Edward's favorite language is Ruby.
Phil's favorite language is Python.
```

---

