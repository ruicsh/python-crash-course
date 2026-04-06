def make_album(artist_name, album_title, number_of_songs=None):
    album = {"artist": artist_name.title(), "title": album_title.title()}
    if number_of_songs:
        album["number_of_songs"] = number_of_songs
    return album


print(make_album("the beatles", "revolver", 9))
print(make_album("pink floyd", "dark side of the moon", 10))
print(make_album("queen", "a night at the opera", 11))
