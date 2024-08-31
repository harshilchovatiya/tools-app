function shortenURL() {
    const longURL = document.getElementById('long_url').value;
    if (!longURL) {
        alert('Please enter a URL to shorten.');
        return;
    }

    fetch('/api/shorten', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ long_url: longURL })
    })
    .then(response => response.json())
    .then(data => {
        if (data.short_url) {
            document.getElementById('result').innerHTML = `Short URL: <a href="/${data.short_url}" target="_blank">/${data.short_url}</a>`;
        } else {
            alert('Failed to shorten URL.');
        }
    })
    .catch(error => {
        console.error('Error:', error);
    });
}
