async function shortenURL() {
    const longURL = document.getElementById('long_url').value;
    const response = await fetch('/api/shorten', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ long_url: longURL })
    });

    if (response.ok) {
        const data = await response.json();
        document.getElementById('result').innerHTML = `
            <h2>Your Short URL:</h2>
            <a href="${window.location.origin}/${data.short_url}" target="_blank">${window.location.origin}/${data.short_url}</a>
        `;
    } else {
        alert('Failed to shorten URL');
    }
}
