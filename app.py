from flask import Flask, render_template, request, jsonify
from spotify_utils import get_spotify_playlist
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/fetch-playlist', methods=['POST'])
def fetch_playlist():
    playlist_id = request.json['playlist_id']
    playlist_data = get_spotify_playlist(playlist_id)
    return jsonify(playlist_data)

if __name__ == '__main__':
    app.run(debug=True)
    app.run(debug=True)
