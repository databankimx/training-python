## Using the Modulo Operator

The modulo operator `%` is a new arithmetic operation for many people, and it's one of the most
useful tools in programming.

You'll find uses for it everywhere, from checking whether a number is even to scheduling things
that repeat.

The modulo operator returns the remainder left over after dividing one number, the dividend, by
another, the modulus. Its syntax is:

```python
var = number % modulus
```

---

### Modulo as Remainder

Here's the remainder of integer division, for several numbers:

```python
numbers = [4, 5, 6, 7]
for number in numbers:
    print(f"{number} % 3 = {number % 3}")
```

Output:

```
4 % 3 = 1
5 % 3 = 2
6 % 3 = 0
7 % 3 = 1
```

---

### Identifying Multiples

A common use of modulo is to check whether one number is a multiple of another. For any integers `m`
and `n`, you can write the rule like this:

```python
# For any integers, m and n
if n % m == 0:
    # then n is a multiple of m
```

Since zero is a *falsy* value, you can also write it like this:

```python
# For any integers, m and n
if not n % m:
    # then n is a multiple of m
```

One example is telling even numbers from odd ones. Any multiple of 2 is even, so:

```python
number = int(input("\nEnter a number, and I will tell you if it is even or odd:\n> "))
if number % 2 == 0:
    condition = "even"
else:
    condition = "odd"
print(f"The number {number} is {condition}.")
```

User Prompt:

```
Enter a number, and I will tell you if it is even or odd:
> _
```

Let's assume the user types `7` + `<ENTER>`.

Output:

```
The number 7 is odd.
```

---

<span style="color:salmon">**Homework Alert!**</span>

### Checking for Prime Numbers

A fun exercise is to use modulo to determine whether a number is prime.

* Definition of a prime number:
  Any positive integer that has exactly two integer factors: 1 and itself
    * 0 is the additive identity and is neither positive nor negative,
      so it is not a prime number
    * 1 has only one factor (itself), so it's the unit, and it is neither prime nor composite
    * 2 is the smallest (and only even) prime number
    * Every positive integer greater than 1 that isn't prime is a composite number

Try to resist the urge to look at my examples until you've tried it yourself:

> Example file [primes.zip](./primes.zip) - password: *igiveup*

Think about efficiency as well as functionality.

---

