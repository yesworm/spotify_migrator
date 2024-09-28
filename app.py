# Import necessary modules
from flask import Flask, render_template, request, jsonify
from spotify_utils import get_spotify_playlist
import os

# Initialize the Flask application
app = Flask(__name__)

# Define a route for the home page
@app.route('/')
def index():
    # Render the index.html template when accessing the root URL
    return render_template('index.html')

# Define a route for fetching playlist data
@app.route('/fetch-playlist', methods=['POST'])
def fetch_playlist():
    # Get the playlist ID from the JSON data sent in the POST request
    playlist_id = request.json['playlist_id']
    # Use our existing function to get the playlist songs
    songs = get_spotify_playlist(playlist_id)
    # Return the songs as a JSON response
    return jsonify(songs)

# Run the Flask app if this file is executed directly
if __name__ == '__main__':
    app.run(debug=True)
