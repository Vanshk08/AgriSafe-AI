"""
AgriSafe AI Backend - Vercel Serverless Function
Handles all API routes for food contamination and agricultural risk detection
"""
from flask import Flask, request, jsonify
from flask_cors import CORS
import os
import json
from datetime import datetime

# Initialize Flask app
app = Flask(__name__)
CORS(app)

# Configuration
app.config['JSON_SORT_KEYS'] = False

# Simple health check - no database required
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

# Placeholder endpoints that return 200 to prevent 404s
@app.route('/api/predict-image', methods=['POST'])
def predict_image():
    """Placeholder for image prediction"""
    return jsonify({
        'success': True,
        'message': 'Image prediction endpoint - configure models to enable',
        'prediction': {'status': 'placeholder'}
    }), 200

@app.route('/api/predict-risk', methods=['POST'])
def predict_risk():
    """Placeholder for risk prediction"""
    return jsonify({
        'success': True,
        'message': 'Risk prediction endpoint - configure models to enable',
        'prediction': {'status': 'placeholder'}
    }), 200

@app.route('/api/agricultural-input', methods=['POST'])
def agricultural_input():
    """Placeholder for agricultural input"""
    return jsonify({
        'success': True,
        'message': 'Agricultural input recorded',
        'id': 'placeholder-id'
    }), 201

@app.route('/api/batch/<batch_id>', methods=['GET'])
def get_batch(batch_id):
    """Placeholder for batch details"""
    return jsonify({
        'batch_id': batch_id,
        'message': 'Batch data - configure database to enable'
    }), 200

# Root route for frontend
@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def serve_frontend(path):
    """Serve frontend for non-API routes"""
    # If it's an API route, it should have been caught by the routes above
    # Otherwise return a message
    if path.startswith('api'):
        return jsonify({'error': 'API endpoint not found'}), 404
    
    # For all other routes, return a simple response
    return jsonify({'message': 'Frontend would be served here. API is available at /api/'}), 200

# Error handler for 404
@app.errorhandler(404)
def not_found(error):
    return jsonify({'error': 'Endpoint not found', 'path': request.path}), 404

# Error handler for 500
@app.errorhandler(500)
def internal_error(error):
    return jsonify({'error': 'Internal server error'}), 500

# Export for Vercel
if __name__ == '__main__':
    app.run(debug=True)

