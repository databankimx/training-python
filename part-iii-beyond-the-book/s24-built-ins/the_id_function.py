"""The id function"""

# In Python, the id() function returns the memory location where an
# object is stored

# Here I am stashing a string in memory
loc_1 = id("Hello World")
print(loc_1)

# Here, we put the same string into a variable
# Because Python uses a table of all stored string values to minimize
# memory use, this is at the same address
my_string = "Hello World"
loc_2 = id(my_string)
print(loc_2)

# When we change the value, however, even though it's the same variable,
# the string is at a new address
my_string = "Hello World!"
loc_3 = id(my_string)
print(loc_3)
