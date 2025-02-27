import main

def search_for_artist(token, artist_name):
    url = f"https://api.spotify.com/v1/search?q={artist_name}&type=artist&limit=1"
    headers = main.get_header(token)
    
    result = main.get(url, headers=headers)
    json_result = main.json.loads(result.content)["artists"]["items"]
    
    if not json_result:
        print("No artist with this name")
        return None
    
    for artist in json_result:
        if artist["name"].lower() == artist_name.lower():
            return artist

    return None

def get_top_tracks_by_artist(token, artist_id):
    url = f"https://api.spotify.com/v1/artists/{artist_id}/top-tracks?country=DK"
    headers = main.get_header(token)

    result = main.get(url, headers=headers)
    json_result = main.json.loads(result.content)["tracks"]
    return json_result

def get_albums_by_artist(token, artist_id):
    url = f"https://api.spotify.com/v1/artists/{artist_id}/albums"
    headers = main.get_header(token)

    result = main.get(url, headers=headers)
    json_result = main.json.loads(result.content)["items"]
    return json_result

def user_wants_information(token):
    user_artist = input("Type the name of an artist: ")
    artist_data = search_for_artist(token, user_artist)

    if artist_data == None:
        print("No such artist exists on spotify")
        return None

    artist_id = artist_data["id"]

    print("Choose something you want to know about this artist:")
    print("Type one of these options: top tracks, albums")

    user_input = input()

    if user_input == "top tracks":
        res = get_top_tracks_by_artist(token, artist_id)
        for idx, song in enumerate(res):
            print(f"{idx + 1}. {song['name']}")
    elif user_input == "albums":
        res = get_albums_by_artist(token, artist_id)
        for idx, album in enumerate(res):
            print(f"{idx + 1}. {album['name']}")


token = main.get_token()
user_wants_information(token)