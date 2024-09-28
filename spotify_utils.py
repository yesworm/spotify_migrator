import os
import requests
from dotenv import load_dotenv

load_dotenv()

SPOTIFY_CLIENT_ID = os.getenv('SPOTIFY_CLIENT_ID')
SPOTIFY_CLIENT_SECRET = os.getenv('SPOTIFY_CLIENT_SECRET')

def get_spotify_access_token():
    auth_url = 'https://accounts.spotify.com/api/token'
    auth_response = requests.post(auth_url, {
        'grant_type': 'client_credentials',
        'client_id': SPOTIFY_CLIENT_ID,
        'client_secret': SPOTIFY_CLIENT_SECRET,
    })
    auth_response_data = auth_response.json()
    return auth_response_data['access_token']

def get_spotify_playlist(playlist_id):
    access_token = get_spotify_access_token()
    playlist_url = f"https://api.spotify.com/v1/playlists/{playlist_id}"
    response = requests.get(
        playlist_url,
        headers={
            "Authorization": f"Bearer {access_token}"
        }
    )
    playlist_data = response.json()
    
    # Extract playlist details
    playlist_info = {
        'name': playlist_data['name'],
        'description': playlist_data['description'],
        'image': playlist_data['images'][0]['url'] if playlist_data['images'] else None
    }
    
    # Extract track details
    tracks = playlist_data['tracks']['items']
    track_info = [{
        'name': track['track']['name'],
        'artist': track['track']['artists'][0]['name'],
        'album': track['track']['album']['name'],
        'image': track['track']['album']['images'][0]['url'] if track['track']['album']['images'] else None
    } for track in tracks]
    
    return {
        'playlist': playlist_info,
        'tracks': track_info
    }