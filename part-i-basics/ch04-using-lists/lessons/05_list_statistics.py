"""Lesson 4.5"""

import statistics

print("Chapter 4:")
print("Exercise 5 - List Statistics")

digits = list(range(10))
print(digits)
print(f"List Length:  {len(digits)}")
print(f"Minimum:      {min(digits)}")
print(f"Maximum:      {max(digits)}")
print(f"Sum:          {sum(digits)}")
print(f"Average:      {sum(digits) / len(digits)}")

tens = list(range(10, 101, 10))
print(tens)
print(f"Average:      {sum(tens) / len(tens)}")
print(f"Average:      {statistics.mean(tens)}")

avg = sum(tens) / len(tens)
mean = int(avg) if (avg * 10) % 10 == 0 else avg
print(f"Average:      {mean}")
