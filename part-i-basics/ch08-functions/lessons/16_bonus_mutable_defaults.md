## Using Default Values with Mutable Types

One technique we've learned about is setting a default value for an 
argument so that we don't need to pass an object to the function.

This can result in unexpected behavior when the default  value is of a mutable type (like a list or dictionary).

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

On the surface, it looks like this function should work fine, and if we
run it only once, nothing unexpected occurs. But let's look at what happens when we run the function multiple times:

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

Each time we called the function it added another element instead of 
creating a new, empty list. That's not what we expected at all!

This occurs because, as a mutable type, the list in the default function
is only generated once in Python: when the function is processed into
memory, before it is ever called.

So, multiple calls are hitting that same list, which is why we see the
list getting longer with each call.

---

### Fixing the Problem

Generally speaking, the easiest approach to work around this behavior is
to avoid mutable default arguments entirely.

In our case, we need the empty list to exist without being passed, so to
avoid using a mutable default, we'll make the default value `None` and
then create the list in the function if the argument isn't passed.

```python
def my_good_function(my_arg: list[str]=None) -> list[str]:
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

Now we have the desired behavior.

---

### When is it OK to Use a Mutable Default?

Although not always desirable (as we saw above) the fact that a mutable
default argument is created only once and maintained throughout the
program's runtime is consistent, which makes it predictable.

Predictable behavior is generally useful in some use cases.

Let's consider this function to recursively compute a Fibonacci number
using a dictionary as a memo (to avoid unnecessary recursive calls).

```python
@counter
def fibonacci(n: int, memo: dict[int, int]={0: 0, 1: 1}) -> int:
    """Return the nth Fibonacci number (memoized algorithm)"""
    if n in memo:
        return memo[n]
    memo[n] = fibonacci(n - 1, memo) + fibonacci(n - 2, memo)
    return memo[n]
```

I'm using this decorator function to count the number of times the 
recursive function is called:

```python
def counter(func: callable) -> callable:
    """Counts the number of calls to the passed function"""
    def _counter(*args, **kwargs):
        _counter.calls += 1
        return func(*args, **kwargs)
    _counter.calls = 0
    return _counter
```

The first time we call this function, we'll make 79 recursive calls to
obtain the 40th Fibonacci number.

But the second time, the same request will only take 1 call, because the
memo was populated up through 40 the first time through. Since it does
not get replaced in the default value, we gain the advantage of the prior
values being already computed.

Essentially, this behavior causes the function to be more efficient the
more times you use it.

```python
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
