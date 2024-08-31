from flask import Blueprint, request, jsonify, redirect
from services.url_shortener_service import generate_short_url, store_url, get_long_url


bp = Blueprint('url_shortener', __name__)

@bp.route('/api/shorten', methods=['POST'])
def shorten_url():
    try:
        data = request.json
        long_url = data.get('long_url')
        
        if not long_url:
            return jsonify({'error': 'No long_url provided'}), 400
        
        short_url = generate_short_url(long_url)
        store_url(short_url, long_url)
        
        return jsonify({'short_url': short_url}), 200
    except Exception as e:
        print(f"Error: {e}")  # This will print to the server logs
        return jsonify({'error': 'Internal Server Error'}), 500


@bp.route('/expand/<short_url>', methods=['GET'])
def expand_url(short_url):
    long_url = get_long_url(short_url)
    if long_url:
        return jsonify({'long_url': long_url}), 200
    return jsonify({'error': 'URL not found'}), 404

@bp.route('/<short_url>', methods=['GET'])
def redirect_to_long_url(short_url):
    long_url = get_long_url(short_url)
    if long_url:
        return redirect(long_url)
    return 'URL not found', 404
