## Lambda Rules

Lambdas are extremely flexible, but there are rules for how they are
implemented, including the structure of their parameters/arguments.

---

### A Lambda Cannot Contain a Statement

Statements (including `return`, `pass`, `assert`, and `raise`) are not permitted in lambdas.

Attempting to include a statement in a lambda, like this...

```python
bad = lambda x: assert x == 2
print(bad(2))
```

... will result in a SyntaxError

Output:

```
  File "...\03_rules_arguments.py", line 1
    bad = lambda x: assert x == 2
                    ^^^^^^
SyntaxError: invalid syntax
```

> Side-note: Lambdas do not support type hints, so this would also result
> in a SyntaxError:
>
> ```python
> bad = lambda x: int : x + 1 -> int
> ```

---

### A Lambda Must Contain Exactly One Expression

The return portion of a lambda must be a single expression. It can be
arbitrarily complex though.

```python
even_odd = lambda x: x % 2 and "odd" or "even"
print(even_odd(2))
print(even_odd(3))
```

> Note: In case the syntax is difficult to decipher in the lambda, I am
> taking advantage of the truthy value of a non-empty string and using
> an older version of the Python ternary operator. The lambda is 
> equivalent to:
>
> ```python
> even_odd = lambda x: "odd" if x % 2 else "even"
> ```

Output:

```
even
odd
```

---
