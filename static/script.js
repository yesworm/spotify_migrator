function fetchPlaylist() {
    // Get the playlist ID from the input field
    const playlistId = document.getElementById('playlist-id').value;

    // Send a POST request to our Flask backend
    fetch('/fetch-playlist', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({playlist_id: playlistId}),
    })
    .then(response => response.json())  // Parse the JSON response
    .then(songs => {
        // Get the ul element where we'll display the songs
        const songList = document.getElementById('song-list');
        // Clear any existing list items
        songList.innerHTML = '';
        // Add each song to the list
        songs.forEach(song => {
            const li = document.createElement('li');
            li.textContent = song;
            songList.appendChild(li);
        });
    })
    .catch(error => console.error('Error:', error));  // Log any errors
}