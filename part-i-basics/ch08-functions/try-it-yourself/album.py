"""Module for assignment 8.16"""

def make_album(artist, title, songs = None) -> dict[str, any]:
    """Create a new album"""
    album = {"Artist": artist.title(), "Title": title.title()}
    if songs:
        album["Tracks"] = songs
    return album
