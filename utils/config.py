# /utils/config.py

import os
from dotenv import load_dotenv

# Load environment variables from a .env file
load_dotenv()

class Config:
    """
    Flask configuration class.
    Loads configuration variables from environment variables.
    """
    # --- Flask Core ---
    SECRET_KEY = os.getenv('SECRET_KEY', 'a-fallback-secret-key-for-development')
    DEBUG = os.getenv('DEBUG', 'False').lower() in ('true', '1', 't')
    
    # --- Database ---
    MONGO_URI = os.getenv('MONGO_URI', 'mongodb://localhost:27017/mediguide_ai')
    
    # --- JWT Authentication ---
    JWT_SECRET_KEY = os.getenv('JWT_SECRET_KEY', 'a-fallback-jwt-secret-key')
    
    # --- File Uploads ---
    MAX_CONTENT_LENGTH = int(os.getenv('MAX_CONTENT_LENGTH', 16 * 1024 * 1024)) # 16MB default
    UPLOAD_FOLDER = os.getenv('UPLOAD_FOLDER', 'uploads')
    PROCESSED_FOLDER = os.getenv('PROCESSED_FOLDER', 'processed')
    
    # --- External Services ---
    GEMINI_API_KEY = os.getenv('GEMINI_API_KEY')
    OCR_API_KEY = os.getenv('OCR_API_KEY')
    OCR_API_URL = os.getenv('OCR_API_URL', 'https://api.ocr.space/parse/image')
    
    # --- CORS ---
    # We handle CORS in app.py directly for more control
    
    # --- Logging ---
    LOG_LEVEL = os.getenv('LOG_LEVEL', 'INFO')
    LOG_FILE = os.getenv('LOG_FILE', 'mediguide.log')

