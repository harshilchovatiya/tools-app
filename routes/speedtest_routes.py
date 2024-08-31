from flask import Blueprint, jsonify, request
from services.speedtest_service import run_speedtest
import logging

bp = Blueprint('speedtest', __name__, url_prefix='/api/speedtest')

@bp.route('/test', methods=['GET'])
def test_speed():
    try:
        # Optional: Check if a specific parameter is passed to control the behavior
        interval = int(request.args.get('interval', 1))  # Interval in seconds
        if interval <= 0:
            raise ValueError("Interval must be a positive integer")

        speed = run_speedtest()
        response = {
            'status': 'success',
            'data': {
                'download_speed': speed['download_speed'],
                'upload_speed': speed['upload_speed'],
                'ping': speed['ping']
            }
        }
        return jsonify(response), 200

    except Exception as e:
        logging.error(f"Error during speed test: {e}")
        return jsonify({'status': 'error', 'message': str(e)}), 500
