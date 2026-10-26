"""Lesson 2.7"""

print("Chapter 2:")
print("Exercise 7 - Removing Prefixes")

# Why removeprefix() exists: lstrip() removes any of the characters you list.
# Many editors underline the next line. That warning is intentional, because the argument
# looks like a prefix, but lstrip() treats it as a set of characters.
#pylint: disable=bad-str-strip-call
print("pepper".lstrip("pep"))        # r
print("pepper".removeprefix("pep"))  # per

no_starch_url = "https://nostarch.com"

# Remove the protocol from the beginning of the URL
print(no_starch_url.removeprefix("https://"))

# Note: removeprefix() does not modify the original string
print(no_starch_url)

# removesuffix() removes the given text from the end of a string
print("\nThe protocol used by the No Starch URL is " + \
      f"{no_starch_url.removesuffix('://nostarch.com')}")

# Note: removesuffix() does not modify the original string either
print(no_starch_url)

# Strip the extension from a filename
filename = "report.txt"
print(filename.removesuffix(".txt"))
