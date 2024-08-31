document.getElementById('scale').addEventListener('input', function() {
    document.getElementById('scale_value').textContent = this.value + 'x';
});

function upscaleImage() {
    const imageFile = document.getElementById('image').files[0];
    const scale = document.getElementById('scale').value;

    if (!imageFile) {
        alert('Please select an image to upscale.');
        return;
    }

    const formData = new FormData();
    formData.append('image', imageFile);
    formData.append('scale', scale);

    fetch('/api/image_upscaler', {
        method: 'POST',
        body: formData
    })
    .then(response => response.blob())
    .then(blob => {
        const downloadButton = document.getElementById('download_button');
        const url = URL.createObjectURL(blob);
        downloadButton.href = url;
        downloadButton.download = 'upscaled_image.jpg';
        downloadButton.style.display = 'block';
        document.getElementById('result').innerHTML = 'Image upscaled successfully. <a href="' + url + '" download>Download Image</a>';
    })
    .catch(error => {
        console.error('Error:', error);
    });
}
