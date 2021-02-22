from datetime import date

import requests
from bs4 import BeautifulSoup
# for auth with spotify
import spotipy
from spotipy.oauth2 import SpotifyOAuth
APP_CLIENT_ID = " "
APP_CLIENT_SECRET = " "
APP_REDIRECT_URI = "http://example.com"

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
                                               client_id=APP_CLIENT_ID,
                                               client_secret= APP_CLIENT_SECRET,
                                               redirect_uri= APP_REDIRECT_URI,
                                               show_dialog="True",
                                               cache_path="token.txt",
                                                scope="playlist-modify-private",
                                               ))
user_id = sp.current_user()["id"]

# results = sp.current_user_saved_tracks()
# for idx, item in enumerate(results['items']):
#     track = item['track']
#     print(idx, track['artists'][0]['name'], " – ", track['name'])


# hard coding the date for build test, uncomment later
# travel_date = input("What date do you want to travel to in format YYYY-MM-DD ?")
#
# URL = "https://www.billboard.com/charts/hot-100/"+ travel_date
URL = "https://www.billboard.com/charts/hot-100/2008-08-25"
response = requests.get(URL)
website_html = response.text
soup = BeautifulSoup(website_html, "html.parser")

song_titles = soup.find_all(name="span", class_="chart-element__information__song text--truncate color--primary")
song_names = [song.getText() for song in song_titles]
# print(song_names)
# song_uris = []
# year = date.split("-")[0]
# for song in song_names:
#     result = sp.search(q=f"track:{song} year:{year}", type="track")
#     print(result)
#     try:
#         uri = result["tracks"]["items"][0]["uri"]
#         song_uris.append(uri)
#     except IndexError:
#         print(f"{song} doesn't exist in Spotify. Skipped.")
song_uris = ["The list of", "song URIs", "you got by", "searching Spotify"]
playlist = sp.user_playlist_create(user=user_id, name=f"{date} Billboard 100", public=False)
# print(playlist)

sp.playlist_add_items(playlist_id=playlist["id"], items=song_uris)