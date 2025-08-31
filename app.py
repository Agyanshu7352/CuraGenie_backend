# app.py

import os
import logging
from datetime import datetime
# --- MODIFICATION 1: Add 'send_from_directory' to your imports ---
from flask import Flask, jsonify, send_from_directory
from flask_cors import CORS

# Import configurations and initializers
from utils.config import Config
from utils.database import init_db
from services.gemini_model import configure_gemini

# Import Blueprints (route modules)
from routes.auth_routes import auth_bp
from routes.report_routes import report_bp
from routes.analysis_routes import analysis_bp
from routes.user_routes import user_bp


# pymongo aur motor ke liye logging level warning pe set kar do
logging.getLogger("pymongo").setLevel(logging.WARNING)
logging.getLogger("asyncio").setLevel(logging.WARNING)


def create_app():
    """Create and configure the Flask application."""
    app = Flask(__name__)
    
    # --- 1. Load Configuration ---
    app.config.from_object(Config)
    
    # --- 2. Enable CORS ---
    CORS(
        app,
        resources={r"/api/*": {"origins": os.getenv('CORS_ORIGINS', "http://localhost:5173")}},
        allow_headers=["Authorization", "Content-Type"],
        supports_credentials=True
    )

    # --- 3. Configure Logging ---
    logging.basicConfig(
        level=app.config['LOG_LEVEL'],
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        filename=app.config['LOG_FILE'],
        filemode='a'
    )
    if app.config['DEBUG']:
        logging.getLogger().addHandler(logging.StreamHandler())

    logger = logging.getLogger(__name__)
    logger.info("Flask application configuration loaded.")
    
    # --- 4. Create Upload Directories ---
    os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)
    os.makedirs(app.config['PROCESSED_FOLDER'], exist_ok=True)
    
    # --- 5. Initialize Database and Services within App Context ---
    with app.app_context():
        init_db(app)
        try:
            configure_gemini()
        except ValueError as e:
            logger.critical(f"CRITICAL ERROR: {e}. The application cannot function without the Gemini service.")
    
    # --- 6. Register Blueprints ---
    app.register_blueprint(report_bp, url_prefix='/api/reports')
    app.register_blueprint(analysis_bp, url_prefix='/api/analysis')
    app.register_blueprint(auth_bp, url_prefix='/api/auth')  
    app.register_blueprint(user_bp, url_prefix='/api/user')

    
    logger.info("Blueprints registered.")
    
    # --- 7. Define Root and Health Check Endpoints ---
    @app.route('/', methods=['GET'])
    def root():
        return jsonify({
            'service': 'MediGuide AI Backend',
            'status': 'running',
            'version': '1.0.0',
            'timestamp': datetime.utcnow().isoformat()
        }), 200
    
    @app.route('/api/health', methods=['GET'])
    def health_check():
        db_status = "connected"
        try:
            app.mongo.db.command('ping')
        except Exception as e:
            db_status = f"error: {str(e)}"
        
        return jsonify({
            'status': 'healthy',
            'timestamp': datetime.utcnow().isoformat(),
            'database': db_status
        }), 200
        
    # --- MODIFICATION 2: Add the GET route for serving uploaded files ---
    @app.route('/uploads/<path:filename>')
    def serve_upload(filename):
        """This route serves files from the UPLOAD_FOLDER."""
        return send_from_directory(
            app.config['UPLOAD_FOLDER'],
            filename
        )
    # --------------------------------------------------------------------
        
    # --- 8. Register Global Error Handlers ---
    @app.errorhandler(404)
    def not_found(error):
        return jsonify({'success': False, 'error': 'Endpoint not found'}), 404

    @app.errorhandler(500)
    def internal_error(error):
        logger.error(f"Internal Server Error: {error}")
        return jsonify({'success': False, 'error': 'An internal server error occurred.'}), 500
        
    @app.errorhandler(413)
    def file_too_large(error):
        max_size = app.config['MAX_CONTENT_LENGTH'] / (1024*1024)
        return jsonify({'success': False, 'error': f'File too large. Maximum size is {max_size}MB'}), 413

    logger.info("Flask application created and configured successfully.")
    return app


if __name__ == '__main__':
    app = create_app()
    app.run(
        host='0.0.0.0',
        port=int(os.getenv('FLASK_PORT', 5000)),
        debug=app.config['DEBUG']
    )