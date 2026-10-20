"""Decorator examples"""

import timeit
from datetime import datetime, timezone

DEBUG = True

def logger(func: callable) -> callable:
    """Provides a logger to execute each time a function is called"""

    def _logger(*args, **kwargs) -> callable:
        """Log function call when executing"""
        if not DEBUG:
            return func
        called_at = datetime.now(timezone.utc).astimezone().strftime(
            "on %Y-%m-%d at %H:%M:%S GMT%z (%Z)")
        to_execute = func(*args, **kwargs)
        print(f"Function {func.__name__} executed {called_at}")
        return to_execute

    return _logger

def timer(func: callable) -> callable:
    """Time the execution of a decorated function"""

    def _timer(*args, **kwargs):
        """Write out elapsed time of function execution"""
        start = timeit.default_timer()
        res = func(*args, **kwargs)
        end = timeit.default_timer()
        delta = end - start

        if delta > 60:
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

def smart_divide(func: callable) -> callable:
    """Decorator to protect against division by zero"""
    def inner(a: int, b: int) -> callable|None:
        """Execute function only if not dividing by zero"""
        print(f"I am going to divide {a} by {b}")
        if b == 0:
            print("Whoops! cannot divide by zero")
            return None
        return func(a, b)
    return inner

@smart_divide
def divide(a: int|float, b: int|float) -> float:
    """Perform division (protected by decorator)"""
    return a / b
