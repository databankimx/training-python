"""Assignment 2.7"""

# Stripping Names: Use a variable to represent a person's name, include some
#                  whitespace characters ("\t" and "\n") at the beginning and
#                  end. Print the name once with whitespace, then print using
#                  lstrip(), rstrip(), and strip().

print("Try-it-Yourself:")
print("Assignment 2.7")

me = "\n\tScott McLean\t\n"
print(f"[{me}]\n")
print(f"[{me.lstrip()}]\n")
print(f"[{me.rstrip()}]\n")
print(f"[{me.strip()}]\n")
