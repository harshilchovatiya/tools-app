from flask import Flask
from routes import main_routes_bp, qr_code_bp, url_shortener_bp, image_compressor_bp, image_upscaler_bp, file_converter_bp, image_to_text_bp, speedtest_bp, unit_converter_bp

def create_app():
    app = Flask(__name__)
    # CORS(app) 
    app.register_blueprint(main_routes_bp)
    app.register_blueprint(qr_code_bp)
    app.register_blueprint(url_shortener_bp)
    app.register_blueprint(image_compressor_bp)
    app.register_blueprint(image_upscaler_bp)
    app.register_blueprint(file_converter_bp)
    app.register_blueprint(image_to_text_bp)
    app.register_blueprint(speedtest_bp)
    app.register_blueprint(unit_converter_bp)



    return app

app = create_app()
if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug=True)
