"""Lesson 4.5"""

import statistics

print("Chapter 4:")
print("Exercise 5 - List Statistics")

digits = list(range(0, 10))
print(digits)
print(f"List Length:  {len(digits)}")
print(f"Minimum:      {min(digits)}")
print(f"Maximum:      {max(digits)}")
print(f"Sum:          {sum(digits)}")
print(f"Average:      {sum(digits) / len(digits)}")

tens = list(range(10, 101, 10))
print(f"\n{tens}")
avg = sum(tens) / len(tens)
print(f"Average:      {avg}")
mean_avg = statistics.mean(tens)
print(f"Mean Average: {mean_avg}")

calc_avg = int(avg) if (avg * 10) % 10 == 0 else avg
print(f"Calc Average: {calc_avg}")
