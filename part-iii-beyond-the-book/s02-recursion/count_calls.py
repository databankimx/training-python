"""Class to count the number of recursive calls to a function"""

from collections.abc import Callable
from typing import Any

class CountCalls:
    """Class to allow counting the times a recursive function is called"""

    def __init__(self, func: Callable) -> None:
        """Initialize"""
        self._count = 0
        self._func = func

    def __call__(self, *args: Any, **kwargs: Any) -> Any:
        """Magic method override to add to counter and execute function"""
        self._count += 1
        return self._func(*args, **kwargs)

    @property
    def call_count(self) -> int:
        """Number of times the recursive function has been called"""
        return self._count
