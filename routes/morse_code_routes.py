from flask import Blueprint, request, jsonify
from services.morse_code_service import text_to_morse, morse_to_text

bp = Blueprint('morse_code', __name__)

@bp.route('/api/morse_code', methods=['POST'])
def translate_morse_code():
    data = request.get_json()
    text = data.get('text')
    morse_code = data.get('morse_code')

    if text:
        result = text_to_morse(text)
    elif morse_code:
        result = morse_to_text(morse_code)
    else:
        return jsonify({'error': 'No text or Morse code provided'}), 400

    return jsonify({'result': result})
