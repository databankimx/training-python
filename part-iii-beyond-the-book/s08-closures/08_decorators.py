"""Decorators"""

import timeit

def debug(func: callable) -> callable:
    """Print out debug information when another function is called"""

    def _debug(*args, **kwargs):
        """Inner function to perform the work on the decorated function"""
        result = func(*args, **kwargs)
        print(f"{func.__name__}(args: {args}, kwargs: {kwargs}) -> {result}")
        return result

    return _debug

def timer(func: callable) -> callable:
    """Time the execution of a decorated function"""

    def _timer(*args, **kwargs):
        """Write out elapsed time of function execution"""
        start = timeit.default_timer()
        res = func(*args, **kwargs)
        end = timeit.default_timer()
        delta = end - start

        if delta > 60:\
            ex_time = f"{int(delta // 60)} m : {round(delta % 60, 4)} s"
        elif delta * 1_000_000 < 1:
            ex_time = f"{round(delta * 1_000_000_000, 4)} ns"
        elif delta * 1_000 < 1:
            ex_time = f"{round(delta * 1_000_000, 4)} µs"
        elif delta < 1:
            ex_time = f"{round(delta * 1000, 4)} ms"
        else:
            ex_time = f"{round(delta, 4)} s"
        print(f"Execution Time: {ex_time}")

        return res

    return _timer

def compute_sum(a: int, b: int) -> int:
    """Sum two numbers"""
    return a + b

@debug
def add(a: int, b: int) -> int:
    """Add two numbers"""
    return a + b

# pylint: disable=dangerous-default-value
def fibonacci(n: int, cache: dict[int, int]={0: 0, 1: 1}) -> int:
    """Return the nth Fibonacci number"""
    if n in cache:
        return cache[n]
    cache[n] = fibonacci(n - 1, cache) + fibonacci(n - 2, cache)
    return cache[n]

@timer
@debug
def run_fibonacci(n: int) -> int:
    """ Wrap the fibonacci call with a timer"""
    return fibonacci(n)

def main() -> None:
    """Run the program"""
    total = debug(compute_sum)
    total(1, 2)
    total(3, b=4)
    print()
    add(5, 6)
    add(7, b=8)
    print()
    n = 50
    print(f"F({n}) = {run_fibonacci(n):,}")

if __name__ == "__main__":
    main()
