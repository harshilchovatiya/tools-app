from flask import Flask, request, jsonify, redirect, render_template, send_file
import hashlib
import qrcode
from io import BytesIO
import base64
import io
from PIL import Image
from docx import Document
import json
from pymongo import MongoClient
# from bson import ObjectId

app = Flask(__name__)

# Initialize MongoDB client
client = MongoClient('mongodb+srv://harahgaming37:3X#b9AxDjN!Jb5H@tools-app.j5whn.mongodb.net/?retryWrites=true&w=majority&appName=tools-app')
db = client['tools_db']
urls_collection = db['urls']

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/qr_code')
def qr_code():
    return render_template('qr_code.html')

@app.route('/url_shortener')
def url_shortener():
    return render_template('url_shortener.html')

@app.route('/image_compressor')
def image_compressor():
    return render_template('image_compressor.html')

@app.route('/image_upscaler')
def image_upscaler():
    return render_template('image_upscaler.html')

@app.route('/file_converter')
def file_converter():
    return render_template('file_converter.html')

# QR Code API
@app.route('/api/qr_code', methods=['POST'])
def generate_qr_code():
    data = request.json
    text = data.get('text')
    if not text:
        return jsonify({'error': 'No text provided'}), 400

    qr = qrcode.QRCode(version=1, box_size=10, border=4)
    qr.add_data(text)
    qr.make(fit=True)

    img = qr.make_image(fill='black', back_color='white')

    # Save the image to a BytesIO object and encode it as base64
    buffered = BytesIO()
    img.save(buffered, format="PNG")
    img_str = base64.b64encode(buffered.getvalue()).decode()

    return jsonify({'qr_code': f'data:image/png;base64,{img_str}'}), 200

# URL Shortener API
@app.route('/api/shorten', methods=['POST'])
def shorten_url():
    data = request.json
    long_url = data.get('long_url')
    if not long_url:
        return jsonify({'error': 'No long_url provided'}), 400
    
    short_url = generate_short_url(long_url)
    store_url(short_url, long_url)
    return jsonify({'short_url': short_url}), 200

@app.route('/api/expand/<short_url>', methods=['GET'])
def expand_url(short_url):
    long_url = get_long_url(short_url)
    if long_url:
        return jsonify({'long_url': long_url}), 200
    return jsonify({'error': 'URL not found'}), 404

@app.route('/<short_url>', methods=['GET'])
def redirect_to_long_url(short_url):
    long_url = get_long_url(short_url)
    if long_url:
        return redirect(long_url)
    return 'URL not found', 404

# Image Compressor API
@app.route('/api/image_compressor', methods=['POST'])
def image_gen_compressor():
    if 'image' not in request.files:
        return jsonify({'error': 'No image file provided'}), 400
    
    image_file = request.files['image']
    if not image_file:
        return jsonify({'error': 'Invalid image file'}), 400

    # Get the quality parameter (default to 20 if not provided)
    quality = int(request.form.get('quality', 20))
    if quality < 10 or quality > 90:
        return jsonify({'error': 'Quality must be between 10 and 90'}), 400

    # Open the image file
    image = Image.open(image_file)
    
    # Compress the image
    buffered = io.BytesIO()
    image.save(buffered, format="JPEG", quality=quality)  
    compressed_image = buffered.getvalue()
    
    # Return the compressed image
    return send_file(
        io.BytesIO(compressed_image),
        mimetype='image/jpeg',
        as_attachment=True,  
        download_name='compressed_image.jpg'  
    )

# Image Upscaler API
@app.route('/api/image_upscaler', methods=['POST'])
def image_upscaler_api():
    if 'image' not in request.files:
        return jsonify({'error': 'No image file provided'}), 400

    image_file = request.files['image']
    scale_factor = float(request.form.get('scale', 2))  # Default to 2x scaling

    if not image_file:
        return jsonify({'error': 'Invalid image file'}), 400

    image = Image.open(image_file)

    # Increase image size by scale factor
    width, height = image.size
    new_width = int(width * scale_factor)
    new_height = int(height * scale_factor)
    resized_image = image.resize((new_width, new_height), Image.LANCZOS)
    
    buffered = io.BytesIO()
    resized_image.save(buffered, format="JPEG")
    enhanced_image = buffered.getvalue()

    return send_file(
        io.BytesIO(enhanced_image),
        mimetype='image/jpeg',
        download_name='upscaled_image.jpg'
    )

# File Converter API
@app.route('/api/convert_file', methods=['POST'])
def convert_file():
    file = request.files.get('file')
    file_type = request.form.get('file_type')
    output_format = request.form.get('output_format')

    if not file:
        return jsonify({'error': 'File not provided'}), 400
    if not file_type:
        return jsonify({'error': 'File type not provided'}), 400
    if not output_format:
        return jsonify({'error': 'Output format not provided'}), 400

    try:
        if output_format == 'pdf':
            if file_type == 'image':
                return convert_image_to_pdf(file)
        elif output_format == 'txt':
            if file_type == 'docx':
                return convert_docx_to_txt(file)
            elif file_type == 'json':
                return convert_json_to_txt(file)
        return jsonify({'error': 'Unsupported conversion type'}), 400
    except Exception as e:
        return jsonify({'error': f'Error during conversion: {str(e)}'}), 500





def convert_image_to_pdf(file):
    try:
        image = Image.open(file)
        pdf_output = io.BytesIO()
        image.convert('RGB').save(pdf_output, format='PDF')
        pdf_output.seek(0)
        return send_file(pdf_output, mimetype='application/pdf', download_name='converted_image.pdf')
    except Exception as e:
        return jsonify({'error': f'Error converting image to PDF: {str(e)}'}), 500

def convert_docx_to_txt(file):
    try:
        doc = Document(file)
        text = '\n'.join([p.text for p in doc.paragraphs])
        txt_output = io.BytesIO()
        txt_output.write(text.encode('utf-8'))
        txt_output.seek(0)
        return send_file(txt_output, mimetype='text/plain', download_name='converted_file.txt')
    except Exception as e:
        return jsonify({'error': f'Error converting DOCX to TXT: {str(e)}'}), 500

def convert_json_to_txt(file):
    try:
        data = json.load(file)
        text = json.dumps(data, indent=4)
        txt_output = io.BytesIO()
        txt_output.write(text.encode('utf-8'))
        txt_output.seek(0)
        return send_file(txt_output, mimetype='text/plain', download_name='converted_file.txt')
    except Exception as e:
        return jsonify({'error': f'Error converting JSON to TXT: {str(e)}'}), 500

def generate_short_url(long_url):
    hash_object = hashlib.md5(long_url.encode())
    short_hash = hash_object.hexdigest()[:6]
    return short_hash

def store_url(short_url, long_url):
    urls_collection.update_one(
        {'short_url': short_url},
        {'$set': {'long_url': long_url}},
        upsert=True
    )

def get_long_url(short_url):
    url_data = urls_collection.find_one({'short_url': short_url})
    return url_data['long_url'] if url_data else None

if __name__ == '__main__':
    app.run()
