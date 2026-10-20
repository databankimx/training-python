"""Lesson 3.0"""

# Python Collection Examples

my_list = [1, 2, 3]
print(my_list[0])
my_list.append(4)
my_list[0] = 4
print(my_list)

my_tuple = (1, 2, 3, 1)
print(my_tuple[-1])
print(my_tuple)

my_set = {1, 2, 3}
my_set.add(4)
print(my_set)

my_dictionary = {
    "x": 1,
    "y": 2,
    "z": 3
}
print(my_dictionary["x"])
print(my_dictionary)
my_dictionary["a"] = 4
print(my_dictionary)

my_amalgam = ["a", 9, (1, 2, 3), {4, 5, 6}, {"x": 1, "y": 2}]
print(my_amalgam)
print(my_amalgam[4]["y"])
print(my_amalgam[2][-1])
