from flask import Blueprint, request, jsonify, render_template
from services.image_to_text_service import convert_image_to_text

bp = Blueprint('image_to_text', __name__)


@bp.route('/api/image_to_text', methods=['POST'])
def image_to_text():
    try:
        file = request.files['image']
        if not file:
            return jsonify({'error': 'No file provided'}), 400
        
        text = convert_image_to_text(file)
        return jsonify({'text': text}), 200
    except Exception as e:
        print(f"Error: {e}")
        return jsonify({'error': 'Internal Server Error'}), 500
