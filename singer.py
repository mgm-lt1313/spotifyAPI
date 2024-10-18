import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

client_id = 'xxxxx'
client_secret = 'xxxxx'
client_credentials_manager = spotipy.oauth2.SpotifyClientCredentials(client_id, client_secret)

spotify = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

name = 'Gen Hoshino'
result = spotify.search(q='artist:' + name, type='artist')
print(result)

print('')

for i in result['artists']['items']:
    print("{0} popularity: {1}".format(i['name'], i['popularity']))