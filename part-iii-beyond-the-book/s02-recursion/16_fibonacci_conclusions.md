## Conclusions

We've looked at several different ways to compute Fibonacci numbers.

We've discovered that a direct translation of a formula (even if it is
natively recursive) is often not the best algorithm.

And we've explored non-recursive options.

---

### Can I See This in Action?

All of the functions described in the Fibonacci chapters are in this file:

<details>
<summary>Fibonacci Functions</summary>
<br>

In [fibonacci_functions.py](./fibonacci_functions.py)

```python
from count_calls import CountCalls

@CountCalls
def fibonacci_recursive(n: int) -> int:
    """Return the nth Fibonacci number (naive algorithm)"""
    if n in [0, 1]:
        return n
    return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)

@CountCalls
def fibonacci_recursive_memo(n: int, cache: dict[int, int]={0: 0, 1: 1}) -> int:
    """Return the nth Fibonacci number (memoized algorithm)"""
    if n in cache:
        return cache[n]
    cache[n] = fibonacci_recursive_memo(n - 1, cache) + fibonacci_recursive_memo(n - 2, cache)
    return cache[n]

@CountCalls
def fibonacci_iterative(n: int) -> int:
    """Return the nth Fibonacci number (iterative algorithm)"""
    values = [0, 1]
    for i in range(2, n + 1):
        values.append(values[i - 1] + values[i - 2])
    return values[-1]

@CountCalls
def fibonacci_formulaic(n):
    """Return the nth Fibonacci number approximation (formulaic algorithm)"""
    if n in [0, 1]:
        return n
    phi = (1 + 5 ** 0.5) / 2
    return int((phi ** n - (1 - phi) ** n) / (phi - (1 - phi)))
```

</details>
<br>

And this file provides a program you can use to calculate different
Fibonacci numbers in any of the algorithms.

<details>
<summary>Fibonacci Runner Program</summary>
<br>

In [fibonacci_tests.py](./fibonacci_tests.py)

```python
import fibonacci_functions as fib

def print_menu() -> None:
    """Display the menu of algorithm options"""
    print("\nEnter one of the following options:")
    print("[R]ecursive Algorithm")
    print("[M]emoized Recursive Algorithm")
    print("[I]terative Algorithm")
    print("[F]ormula-Based Algorithm")
    print("[Q]uit")

def main() -> None:
    options = ["r", "m", "i", "f", "q"]

    while True:
        n = -1
        print_menu()
        option = ""
        option = input("\n> ")[:1].lower()
        if option not in options:
            print("Please enter a valid value!")
            continue
        else:
            while n < 0 and option != "q":
                try:
                    n = int(input("Enter a non-negative integer:\n> "))
                except:
                    continue
        if option == "r":
            # Call naive recursive function
            print(f"\nF({n}) = {fib.fibonacci_recursive(n):,}")
            print(f"Recursive calculation required {fib.fibonacci_recursive.call_count:,} function calls.")
        elif option == "m":
            # Call recursive function with memoization
            print(f"\nF({n}) = {fib.fibonacci_recursive_memo(n):,}")
            print(f"Cached recursive calculation required {fib.fibonacci_recursive_memo.call_count:,} function calls.")
        elif option == "i":
            # Call iterative function
            print(f"\nF({n}) = {fib.fibonacci_iterative(n):,}")
            suffix = "s"
            if fib.fibonacci_iterative.call_count == 1:
                suffix = ""
            print(f"Iterative calculation required {fib.fibonacci_iterative.call_count:,} function call{suffix}.")
        elif option == "f":    
            # Call formulaic function
            print(f"\nF({n}) = {fib.fibonacci_formulaic(n):,}")
            suffix = "s"
            if fib.fibonacci_formulaic.call_count == 1:
                suffix = ""
            print(f"Formula-based calculation required {fib.fibonacci_formulaic.call_count:,} function call{suffix}.")
        else:
            break

if __name__ == "__main__":
    main()
```

</details>
<br>

Run the code, and you can test all the algorithms for yourself:

```pwsh
python .\01_recursion.py
```

---
