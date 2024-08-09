document.getElementById('scale').addEventListener('input', function() {
    document.getElementById('scale_value').textContent = this.value + 'x';
});

async function upscaleImage() {
    const formData = new FormData(document.getElementById('upscaler_form'));
    const scale = document.getElementById('scale').value;
    formData.append('scale', scale);

    const response = await fetch('/api/image_upscaler', {
        method: 'POST',
        body: formData
    });

    if (response.ok) {
        const blob = await response.blob();
        const url = URL.createObjectURL(blob);

        // Update the result section with image and download button
        const resultDiv = document.getElementById('result');
        resultDiv.innerHTML = `
            <h2>Upscaled Image:</h2>
            <img src="${url}" alt="Upscaled Image" style="max-width: 80%;">
        `;
        
        // Display the download button
        const downloadButton = document.getElementById('download_button');
        downloadButton.style.display = 'block';
        downloadButton.href = url;
        downloadButton.download = 'upscaled_image.jpg';
        downloadButton.textContent = 'Download Image';
    } else {
        alert('Failed to upscale image');
    }
}
