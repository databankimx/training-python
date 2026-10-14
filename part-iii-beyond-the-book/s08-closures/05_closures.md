## Closures

Closures are a powerful but underused feature of many programming 
languages including Python.

A closure is a dynamically generated function created and returned by 
another function.

What makes a closure particularly powerful is that it captures the 
environment in which it was generated. This means that a closure has full 
access to locally scoped free variables* from its outer function even 
after that function has finished executing.

\* A *free* variable is any locally scoped variable that is not bound to
a parameter.

> Formal Definition:  
> A closure is a persistent local variable scope (the combination of a 
> function  bundled together (enclosed) with references to its surrounding 
> state (the lexical environment)).

---

### Defining a Closure

In Python, functions are first-class objects, which means that they can be
passed to and returned from functions.

When you return an inner function object, the interpreter packs the function 
along with its containing environment or closure.

The function object keeps a snapshot of all the variables and names defined 
in its containing scope.

To define a closure, you need to take three steps:

1. Create an inner function.
2. Reference variables from the enclosing function.
3. Return the inner function.

As an example, we will create a function that will generate closures that
raise a given value to a static power (defined by the outer function).

```python
def generate_power(exponent: int) -> callable:
    """Closure factory (creates a new closure each time it is called)"""
    def power(base: int) -> int:
        """Inner function will be created with the exponent known"""
        return base ** exponent
    return power
```

Notice how the inner `power()` function captures the `exponent` parameter from
the outer function.

---

### Instantiating and Using a Closure

We can create an instance of the closure and test it like this:

```python
squared = generate_power(2)
for n in range(1, 6):
    print(f"{n}² = {squared(n)}")
```

Output:

```
1² = 1
2² = 4
3² = 9
4² = 16
5² = 25
```

---

### Multiple Closures

The outer function can be used to generate multiple closures, and each will
retain the value for `exponent` that was in place when it was created.

```python
squared = generate_power(2)
cubed = generate_power(3)
for n in range(1, 6):
    print(f"{n}² = {cubed(n)}")
print()
for n in range(1, 6):
    print(f"{n}² = {squared(n)}")
```

Output:

```
1³ = 1
2³ = 8
3³ = 27
4³ = 64
5³ = 125

1² = 1
2² = 4
3² = 9
4² = 16
5² = 25
```

Generating the `cubed()` closure did not affect the existing `squared()` 
closure, even though it passed a different `exponent` value. This is because
`squared()` captured its value at the time it was run and enclosed that value.
It is not tied to the variable in the outer function but to the value that 
existed in the environment at the time.

---
