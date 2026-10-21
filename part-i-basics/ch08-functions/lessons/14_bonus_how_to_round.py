"""Lesson 8.14"""

from statistics import mean
import random
from sm_utils import clear_terminal, pause
from rounding_functions import (
    truncate,
    round_up,
    round_down,
    round_half_up,
    round_half_down,
    round_half_away_from_zero,
    round_half_toward_zero,
    round_half_to_even,
    average,
)

random.seed(100)

print("Chapter 8:")
print("Exercise 14 - Bonus Lesson - Understanding Rounding")

pi = 3.14159265359
x = 1.5
y = 2.5

clear_terminal()
print("Using the built-in round() function:")
print("round(pi)", round(pi))
print("round(pi)", round(pi, 2))

pause()
clear_terminal()

print("Using the built-in round() function:")
print(f"round({x}) =", round(x))
print(f"round({y}) =", round(y))

pause()
clear_terminal()

print("Truncating:")
print("truncate(pi, 2) = ", truncate(pi, 2))
print("truncate(pi) = ", truncate(pi))
print(f"truncate({x}) = ", truncate(x))
print(f"truncate({y}) = ", truncate(y))

pause()
clear_terminal()

print("Rounding Up:")
print("round_up(pi, 2) = ", round_up(pi, 2))
print("round_up(pi) = ", round_up(pi))
print(f"round_up({x}) = ", round_up(x))
print(f"round_up({y}) = ", round_up(y))

pause()
clear_terminal()

print("Rounding Down:")
print("round_down(pi, 2) = ", round_down(pi, 2))
print("round_down(pi) = ", round_down(pi))
print(f"round_down({x}) = ", round_down(x))
print(f"round_down({y}) = ", round_down(y))

pause()
clear_terminal()

print("Rounding Half Up:")
print("round_half_up(pi, 2) = ", round_half_up(pi, 2))
print("round_half_up(pi) = ", round_half_up(pi))
print(f"round_half_up({x}) = ", round_half_up(x))
print(f"round_half_up({y}) = ", round_half_up(y))

pause()
clear_terminal()

print("Rounding Half Down:")
print("round_half_down(pi, 2) = ", round_half_down(pi, 2))
print("round_half_down(pi) = ", round_half_down(pi))
print(f"round_half_down({x}) = ", round_half_down(x))
print(f"round_half_down({y}) = ", round_half_down(y))

pause()
clear_terminal()

print("Rounding Half away from Zero:")
print("round_half_away_from_zero(pi, 2) = ", round_half_away_from_zero(pi, 2))
print("round_half_away_from_zero(pi) = ", round_half_away_from_zero(pi))
print(f"round_half_away_from_zero({x}) = ", round_half_away_from_zero(x))
print(f"round_half_away_from_zero({y}) = ", round_half_away_from_zero(y))
print(f"round_half_away_from_zero(-{x}) = ", round_half_away_from_zero(-x))
print(f"round_half_away_from_zero(-{y}) = ", round_half_away_from_zero(-y))

pause()
clear_terminal()

print("Rounding Half toward Zero:")
print("round_half_toward_zero(pi, 2) = ", round_half_toward_zero(pi, 2))
print("round_half_toward_zero(pi) = ", round_half_toward_zero(pi))
print(f"round_half_toward_zero({x}) = ", round_half_toward_zero(x))
print(f"round_half_toward_zero({y}) = ", round_half_toward_zero(y))
print(f"round_half_toward_zero(-{x}) = ", round_half_toward_zero(-x))
print(f"round_half_toward_zero(-{y}) = ", round_half_toward_zero(-y))

pause()
clear_terminal()

print("Rounding Half to Even:")
print("round_half_to_even(pi, 2) = ", round_half_to_even(pi, 2))
print("round_half_to_even(pi) = ", round_half_to_even(pi))
print(f"round_half_to_even({x}) = ", round_half_to_even(x))
print(f"round_half_to_even({y}) = ", round_half_to_even(y))

pause()
clear_terminal()

# Let's create some data to observe
# data = [random.uniform(-1.0, 1.01) for _ in range(1_000_000)]
data = [i + j / 10 for i in range(10) for j in range(10)]
d = 0

print("** Rounding Bias Examples **")
print("----------------------------")
print("Computed Average:          ", average(data))
print("Statistical Mean:          ", mean(data))
print("Rounded Mean:              ", average([round(x, d) for x in data]))
print("Truncated Mean:            ", average([truncate(x, d) for x in data]))
print("Round Up Mean:             ", average([round_up(x, d) for x in data]))
print("Round Down Mean:           ", average([round_down(x, d) for x in data]))
print("Round Half Up Mean:        ", average([round_half_up(x, d) for x in data]))
print("Round Half Down Mean:      ", average([round_half_down(x, d) for x in data]))
print("Round Away from Zero Mean: ", average([round_half_away_from_zero(x, d) for x in data]))
print("Round Toward Zero Mean:    ", average([round_half_toward_zero(x, d) for x in data]))
print("Round Half to Even Mean:   ", average([round_half_to_even(x, d) for x in data]))
