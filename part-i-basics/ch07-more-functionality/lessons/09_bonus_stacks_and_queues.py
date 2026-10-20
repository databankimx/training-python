"""Lesson 7.9"""

print("Chapter 7:")
print("Bonus Exercise 9 - Stacks and Queues")

my_stack = [1, 2, 3, 4, 5]
print(f"Stack: {my_stack}")
while my_stack:
    print(my_stack.pop(-1))

my_queue = [1, 2, 3, 4, 5]
print(f"\nQueue: {my_queue}")
while my_queue:
    print(my_queue.pop(0))

# This isn't a complete illustration of stacks and queues,
#   just of removal order
