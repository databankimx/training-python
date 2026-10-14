"""Utility functions"""

import timeit

def timer(func: callable) -> callable:
    """Time the execution of a the decorated function"""
    def wrapped(*args, **kwargs):
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
    return wrapped

def ord_suffix(n: int) -> str:
    """Return the ordinal suffix for a given number"""
    suf = ["th", "st", "nd", "rd"]
    m = n % 10
    th = 10 < n < 20 or m > 3
    return suf[0] if th else suf[n]
