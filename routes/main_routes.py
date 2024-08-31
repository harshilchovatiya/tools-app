from flask import Blueprint, render_template

bp = Blueprint('main_routes', __name__)

@bp.route('/')
def index():
    return render_template('index.html')

@bp.route('/qr_code')
def qr_code():
    return render_template('qr_code.html')

@bp.route('/url_shortener')
def url_shortener():
    return render_template('url_shortener.html')

@bp.route('/image_compressor')
def image_compressor():
    return render_template('image_compressor.html')

@bp.route('/image_upscaler')
def image_upscaler():
    return render_template('image_upscaler.html')

@bp.route('/file_converter')
def file_converter():
    return render_template('file_converter.html')

@bp.route('/image_to_text', methods=['GET'])
def image_to_text_page():
    return render_template('image_to_text.html')

@bp.route('/speedtest', methods=['GET'])
def view_speedtest():
    return render_template('speedtest.html')

@bp.route('/unit_converter', methods=['GET'])
def unit_converter():
    return render_template('unit_converter.html')