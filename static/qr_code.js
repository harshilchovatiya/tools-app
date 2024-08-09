async function generateQRCode() {
    const qrText = document.getElementById('qr_text').value;
    const qrResult = document.getElementById('qr_result');

    const response = await fetch('/api/qr_code', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ text: qrText })
    });

    if (response.ok) {
        const data = await response.json();
        qrResult.innerHTML = `<img src="${data.qr_code}" alt="QR Code">`;
    } else {
        alert('Failed to generate QR Code');
    }
}
