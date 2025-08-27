

from flask import Blueprint, request
from services.color_code_service import color_code_conversion_service

bp = Blueprint('color_code', __name__)

@bp.route('/api/color_code', methods=['POST'])
def convert_color_code():
    data = request.json
    color_code = data.get('color_code')
    input_format = data.get('input_format')
    output_format = data.get('output_format')
    return color_code_conversion_service(color_code, input_format, output_format)
