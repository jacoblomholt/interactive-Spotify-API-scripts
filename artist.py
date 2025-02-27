import main

token = main.get_token()
result = main.search_for_artist(token, "CRO")
artist_id = result["id"]
songs = main.get_songs_by_artist(token, artist_id)

for idx, song in enumerate(songs):
    print(f"{idx + 1}. {song['name']}")