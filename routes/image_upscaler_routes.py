from flask import Blueprint, request, jsonify, send_file
from services.image_upscaler_service import upscale_image

bp = Blueprint('image_upscaler', __name__)

@bp.route('/api/image_upscaler', methods=['POST'])
def image_upscaler_api():
    if 'image' not in request.files:
        return jsonify({'error': 'No image file provided'}), 400

    image_file = request.files['image']
    scale_factor = float(request.form.get('scale', 2))

    enhanced_image = upscale_image(image_file, scale_factor)

    return send_file(
        enhanced_image,
        mimetype='image/jpeg',
        download_name='upscaled_image.jpg'
    )
