from flask import Blueprint, request, jsonify, send_file
from services.image_compressor_service import compress_image

bp = Blueprint('image_compressor', __name__)

@bp.route('/api/image_compressor', methods=['POST'])
def image_compressor_api():
    if 'image' not in request.files:
        return jsonify({'error': 'No image file provided'}), 400
    
    image_file = request.files['image']
    quality = int(request.form.get('quality', 20))
    if quality < 10 or quality > 90:
        return jsonify({'error': 'Quality must be between 10 and 90'}), 400

    compressed_image = compress_image(image_file, quality)
    
    return send_file(
        compressed_image,
        mimetype='image/jpeg',
        as_attachment=True,  
        download_name='compressed_image.jpg'  
    )
