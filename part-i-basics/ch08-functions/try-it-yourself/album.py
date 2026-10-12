"""Module for assignment 8.16"""

def make_album(artist, album, songs = None):
    """Create a new album"""
    album = {"Artist": artist.title(), "Title": album.title()}
    if songs:
        album["Tracks"] = songs
    return album
