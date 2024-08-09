document.getElementById('quality').addEventListener('input', function() {
    document.getElementById('quality_value').textContent = this.value + '%';
});

async function compressImage() {
    const formData = new FormData(document.getElementById('compressor_form'));
    const quality = document.getElementById('quality').value;
    formData.append('quality', quality);

    const response = await fetch('/api/image_compressor', {
        method: 'POST',
        body: formData
    });

    if (response.ok) {
        const blob = await response.blob();
        const url = URL.createObjectURL(blob);

        // Update the result section with image and download button
        const resultDiv = document.getElementById('result');
        resultDiv.innerHTML = `
            <h2>Compressed Image:</h2>
            <img src="${url}" alt="Compressed Image" style="max-width: 80%;">
        `;
        
        // Display the download button
        const downloadButton = document.getElementById('download_button');
        downloadButton.style.display = 'block';
        downloadButton.href = url;
        downloadButton.download = 'compressed_image.jpg';
        downloadButton.textContent = 'Download Image';
    } else {
        alert('Failed to compress image');
    }
}
