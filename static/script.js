function fetchPlaylist() {
    const playlistId = document.getElementById('playlist-id').value;
    fetch('/fetch-playlist', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({playlist_id: playlistId}),
    })
    .then(response => response.json())
    .then(data => {
        displayPlaylistInfo(data.playlist);
        displaySongs(data.tracks);
    })
    .catch(error => console.error('Error:', error));
}

function displayPlaylistInfo(playlist) {
    const playlistInfo = document.getElementById('playlist-info');
    playlistInfo.innerHTML = `
        <h2>${playlist.name}</h2>
        <p>${playlist.description}</p>
        <img src="${playlist.image}" alt="${playlist.name}" class="playlist-image">
    `;
}

function displaySongs(songs) {
    const songList = document.getElementById('song-list');
    songList.innerHTML = '';
    songs.forEach(song => {
        const li = document.createElement('li');
        li.innerHTML = `
            <img src="${song.image}" alt="${song.album}" class="album-image">
            <div class="song-info">
                <strong>${song.name}</strong> - ${song.artist}
                <br>
                <em>${song.album}</em>
            </div>
        `;
        songList.appendChild(li);
    });
}

// ASCII art generation and interaction will be added here later