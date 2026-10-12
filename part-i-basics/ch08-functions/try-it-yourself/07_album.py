"""Assignment 8.7"""

# Album: Write a function called `make_album()` that builds a
#        dictionary describing a music album. The function should
#        take in an artist name and an album title, and it should
#        return a dictionary containing these two pieces of
#        information. Use the function to make three dictionaries
#        representing different albums. Print each return value
#        to show that the dictionaries are storing the album
#        information correctly.
#
#        Use `None` to add an optional parameter to `make_album()`
#        that allows you to store the number of songs on an album.
#        If the calling line includes a value for the number of
#        songs, add that value to the album's dictionary. Make at
#        least one new function call that includes the number of
#        songs on an album.

print("Try-it-Yourself:")
print("Assignment 8.7")

def make_album(artist, album, songs=None):
    """Return a dictionary describing a music album"""
    album = {"Artist": artist.title(), "Title": album.title()}
    if songs:
        album["Tracks"] = songs
    return album

my_album = make_album("pink floyd", "animals")
print(my_album)
my_album = make_album("simon & garfunkel", "sounds of silence")
print(my_album)
my_album = make_album("they might be giants", "flood")
print(my_album)
my_album = make_album("john prine", "fair & square", 14)
print(my_album)
