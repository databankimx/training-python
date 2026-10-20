"""Lesson 8.14"""

from statistics import mean
import random
import rounding_functions as rf
from sm_utils import clear_terminal, pause

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

# See rounding_functions.py for the definition of the truncate() function
print("Truncating:")
print("truncate(pi, 2) = ", rf.truncate(pi, 2))
print("truncate(pi) = ", rf.truncate(pi))
print(f"truncate({x}) = ", rf.truncate(x))
print(f"truncate({y}) = ", rf.truncate(y))

pause()
clear_terminal()

# See rounding_functions.py for the definition of the round_up() function
print("Rounding Up:")
print("round_up(pi, 2) = ", rf.round_up(pi, 2))
print("round_up(pi) = ", rf.round_up(pi))
print(f"round_up({x}) = ", rf.round_up(x))
print(f"round_up({y}) = ", rf.round_up(y))

pause()
clear_terminal()

# See rounding_functions.py for the definition of the round_down() function
print("Rounding Down:")
print("round_down(pi, 2) = ", rf.round_down(pi, 2))
print("round_down(pi) = ", rf.round_down(pi))
print(f"round_down({x}) = ", rf.round_down(x))
print(f"round_down({y}) = ", rf.round_down(y))

pause()
clear_terminal()

# See rounding_functions.py for the definition of the round_half_up() function
print("Rounding Half Up:")
print("round_half_up(pi, 2) = ", rf.round_half_up(pi, 2))
print("round_half_up(pi) = ", rf.round_half_up(pi))
print(f"round_half_up({x}) = ", rf.round_half_up(x))
print(f"round_half_up({y}) = ", rf.round_half_up(y))

pause()
clear_terminal()

# See rounding_functions.py for the definition of the round_half_down() function
print("Rounding Half Down:")
print("round_half_down(pi, 2) = ", rf.round_half_down(pi, 2))
print("round_half_down(pi) = ", rf.round_half_down(pi))
print(f"round_half_down({x}) = ", rf.round_half_down(x))
print(f"round_half_down({y}) = ", rf.round_half_down(y))

pause()
clear_terminal()

# See rounding_functions.py for the definition of the round_half_away_from_zero() function
print("Rounding Half away from Zero:")
print("round_half_away_from_zero(pi, 2) = ", rf.round_half_away_from_zero(pi, 2))
print("round_half_away_from_zero(pi) = ", rf.round_half_away_from_zero(pi))
print(f"round_half_away_from_zero({x}) = ", rf.round_half_away_from_zero(x))
print(f"round_half_away_from_zero({y}) = ", rf.round_half_away_from_zero(y))
print(f"round_half_away_from_zero(-{x}) = ", rf.round_half_away_from_zero(-x))
print(f"round_half_away_from_zero(-{y}) = ", rf.round_half_away_from_zero(-y))

pause()
clear_terminal()

# See rounding_functions.py for the definition of the round_half_away_from_zero() function
print("Rounding Half toward Zero:")
print("round_half_toward_zero(pi, 2) = ", rf.round_half_toward_zero(pi, 2))
print("round_half_toward_zero(pi) = ", rf.round_half_toward_zero(pi))
print(f"round_half_toward_zero({x}) = ", rf.round_half_toward_zero(x))
print(f"round_half_toward_zero({y}) = ", rf.round_half_toward_zero(y))
print(f"round_half_toward_zero(-{x}) = ", rf.round_half_toward_zero(-x))
print(f"round_half_toward_zero(-{y}) = ", rf.round_half_toward_zero(-y))

pause()
clear_terminal()

# See rounding_functions.py for the definition of the round_half_to_even() function
print("Rounding Half to Even:")
print("round_half_to_even(pi, 2) = ", rf.round_half_to_even(pi, 2))
print("round_half_to_even(pi) = ", rf.round_half_to_even(pi))
print(f"round_half_to_even({x}) = ", rf.round_half_to_even(x))
print(f"round_half_to_even({y}) = ", rf.round_half_to_even(y))

pause()
clear_terminal()

# Let's create some data to observe
# data = [random.uniform(-1.0, 1.01) for _ in range(1_000_000)]
data = [i + j / 10 for i in range(10) for j in range(10)]
d = 0

print("** Rounding Bias Examples **")
print("----------------------------")
print("Computed Average:          ", rf.average(data))
print("Statistical Mean:          ", mean(data))
print("Rounded Mean:              ", rf.average([round(x, d) for x in data]))
print("Truncated Mean:            ", rf.average([rf.truncate(x, d) for x in data]))
print("Round Up Mean:             ", rf.average([rf.round_up(x, d) for x in data]))
print("Round Down Mean:           ", rf.average([rf.round_down(x, d) for x in data]))
print("Round Half Up Mean:        ", rf.average([rf.round_half_up(x, d) for x in data]))
print("Round Half Down Mean:      ", rf.average([rf.round_half_down(x, d) for x in data]))
print("Round Away from Zero Mean: ", rf.average([rf.round_half_away_from_zero(x, d) for x in data]))
print("Round Toward Zero Mean:    ", rf.average([rf.round_half_toward_zero(x, d) for x in data]))
print("Round Half to Even Mean:   ", rf.average([rf.round_half_to_even(x, d) for x in data]))
