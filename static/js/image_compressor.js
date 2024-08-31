document.getElementById('quality').addEventListener('input', function() {
    document.getElementById('quality_value').textContent = this.value + '%';
});

function compressImage() {
    const imageFile = document.getElementById('image').files[0];
    const quality = document.getElementById('quality').value;

    if (!imageFile) {
        alert('Please select an image to compress.');
        return;
    }

    const formData = new FormData();
    formData.append('image', imageFile);
    formData.append('quality', quality);

    fetch('/api/image_compressor', {
        method: 'POST',
        body: formData
    })
    .then(response => response.blob())
    .then(blob => {
        const downloadButton = document.getElementById('download_button');
        const url = URL.createObjectURL(blob);
        downloadButton.href = url;
        downloadButton.download = 'compressed_image.jpg';
        downloadButton.style.display = 'block';
        document.getElementById('result').innerHTML = 'Image compressed successfully. <a href="' + url + '" download>Download Image</a>';
    })
    .catch(error => {
        console.error('Error:', error);
    });
}
