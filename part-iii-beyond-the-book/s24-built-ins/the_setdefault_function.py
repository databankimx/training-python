"""The setdefault function"""

from pprint import pprint

# The setdefault function will add a key/value pair to a dictionary
# if that key does not already exist

my_dict = {"name": "fido", "age": 3}
print(my_dict)

# This will add the default value like my_dict["animal"] = dog
my_dict.setdefault("animal", "dog")
print(my_dict)

# But, while my_dict["animal"] = cat would overwrite the value for key = animal, this will not
my_dict.setdefault("animal", "cat")
print(my_dict)

# While we're here, let's demonstrate pretty-print
pprint(my_dict, width=1)
