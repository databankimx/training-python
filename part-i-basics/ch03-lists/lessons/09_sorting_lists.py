"""Lesson 3.9"""

print("Chapter 3:")
print("Exercise 9 - Sorting Lists")

# Sorting in place (permanent)
my_list = [13, 7, 28, 3, 2, 17]
print(my_list)
my_list.sort()
print(my_list)

my_list = ["grape", "banana", "fig", "apple", "date"]
print(my_list)
my_list.sort()
print(my_list)

# Sorting a copy (the original is unchanged)
my_list = [13, 7, 28, 3, 2, 17]
my_sorted_list = sorted(my_list)
print(my_sorted_list)
print(my_list)

# Descending order with reverse=True
my_sorted_list = sorted(my_list, reverse=True)
print(my_sorted_list)
print(my_list)
my_list.sort(reverse=True)
print(my_list)

# Reversing in place (permanent)
my_list = [13, 7, 28, 3, 2, 17]
print(my_list)
my_list.reverse()
print(my_list)

# Reversing a copy (reversed() returns an iterator, so wrap it in list())
my_list = [13, 7, 28, 3, 2, 17]
my_reversed_list = reversed(my_list)
print(list(my_reversed_list))
print(my_list)

print(f"There are {len(my_list)} items in the list.")
