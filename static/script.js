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

const trailCharacters = ['@', '#', '$', '%', '&', '*', '!', '?', '<', '>'];
let lastTrailTime = 0;

function createTrailCharacter(x, y) {
    const trailChar = document.createElement('div');
    trailChar.className = 'trail-character';
    trailChar.style.left = `${x}px`;
    trailChar.style.top = `${y}px`;
    trailChar.textContent = trailCharacters[Math.floor(Math.random() * trailCharacters.length)];
    document.getElementById('cursor-trail').appendChild(trailChar);

    setTimeout(() => {
        trailChar.style.opacity = '0';
    }, 100);

    setTimeout(() => {
        trailChar.remove();
    }, 1000);
}

document.addEventListener('mousemove', (e) => {
    const currentTime = Date.now();
    if (currentTime - lastTrailTime > 50) {  // Limit the rate of trail creation
        createTrailCharacter(e.clientX, e.clientY);
        lastTrailTime = currentTime;
    }
});

// Custom cursor
const cursor = document.createElement('div');
cursor.className = 'trail-character';
cursor.textContent = '_';  // You can change this to any character you like
cursor.style.fontSize = '24px';
document.body.appendChild(cursor);

document.addEventListener('mousemove', (e) => {
    cursor.style.left = `${e.clientX}px`;
    cursor.style.top = `${e.clientY}px`;
});