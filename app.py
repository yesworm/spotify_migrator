import os
import requests
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Get Spotify API credentials from environment variables
SPOTIFY_CLIENT_ID = os.getenv('SPOTIFY_CLIENT_ID')
SPOTIFY_CLIENT_SECRET = os.getenv('SPOTIFY_CLIENT_SECRET')

def get_spotify_access_token():
    """
    Authenticate with Spotify API and get an access token.
    This token is required for making requests to the Spotify API.
    """
    auth_url = 'https://accounts.spotify.com/api/token'
    auth_response = requests.post(auth_url, {
        'grant_type': 'client_credentials',
        'client_id': SPOTIFY_CLIENT_ID,
        'client_secret': SPOTIFY_CLIENT_SECRET,
    })
    auth_response_data = auth_response.json()
    return auth_response_data['access_token']

def get_spotify_playlist(playlist_id):
    """
    Fetch a playlist's tracks from Spotify API.
    
    :param playlist_id: Spotify playlist ID
    :return: List of songs in the format "Song Name - Artist Name"
    """
    # Get access token
    access_token = get_spotify_access_token()
    
    # Construct the API endpoint URL
    playlist_url = f"https://api.spotify.com/v1/playlists/{playlist_id}"
    
    # Make GET request to Spotify API
    response = requests.get(
        playlist_url,
        headers={
            "Authorization": f"Bearer {access_token}"
        }
    )
    
    # Parse the JSON response
    playlist_data = response.json()
    
    # Extract tracks from the playlist data
    tracks = playlist_data['tracks']['items']
    
    # Create a list of songs with artist names
    return [f"{track['track']['name']} - {track['track']['artists'][0]['name']}" for track in tracks]

def main():
    print("Welcome to the Spotify to Apple Music migration tool!")
    
    # Get playlist ID from user
    playlist_id = input("Please enter the Spotify playlist ID: ")
    
    # Fetch songs from the playlist
    songs = get_spotify_playlist(playlist_id)
    
    # Display the results
    print(f"\nFound {len(songs)} songs in the playlist:")
    for song in songs:
        print(f"- {song}")

# This ensures that the main() function is only run if this script is executed directly
# (not imported as a module)
if __name__ == "__main__":
    main()