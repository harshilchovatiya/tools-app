function convertFile() {
    const formData = new FormData(document.getElementById('converter_form'));

    fetch('/api/convert_file', {
        method: 'POST',
        body: formData
    })
    .then(response => response.blob())
    .then(blob => {
        const downloadButton = document.getElementById('download_button');
        const url = URL.createObjectURL(blob);
        downloadButton.href = url;
        downloadButton.download = 'converted_file.' + formData.get('output_format');
        downloadButton.style.display = 'block';
        document.getElementById('result').innerHTML = 'File converted successfully. <a href="' + url + '" download>Download File</a>';
    })
    .catch(error => {
        console.error('Error:', error);
    });
}
