"""
AgriSafe AI Backend - Vercel Serverless Function
Handles all API routes for food contamination and agricultural risk detection
"""
from flask import Flask, request, jsonify
from flask_cors import CORS
import os
from datetime import datetime

# Initialize Flask app
app = Flask(__name__)
CORS(app, resources={r"/api/*": {"origins": "*"}})

# Configuration
app.config['JSON_SORT_KEYS'] = False

# ============ API Routes ============

# Health check endpoint
@app.route('/api/health', methods=['GET'])
def health_check():
    """Health check endpoint"""
    return jsonify({
        'status': 'healthy',
        'timestamp': datetime.now().isoformat()
    }), 200

# Test route
@app.route('/api/test', methods=['GET'])
def test():
    """Test endpoint to verify API is working"""
    return jsonify({
        'message': 'API is working',
        'environment': 'production' if not os.getenv('DEBUG') else 'development'
    }), 200

# Metadata endpoint
@app.route('/api/metadata', methods=['GET'])
def get_metadata():
    """Get system metadata and configuration"""
    return jsonify({
        'food_types': ['dairy', 'meat', 'seafood', 'produce', 'other'],
        'crop_types': ['grain', 'vegetables', 'fruits', 'legumes', 'herbs', 'spices', 'nuts', 'root_crops', 'leafy_greens', 'other'],
        'risk_thresholds': {
            'low': 30,
            'medium': 70,
            'high': 100
        }
    }), 200

# Image prediction endpoint
@app.route('/api/predict-image', methods=['POST'])
def predict_image():
    """Placeholder for image prediction"""
    return jsonify({
        'success': True,
        'message': 'Image prediction endpoint',
        'prediction': {'status': 'ready'}
    }), 200

# Risk prediction endpoint
@app.route('/api/predict-risk', methods=['POST'])
def predict_risk():
    """Placeholder for risk prediction"""
    return jsonify({
        'success': True,
        'message': 'Risk prediction endpoint',
        'risk': {'risk_level': 'low', 'risk_score': 25}
    }), 200

# Agricultural input endpoint
@app.route('/api/agricultural-input', methods=['POST'])
def agricultural_input():
    """Placeholder for agricultural input"""
    return jsonify({
        'success': True,
        'message': 'Agricultural input recorded',
        'id': 'input-001'
    }), 201

# Batch details endpoint
@app.route('/api/batch/<batch_id>', methods=['GET'])
def get_batch(batch_id):
    """Placeholder for batch details"""
    return jsonify({
        'batch_id': batch_id,
        'prediction': {'status': 'ready'},
        'confidence': 0.95
    }), 200

# ============ Error Handlers ============

@app.errorhandler(404)
def not_found(error):
    """Handle 404 errors"""
    return jsonify({'error': 'Endpoint not found', 'path': request.path}), 404

@app.errorhandler(500)
def internal_error(error):
    """Handle 500 errors"""
    return jsonify({'error': 'Internal server error'}), 500

# ============ Entry Point for Vercel ============

if __name__ == '__main__':
    app.run(debug=True)


