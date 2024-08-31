document.getElementById('uploadForm').addEventListener('submit', function(event) {
    event.preventDefault();
    const formData = new FormData(this);

    fetch('/api/image_to_text', {
        method: 'POST',
        body: formData
    })
    .then(response => response.json())
    .then(data => {
        if (data.text) {
            document.getElementById('result').innerHTML = `<pre>${data.text}</pre>`;
        } else {
            alert('Failed to convert image to text.');
        }
    })
    .catch(error => {
        console.error('Error:', error);
    });
});
