## Mutating the Closure State

One somewhat counterintuitive behavior of closures occurs when a mutable type
(like a list) exists in its lexical environment.

If the closure modified the mutable object, it remains modified the next time
the closure is called. Effectively, the closure becomes a mutable function.

---

### Example

Let's create a closure-generating function:

```python
def mean() -> callable:
    """Creates a mutable mean function that updates as numbers are added"""
    sample = []
    def inner_mean(n: int) -> float:
        sample.append(n)
        return sum(sample) / len(sample)
    return inner_mean
```

Although `sample` exists in the outer function, because it is a mutable type,
it is only initialized once. After that, on subsequent calls the elements
previously added to the list will still be there:

---

### Testing

Let's put this to the test:

```python
sample_mean = mean()
for i in range(1, 6):
    print(f"Stored {i}: Mean = {sample_mean(i)}")
```

Output:

```
Stored 1: Mean = 1.0
Stored 2: Mean = 1.5
Stored 3: Mean = 2.0
Stored 4: Mean = 2.5
Stored 5: Mean = 3.0
```

We can see that the value passed on each call was appended to the list.

This is powerful, but it illustrates the need to be aware of how mutable
objects behave, as accessing a modified closure can otherwise have unexpected 
results.

---
