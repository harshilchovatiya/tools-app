function generateQRCode() {
    const qrText = document.getElementById('qr_text').value;
    if (!qrText) {
        alert('Please enter text for the QR code.');
        return;
    }

    fetch('/api/qr_code', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ text: qrText })
    })
    .then(response => response.json())
    .then(data => {
        if (data.qr_code) {
            document.getElementById('qr_result').innerHTML = `<img src="${data.qr_code}" alt="QR Code">`;
        } else {
            alert('Failed to generate QR code.');
        }
    })
    .catch(error => {
        console.error('Error:', error);
    });
}
