"""Common functions for algorithm tests"""

from pathlib import Path
from math import log2, ceil, factorial
from relative_paths import get_path

def file_to_list(file_name: str, folder: str=None) -> list[int]:
    """Read a space-delimited file into a list of integers"""
    numbers = []
    path = Path(get_path(file_name, folder))
    for line in path.read_text(encoding="utf-8").splitlines():
        numbers += [int(n) for n in line.split()]
    return numbers

def list_to_file(array: list[int], file_name: str, folder: str=None) -> None:
    """Write a list of integers a space-delimited file"""
    path = Path(get_path(file_name, folder))
    path.write_text(" ".join(str(n) for n in array), encoding="utf-8")

def is_sorted(array: list[int]) -> bool:
    """Verify that all values in the array are in the sorted order"""
    for i in range(1, len(array)):
        if array[i] < array[i - 1]:
            return False
    return True

def complexities(n: int) -> dict[dict[str, any]]:
    """Calculate predicted operations by complexity"""
    return {
        "fac": {
            "name": "factorial",
            "big_o": "n!",
            "count": factorial(n)
        },
        "exp": {
            "name": "exponential",
            "big_o": "2ⁿ",
            "count": 2 ** n
        },
        "n_squared": {
            "name": "quadratic (polynomial)",
            "big_o": "n²",
            "count": n ** 2
        },
        "n_log_n": {
            "name": "loglinear",
            "big_o": "n log n",
            "count": int(ceil(n * log2(n)))
        },
        "n": {
            "name": "linear",
            "big_o": "n",
            "count": n
        },
        "log_n": {
            "name": "logarithmic",
            "big_o": "log n",
            "count": int(ceil(log2(n)))
        },
        "const": {
            "name": "constant",
            "big_o": "const",
            "count": 1
        }
    }

# pylint: disable=too-many-branches
def efficiency_report(algorithm: str, size: int, count: int) -> None:
    """Print out a report of the Big-O efficiency of the algorithm"""
    print(f"\n{algorithm} performed {count:,}", end=" ")

    if "search" in algorithm.lower():
        print(f"comparisons to search {size:,} numbers.\n")
    else:
        print(f"operations to sort {size:,} numbers\n")

    big_o = complexities(size)

    o = big_o["const"]
    if count > big_o["exp"]["count"] * 2:
        o = big_o["fac"]
    elif count > big_o["n_squared"]["count"] * 2:
        o = big_o["exp"]
    elif count > big_o["n_log_n"]["count"] * 2:
        o = big_o["n_squared"]
    elif count > big_o["n"]["count"] * 2:
        o = big_o["n_log_n"]
    elif count > big_o["log_n"]["count"] * 2:
        o = big_o["n"]
    elif count > 2:
        o = big_o["log_n"]

    print(f"Computed complexity: O({o['big_o']}) - {o['name']}\n")
    print("Approximate values for reference:")
    for item in big_o.values():
        try:
            s = str(item["count"])
            if len(s) > 20:
                val = f"{s[0]}.{s[1:3]} * 10^{len(s) - 2}"
            else:
                val = f"{item['count']:,}"
            print(f" • {item['big_o']: <8} = {val}")
        except ValueError:
            try:
                print(f" • {item['big_o']: <8} = {item['count']:.2E}")
            except OverflowError:
                print(f" • {item['big_o']: <8} = Value omitted - too large to calculate!")
    print()
