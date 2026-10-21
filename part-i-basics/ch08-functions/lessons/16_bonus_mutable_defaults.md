## Using Default Values with Mutable Types

One technique we've learned is setting a default value for an argument so that we don't need to pass an object to the function.

This can result in unexpected behavior when the default value is of a mutable type (like a list or dictionary).

The code for this lesson is in `16_bonus_mutable_defaults.py`. It turns off Pylint's `dangerous-default-value` warning on purpose, because this lesson is about the danger. The code file also has a `# NOSONAR` comment on `my_bad_function`. Those comments stay in the code file.

---

### Assigning a Mutable Default Value

Let's consider an example where we want to append an element to a list.

We can pass an existing list, but if we don't pass anything, we want the function to append to a new, empty list.

Consider this code:

```python
def my_bad_function(my_arg: list[str]=[]) -> list[str]:
    """Demonstrate the result of a default mutable argument"""
    print("Using an empty list as a default argument:")
    my_arg.append("new item")
    print(my_arg, "\n")
    return my_arg
```

On the surface, it looks like this function should work fine, and if we run it only once, nothing unexpected occurs. But let's look at what happens when we run the function multiple times:

```python
for _ in range(3):
    my_bad_function()
```

Output:

```
Using an empty list as a default argument:
['new item'] 

Using an empty list as a default argument:
['new item', 'new item'] 

Using an empty list as a default argument:
['new item', 'new item', 'new item'] 
```

Each time we called the function, it added another element instead of creating a new, empty list. That's not what we expected at all!

This happens because the default value is a list, and the default is evaluated once, when the `def` statement runs, before the function is ever called. Every call that uses the default gets that same list object.

So multiple calls are hitting the same list, which is why it gets longer with each call.

The code file runs these calls through a small helper, `run_repeat()`, which calls each function a set number of times and prints a header before each group:

```python
def run_repeat(repeat: int, functions: list[callable], *args, **kwargs) -> dict[str, callable]:
    """Execute a list of functions, repeating each a specified number of times"""
    ret = {}
    for function in functions:
        print(f"\nFunction: {function.__name__}")
        for i in range(repeat):
            ret[f"{function.__name__}_{i}"] = function(*args, **kwargs)
    return ret
```

Calling `run_repeat(3, [my_bad_function, my_good_function])` produces the same results as the loops above, with the `Function:` headers added. You'll see them when you run the file.

---

### Fixing the Problem

Generally speaking, the easiest approach is to avoid mutable default arguments entirely.

In our case, we need the empty list to exist without being passed. So to avoid a mutable default, we'll make the default value `None`, and then create the list in the function if the argument isn't passed.

```python
def my_good_function(my_arg: list[str] | None=None) -> list[str]:
    """Demonstrate the result of a default None argument"""
    print("Using `None` as a default argument:")
    if my_arg is None:
        my_arg = []
    my_arg.append("new item")
    print(my_arg, "\n")
    return my_arg
```

Then, as before, we'll call the function three times:

```python
for _ in range(3):
    my_good_function()
```

Output:

```
Using `None` as a default argument:
['new item']

Using `None` as a default argument:
['new item']

Using `None` as a default argument:
['new item']
```

Now we have the behavior we wanted.

---

### When Is It OK to Use a Mutable Default?

A mutable default is created once and kept for the life of the program. That's not always desirable, as we saw above, but it does make the behavior predictable. Sometimes a value that sticks around is exactly what you want.

Let's consider a function that recursively computes a Fibonacci number, using a dictionary as a memo so it doesn't repeat work.

```python
@counter
def fibonacci(n: int, memo: dict[int, int]={0: 0, 1: 1}) -> int:
    """Return the nth Fibonacci number (memoized algorithm)"""
    if n in memo:
        return memo[n]
    memo[n] = fibonacci(n - 1, memo) + fibonacci(n - 2, memo)
    return memo[n]
```

I'm using this decorator to count how many times the recursive function is called. A decorator has to exist before the function it decorates, so the code file defines `counter` first. If you're running these snippets by hand, define `counter` before `fibonacci`:

```python
def counter(func: callable) -> callable:
    """Counts the number of calls to the passed function"""
    def _counter(*args, **kwargs):
        _counter.calls += 1
        return func(*args, **kwargs)
    _counter.calls = 0
    return _counter
```

The first time we call this function for the 40th Fibonacci number, it makes 79 calls in total, including the first one. The memo fills up as it goes.

The second time, the same request takes only 1 call, because the memo already holds every value up through 40. The default value is never replaced, so the values computed the first time are still there.

Essentially, the function gets more efficient the more it's used, because the memo keeps filling up.

```python
n = 40
for _ in range(2):
    fibonacci.calls = 0
    print(f"F({n}) = {fibonacci(n)} : {fibonacci.calls} call(s)\n")
```

Output:

```
F(40) = 102334155 : 79 call(s)

F(40) = 102334155 : 1 call(s)
```

---

### Summary

- A mutable default is evaluated once, when the function is defined, and shared by every call.
- If you want a fresh object on each call, default to `None` and create the object inside the function.
- A shared mutable default can be useful when you want state to persist between calls, such as a memo.
