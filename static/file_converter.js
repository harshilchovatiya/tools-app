async function convertFile() {
    const formData = new FormData(document.getElementById('converter_form'));
    
    try {
        const response = await fetch('/api/convert_file', {
            method: 'POST',
            body: formData
        });
        
        if (response.ok) {
            const blob = await response.blob();
            const url = URL.createObjectURL(blob);

            // Update the result section with download link
            const resultDiv = document.getElementById('result');
            const fileName = formData.get('file').name;
            resultDiv.innerHTML = `
                <h2>Converted File:</h2>
                <a href="${url}" download="${fileName.split('.')[0]}.${formData.get('output_format')}">Download ${formData.get('output_format').toUpperCase()} File</a>
            `;
        } else {
            const errorText = await response.text();
            console.error('Conversion failed:', errorText);
            alert('Failed to convert file: ' + errorText);
        }
    } catch (error) {
        console.error('Error:', error);
        alert('Failed to convert file');
    }
}
