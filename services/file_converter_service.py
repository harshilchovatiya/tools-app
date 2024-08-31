from flask import send_file, jsonify
from utils.file_converter_utils import convert_image_to_pdf, convert_docx_to_txt, convert_json_to_txt

def convert_file_service(file, file_type, output_format):
    try:
        if output_format == 'pdf' and file_type == 'image':
            return convert_image_to_pdf(file)
        elif output_format == 'txt':
            if file_type == 'docx':
                return convert_docx_to_txt(file)
            elif file_type == 'json':
                return convert_json_to_txt(file)
        return jsonify({'error': 'Unsupported conversion type'}), 400
    except Exception as e:
        return jsonify({'error': f'Error during conversion: {str(e)}'}), 500
