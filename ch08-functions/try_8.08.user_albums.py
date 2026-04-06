def make_album(artist_name, album_title, number_of_songs=None):
    album = {"artist": artist_name.title(), "title": album_title.title()}
    if number_of_songs:
        album["number_of_songs"] = number_of_songs
    return album


while True:
    artist = input("Artist: ")
    if artist == "q":
        break
    title = input("Album: ")
    if title == "q":
        break

    album = make_album(artist, title)
    print(album)
