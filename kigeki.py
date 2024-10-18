import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import pprint

client_id = 'xxxxx'
client_secret = 'xxxxx'
client_credentials_manager = spotipy.oauth2.SpotifyClientCredentials(client_id, client_secret)
spotify = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

music_id = '6pllZAdgBf4QTcFUrF3DzL'
result = spotify.audio_features(music_id)
pprint.pprint(result)