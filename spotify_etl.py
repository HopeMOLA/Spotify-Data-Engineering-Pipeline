import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import pandas as pd

# Replace with your credentials
client_id = "be5ba9c22f094c50b2a9e20db7c11d98"
client_secret = "d90ef61de50f4ce8ab45335e1dc8590d"

# Authenticate
auth_manager = SpotifyClientCredentials(
    client_id=client_id,
    client_secret=client_secret
)

sp = spotipy.Spotify(auth_manager=auth_manager)

# Playlist link
playlist_link = "https://open.spotify.com/playlist/6OuqMHXfqiAWHLvzxhUtnP?si=kdZ4riJsQpOS8JaQZtyY1w"
playlist_URI = playlist_link.split("/")[-1]

# Get playlist data
data = sp.playlist_tracks(playlist_URI)

songs = []
artists = []
popularity = []

for item in data['items']:
    track = item['track']
    
    if track is not None:
        songs.append(track['name'])
        artists.append(track['artists'][0]['name'])
        popularity.append(track['popularity'])

# Create dataframe
df = pd.DataFrame({
    "song": songs,
    "artist": artists,
    "popularity": popularity
})

# Save to CSV
df.to_csv("spotify_data.csv", index=False)

print("Spotify data extracted successfully!")
