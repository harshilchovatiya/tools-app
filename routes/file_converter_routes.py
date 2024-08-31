from flask import Blueprint, request, jsonify
from services.file_converter_service import convert_file_service

bp = Blueprint('file_converter', __name__)

@bp.route('/api/convert_file', methods=['POST'])
def convert_file():
    file = request.files.get('file')
    file_type = request.form.get('file_type')
    output_format = request.form.get('output_format')

    if not file or not file_type or not output_format:
        return jsonify({'error': 'Required data missing'}), 400

    return convert_file_service(file, file_type, output_format)
