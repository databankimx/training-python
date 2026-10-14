## Using Inner Functions for Encapsulation

Sometimes you want to encapsulate some part of the functionality so it cannot 
be directly used by an external call.

This is another case where inner functions can come in handy.

---

### Limiting Execution of Encapsulated Function

Let's imagine a function that increments a number. We want to limit when that
function can do it's work. Let's say only when a number is lower than some
maximum value.

```python
def increment(n: int) -> int:
    """Increment an integer by 1"""
    max = 10
    if n >= max:
        return n
    def inner_increment():
        """Encapsulated function"""
        return n + 1
    return inner_increment()
```

---

#### A Working Test

This test does what is expected:

```python
n = 5
print(f"{n}++ = {increment(n)}")
```

Output:

```
5++ = 6
```

Since 5 < 10, the inner function was called, incrementing `n` to 6.

---

#### A Logically Blocked Test

This test does what is expected:

```python
n = 10
print(f"{n}++ = {increment(n)}")
```

Output:

```
10++ = 10
```

Since 10 is not less than 10, the inner function was not called, so `n` was
not incremented.

---

#### Blocking a Cheater

Let's say we know how the API was developed, and we're aware that the inner
function exists. We might try to call it directly, bypassing the logic that
blocked it from executing:

```python
n = 10
print(f"{n}++ = {inner_increment(n)}")
```

... but here is where encapsulating the inner function plays a role.

Output:

```
Traceback (most recent call last):
  File ...\03_encapsulation.py", line 24, in <module>
    main()
  File "...\03_encapsulation.py", line 16, in main
    print(f"{n}++ = {inner_increment(n)}")
                     ^^^^^^^^^^^^^^^
NameError: name 'inner_increment' is not defined
```

We get a name error, because `inner_increment()` only exists within the scope
of the `increment()` function, so it isn't accessible from an external call.

---
