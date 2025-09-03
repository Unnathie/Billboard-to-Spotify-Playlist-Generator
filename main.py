import requests
from bs4 import BeautifulSoup
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import time
import os

sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        client_id=os.getenv("CLIENT_ID"),
        client_secret=os.getenv("SECRET"),
        redirect_uri="http://127.0.0.1:9090/callback",  # same as in your app settings
        scope="playlist-modify-private user-read-private",
        cache_path="token.txt"
    )
)

# Get current user info
me = sp.current_user()
print("Your Spotify username (id) is:", me["id"])

# for billboard
headers={

    "user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36"
}
user_in=input("Which year do you want to musically travel to?Type the date in this format YYYY-MM-DD: ")

response=requests.get(f"https://www.billboard.com/charts/hot-100/{user_in}/",headers=headers)
soup= BeautifulSoup(response.text,"html.parser")
# Scrape song titles + artists
songs = [s.getText().strip() for s in soup.select("li ul li h3.c-title")]
artists = [a.getText().strip() for a in soup.select("li ul li span.c-label.a-no-trucate")]


song_artist_pairs = list(zip(songs, artists))

# ---- Search and Add Songs ----
uris = []
for title, artist in song_artist_pairs:
    query = f"track:{title} artist:{artist}"
    result = sp.search(q=query, type="track", limit=1)
    tracks = result.get("tracks", {}).get("items", [])
    if tracks:
        uris.append(tracks[0]["uri"])
        print(f"✓ Found: {title} — {artist}")
    else:
        print(f"✗ Not found: {title} — {artist}")
    time.sleep(0.2)


me = sp.current_user()
user_id = me["id"]
# ---- Create Spotify Playlist ----
playlist = sp.user_playlist_create(
    user=user_id,
    name=f"Billboard Hot 100 - {user_in}",
    public=False,
    description=f"Top 100 songs from Billboard on {user_in}"
)
playlist_id = playlist["id"]
print("Created playlist:", playlist["external_urls"]["spotify"])
# Add songs in batches of 100 (Spotify’s limit)
for i in range(0, len(uris), 100):
    sp.playlist_add_items(playlist_id, uris[i:i+100])

print("✅ Playlist complete!")