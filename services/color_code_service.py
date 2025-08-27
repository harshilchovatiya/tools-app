# services/color_code_service.py

from flask import jsonify

def convert_color_code(color_code, input_format, output_format):
    try:
        from colormath.color_objects import (
            HexColor, RGBColor, HSLColor, CMYKColor, HSVColor
        )
        from colormath.color_conversions import convert_color

        # Map formats to color objects
        color_objects = {
            'hex': HexColor,
            'rgb': RGBColor,
            'hsl': HSLColor,
            'cmyk': CMYKColor,
            'hsv': HSVColor
        }

        # Parse input color code
        input_color = color_objects[input_format](color_code)
        output_color = convert_color(input_color, color_objects[output_format])

        # Convert to string format
        return str(output_color)

    except Exception as e:
        return str(e)

def color_code_conversion_service(color_code, input_format, output_format):
    result = convert_color_code(color_code, input_format, output_format)
    return jsonify({'result': result})
