from flask import Blueprint, request, jsonify
from services.qr_code_service import generate_qr_code_image

bp = Blueprint('qr_code', __name__)

@bp.route('/api/qr_code', methods=['POST'])
def generate_qr_code():
    data = request.json
    text = data.get('text')
    if not text:
        return jsonify({'error': 'No text provided'}), 400

    qr_code_data = generate_qr_code_image(text)
    return jsonify({'qr_code': qr_code_data}), 200
