from flask import Blueprint, request, jsonify
from services.unit_converter_service import (
    convert_area,
    convert_length,
    convert_temperature,
    convert_volume,
    convert_mass,
    convert_data,
    convert_speed,
    convert_time
)

bp = Blueprint('unit_converter', __name__, url_prefix='/api/unit_converter')

@bp.route('/convert', methods=['POST'])
def convert_units():
    data = request.json
    category = data.get('category')
    value = float(data.get('value'))  # Ensure value is a float
    from_unit = data.get('from_unit')
    to_unit = data.get('to_unit')

    try:
        if category == 'area':
            result = convert_area(value, from_unit, to_unit)
        elif category == 'length':
            result = convert_length(value, from_unit, to_unit)
        elif category == 'temperature':
            result = convert_temperature(value, from_unit, to_unit)
        elif category == 'volume':
            result = convert_volume(value, from_unit, to_unit)
        elif category == 'mass':
            result = convert_mass(value, from_unit, to_unit)
        elif category == 'data':
            result = convert_data(value, from_unit, to_unit)
        elif category == 'speed':
            result = convert_speed(value, from_unit, to_unit)
        elif category == 'time':
            result = convert_time(value, from_unit, to_unit)
        else:
            return jsonify({'error': 'Invalid category'}), 400

        return jsonify({'result': result})
    except Exception as e:
        return jsonify({'error': str(e)}), 500
