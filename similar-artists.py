import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

client_id = 'xxxxx'
client_secret = 'xxxxx'
client_credentials_manager = spotipy.oauth2.SpotifyClientCredentials(client_id, client_secret)

spotify = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

artist_id = '1S2S00lgLYLGHWA44qGEUs'
result = spotify.artist_related_artists(artist_id)
for artist in result['artists']:
    artist_name = artist['name']
    popularity = artist['popularity']
    genres = artist['genres']
    print("{0} - popularity: {1}, id: {2}".format(artist_name, popularity, genres))