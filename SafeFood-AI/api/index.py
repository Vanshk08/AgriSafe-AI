"""
AgriSafe AI Backend - Vercel Serverless Function
Handles all API routes for food contamination and agricultural risk detection
"""
import sys
import os
from pathlib import Path
import json
from datetime import datetime

# Add backend directory to path for imports
sys.path.insert(0, str(Path(__file__).parent.parent))

from flask import Flask, request, jsonify
from flask_cors import CORS
from werkzeug.utils import secure_filename
import uuid

# Import configuration
from backend.config import (
    SQLALCHEMY_DATABASE_URI, SQLALCHEMY_TRACK_MODIFICATIONS,
    ALLOWED_EXTENSIONS, MAX_FILE_SIZE, FOOD_TYPES, CROP_TYPES,
    MODEL_PATHS, RISK_THRESHOLDS
)

# Initialize Flask app
app = Flask(__name__)
CORS(app)

# Configuration
app.config['UPLOAD_FOLDER'] = '/tmp'  # Use /tmp for Vercel
app.config['MAX_CONTENT_LENGTH'] = MAX_FILE_SIZE
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL', 'sqlite:///agrisafe.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = SQLALCHEMY_TRACK_MODIFICATIONS

# Initialize database
from backend.models import db, AgriculturalInput, EnvironmentalData, ContaminationRisk, FoodSafetyScore, PredictionHistory

db.init_app(app)

# Create upload folder if it doesn't exist
if not os.path.exists(app.config['UPLOAD_FOLDER']):
    os.makedirs(app.config['UPLOAD_FOLDER'])

# Import models and utilities
try:
    from backend.image_classifier import ImageClassifier
    from backend.risk_predictor import RiskPredictor
    from backend.agricultural_risk_calculator import AgriculturalRiskCalculator
    from backend.safety_score_calculator import FoodSafetyScoreCalculator, PreventionAdvisorySystem
    
    # Initialize models
    image_classifier = ImageClassifier(MODEL_PATHS.get('image_classifier', '../models/saved_models/food_classifier.pkl'))
    risk_predictor = RiskPredictor(MODEL_PATHS.get('risk_predictor', '../models/saved_models/risk_predictor.pkl'))
    agricultural_calculator = AgriculturalRiskCalculator()
    safety_calculator = FoodSafetyScoreCalculator()
    advisory_system = PreventionAdvisorySystem()
except Exception as e:
    print(f"Warning: Could not load models - {e}")
    image_classifier = None
    risk_predictor = None

# Health check endpoint
@app.route('/api/health', methods=['GET'])
def health_check():
    """Health check endpoint"""
    return jsonify({
        'status': 'healthy',
        'timestamp': datetime.now().isoformat(),
        'database': 'connected'
    }), 200

# Metadata endpoint
@app.route('/api/metadata', methods=['GET'])
def get_metadata():
    """Get system metadata and configuration"""
    return jsonify({
        'food_types': FOOD_TYPES,
        'crop_types': CROP_TYPES,
        'risk_thresholds': RISK_THRESHOLDS,
        'max_file_size': MAX_FILE_SIZE,
        'allowed_extensions': list(ALLOWED_EXTENSIONS)
    }), 200

# Image prediction endpoint
@app.route('/api/predict-image', methods=['POST'])
def predict_image():
    """Predict food contamination from image"""
    try:
        if 'file' not in request.files:
            return jsonify({'error': 'No file provided'}), 400
        
        file = request.files['file']
        if file.filename == '':
            return jsonify({'error': 'No file selected'}), 400
        
        # Validate file extension
        if not allowed_file(file.filename):
            return jsonify({'error': f'File type not allowed. Allowed: {ALLOWED_EXTENSIONS}'}), 400
        
        # Save file temporarily
        filename = secure_filename(f"{uuid.uuid4()}_{file.filename}")
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(filepath)
        
        try:
            # Classify image
            if image_classifier is None:
                return jsonify({'error': 'Image classifier not available'}), 503
            
            classification_result = image_classifier.predict(filepath)
            
            # Store prediction in database
            with app.app_context():
                prediction = PredictionHistory(
                    batch_id=str(uuid.uuid4()),
                    image_path=filepath,
                    prediction_result=json.dumps(classification_result),
                    confidence=classification_result.get('confidence', 0),
                    created_at=datetime.utcnow()
                )
                db.session.add(prediction)
                db.session.commit()
            
            return jsonify({
                'success': True,
                'prediction': classification_result,
                'batch_id': prediction.batch_id
            }), 200
        
        finally:
            # Clean up file
            if os.path.exists(filepath):
                os.remove(filepath)
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Risk prediction endpoint
@app.route('/api/predict-risk', methods=['POST'])
def predict_risk():
    """Predict agricultural risk"""
    try:
        data = request.get_json()
        
        if not data:
            return jsonify({'error': 'No JSON data provided'}), 400
        
        # Extract fields
        crop_type = data.get('crop_type')
        irrigation_source = data.get('irrigation_source')
        pesticide_used = data.get('pesticide_used')
        pesticide_toxicity = data.get('pesticide_toxicity')
        temperature = data.get('temperature', 20)
        humidity = data.get('humidity', 60)
        rainfall = data.get('rainfall', 0)
        
        if risk_predictor is None:
            return jsonify({'error': 'Risk predictor not available'}), 503
        
        # Prepare features
        features = {
            'crop_type': crop_type,
            'irrigation_source': irrigation_source,
            'pesticide_used': pesticide_used,
            'pesticide_toxicity': pesticide_toxicity,
            'temperature': temperature,
            'humidity': humidity,
            'rainfall': rainfall
        }
        
        # Get risk prediction
        risk_result = risk_predictor.predict(features)
        
        # Store in database
        with app.app_context():
            risk_record = ContaminationRisk(
                crop_type=crop_type,
                risk_level=risk_result.get('risk_level'),
                risk_score=risk_result.get('risk_score', 0),
                affected_area='Unknown',
                environmental_data=json.dumps(features),
                created_at=datetime.utcnow()
            )
            db.session.add(risk_record)
            db.session.commit()
        
        return jsonify({
            'success': True,
            'risk': risk_result
        }), 200
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Agricultural input endpoint
@app.route('/api/agricultural-input', methods=['POST'])
def submit_agricultural_input():
    """Submit agricultural input data"""
    try:
        data = request.get_json()
        
        if not data:
            return jsonify({'error': 'No JSON data provided'}), 400
        
        with app.app_context():
            agricultural_input = AgriculturalInput(
                farmer_name=data.get('farmer_name', 'Unknown'),
                crop_type=data.get('crop_type'),
                field_location=data.get('field_location'),
                planting_date=data.get('planting_date'),
                irrigation_source=data.get('irrigation_source'),
                pesticide_used=data.get('pesticide_used', False),
                pesticide_name=data.get('pesticide_name'),
                pesticide_toxicity=data.get('pesticide_toxicity'),
                notes=data.get('notes', ''),
                created_at=datetime.utcnow()
            )
            db.session.add(agricultural_input)
            db.session.commit()
        
        return jsonify({
            'success': True,
            'message': 'Agricultural input recorded',
            'id': agricultural_input.id
        }), 201
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Batch details endpoint
@app.route('/api/batch/<batch_id>', methods=['GET'])
def get_batch_details(batch_id):
    """Get details of a prediction batch"""
    try:
        with app.app_context():
            prediction = PredictionHistory.query.filter_by(batch_id=batch_id).first()
            
            if not prediction:
                return jsonify({'error': 'Batch not found'}), 404
            
            return jsonify({
                'batch_id': prediction.batch_id,
                'prediction': json.loads(prediction.prediction_result),
                'confidence': prediction.confidence,
                'created_at': prediction.created_at.isoformat()
            }), 200
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Helper function
def allowed_file(filename):
    """Check if file extension is allowed"""
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

# Create tables before first request
with app.app_context():
    db.create_all()

# Export app for Vercel
export_app = app
