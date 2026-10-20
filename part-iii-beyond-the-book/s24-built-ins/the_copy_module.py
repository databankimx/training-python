"""The copy module: shallow copies and deep copies"""

from copy import copy, deepcopy

original = [1, 2, [3, 4]]

# copy() makes a new outer list, but the nested list is still shared
shallow = copy(original)

# deepcopy() also copies the nested list
deep = deepcopy(original)

print(f"Equal values: {shallow == original}")
print(f"Same list object: {shallow is original}")

# Change the nested list in the original
original[2].append(5)
print(f"Original: {original}")
print(f"Shallow:  {shallow}   (the nested list changed too)")
print(f"Deep:     {deep}      (unaffected)")
