"""Lesson 2.6"""

print("Chapter 2:")
print("Exercise 6 - Stripping Excess Whitespace")

# Often you need to strip whitespace (e.g. when retrieving fixed-length fields from a database)
favorite_language = "  Python  "

print(f"Strip Right: [{favorite_language.rstrip()}]")
print(f"Strip Left: [{favorite_language.lstrip()}]")
print(f"Strip Both: [{favorite_language.strip()}]")
