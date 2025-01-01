from bs4 import BeautifulSoup
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import requests

date = input("Which year do you want to travel to? Input the date in format [YYYY-MM-DD]: ")

header = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:131.0) Gecko/20100101 Firefox/131.0"}

url = f"https://www.billboard.com/charts/hot-100/{date}"
client_id = ENTER YOUR CLIENT ID HERE
client_secret = ENTER YOUR CLIENT SECRET HERE


response = requests.post(url=url, headers=header)
top100songs = response.text

soup = BeautifulSoup(top100songs, 'html.parser')
song_names_spans = soup.select("li ul li h3")
song_names = [song.getText().strip() for song in song_names_spans]

with open("100songs.txt",mode="w") as file:
    for i in song_names:
        file.write(i)
        file.write("\n")

sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri="http://example.com",
        client_id=client_id,
        client_secret=client_secret,
        show_dialog=True,
        cache_path="token.txt",
        username="ABIR GUPTA",
    )
)
user_id = sp.current_user()["id"]

song_uris = []
year = date.split("-")[0]
for song in song_names:
    result = sp.search(q=f"track:{song} year:{year}", type="track")
    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
    except IndexError:
        print(f"{song} doesn't exist in Spotify. Skipped.")

playlist = sp.user_playlist_create(user=user_id, name=f"{date} Billboard 100", public=False)
print("Here's your Playlist!:",playlist["external_urls"]["spotify"],"Enjoy going back in time:")

sp.playlist_add_items(playlist_id=playlist["id"], items=song_uris)
