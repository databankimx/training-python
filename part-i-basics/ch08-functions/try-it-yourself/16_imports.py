"""Assignment 8.16"""

# Imports: Using a program you wrote that has one function in it,
#          store that function in a separate file. Import the function
#          into your main program file, and call the function using
#          each of these approaches:
# ----------------------------------------------------
#     • import module_name
#     • from module_name import function_name
#     • from module_name import function_name as fn
#     • import module_name as mn
#     • from module_name import *
# ----------------------------------------------------

import album
# pylint: disable=reimported
import album as a
from album import make_album
from album import make_album as ma
# pylint: disable=wildcard-import
from album import *

print("Try-it-Yourself:")
print("Assignment 8.16")

my_album = album.make_album("Pink Floyd", "Dark Side of the Moon")
print(my_album)

my_album = a.make_album("Fleetwood Mac", "Rumors")
print(my_album)

my_album = make_album("David Bowie", "The Rise and Fall of Ziggy Stardust")
print(my_album)

my_album = ma("The Beatles", "Abbey Road")
print(my_album)
