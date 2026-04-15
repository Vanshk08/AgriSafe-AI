# 🍎 AgriSafe AI - Food Contamination Detection Web App

An AI-powered web application that detects food contamination through image analysis and risk prediction based on food properties. Built with React, Flask, TensorFlow, and Scikit-learn.

## 🎯 Project Overview

AgriSafe AI is a complete end-to-end food safety detection system that helps users determine if food is safe to consume using:

1. **Image Analysis**: Deep learning model classifies food as fresh or spoiled
2. **Risk Assessment**: Machine learning model predicts contamination risk based on food type, storage time, and temperature
3. **Comprehensive UI**: Modern, user-friendly interface for easy interaction

## 🌟 Features

- ✅ **Image Upload & Analysis**: Upload food photos for instant freshness detection
- ✅ **Risk Scoring**: Get contamination risk percentage (0-100%)
- ✅ **Food Type Dropdown**: Support for dairy, meat, seafood, produce, and other foods
- ✅ **Storage Time Tracking**: Input storage duration in hours
- ✅ **Temperature Input**: Account for storage temperature conditions
- ✅ **Confidence Scores**: See model confidence levels for all predictions
- ✅ **Real-time Results**: Get instant predictions with detailed analysis
- ✅ **Error Handling**: Comprehensive validation and error messages
- ✅ **Responsive Design**: Works on desktop and mobile devices
- ✅ **API Status Monitoring**: Health checks for backend connectivity

## 🏗️ Technology Stack

### Frontend
- **React 18** - UI framework
- **Axios** - HTTP client
- **CSS3** - Modern styling with flexbox/grid

### Backend
- **Flask** - Web framework
- **Flask-CORS** - Cross-origin resource sharing
- **Python 3.8+** - Backend language

### AI Models
- **TensorFlow 2.13** - Image classification with MobileNetV2
- **Scikit-learn** - Risk prediction with Random Forest
- **Keras** - Deep learning API

## 📋 Prerequisites

- Python 3.8 or higher
- Node.js 14+ and npm
- Git
- 500MB free disk space (for models and dataset)

## 🚀 Quick Start

### Step 1: Clone or Navigate to Project

```bash
# Navigate to the project directory
cd AgriSafe-AI
```

### Step 2: Backend Setup

#### 2a. Create Python Virtual Environment

```bash
# Windows
python -m venv backend_venv
backend_venv\Scripts\activate

# macOS/Linux
python3 -m venv backend_venv
source backend_venv/bin/activate
```

#### 2b. Install Backend Dependencies

```bash
cd backend
pip install -r requirements.txt
cd ..
```

### Step 3: Train AI Models

#### 3a. Set up Model Training Environment

```bash
# Activate backend environment (if not already)
# Windows: backend_venv\Scripts\activate
# macOS/Linux: source backend_venv/bin/activate

cd models
pip install -r requirements.txt
```

#### 3b. Train Models

```bash
# Train Image Classification Model (5-10 minutes)
python train_image_classifier.py

# Train Risk Prediction Model (1-2 minutes)
python train_risk_predictor.py

cd ..
```

**Expected Output:**
- `models/saved_models/food_classifier.h5` (Image classification model)
- `models/saved_models/risk_predictor.pkl` (Risk prediction model)

### Step 4: Start Backend Server

```bash
# Make sure you're in the backend directory
cd backend

# Activate virtual environment (if not already activated)
# Windows: ..\backend_venv\Scripts\activate
# macOS/Linux: source ../backend_venv/bin/activate

# Run Flask server
python app.py
```

**Expected Output:**
```
WARNING in flask_cors.core: (flask_cors) The default value of the 'vary_by' argument of after_request_cors() will change in the next major release from False to True.
 * Serving Flask app 'app'
 * Debug mode: on
 * Running on http://0.0.0.0:5000
```

✅ **Backend running at**: `http://localhost:5000`

### Step 5: Frontend Setup

#### 5a. Install Frontend Dependencies

```bash
# Open a NEW terminal/tab
# Navigate to frontend directory
cd frontend

npm install
```

#### 5b. Configure Frontend Environment

```bash
# The .env file is already configured for local development
# REACT_APP_API_URL=http://localhost:5000
```

#### 5c. Start Development Server

```bash
npm start
```

**Expected Output:**
```
Compiled successfully!

You can now view agrisafe-ai in the browser.

  Local:            http://localhost:3000
  On Your Network:  http://192.168.x.x:3000
```

✅ **Frontend running at**: `http://localhost:3000`

### Step 6: Use the Application

1. Open browser and go to `http://localhost:3000`
2. You should see the AgriSafe AI dashboard
3. Try both features:
   - **Upload an image** for food freshness detection
   - **Input food properties** for risk assessment

## 📁 Project Structure

```
AgriSafe-AI/
├── frontend/              # React application
│   ├── src/
│   │   ├── components/   # React components
│   │   ├── App.js
│   │   └── index.js
│   ├── package.json
│   └── .env
├── backend/              # Flask API
│   ├── app.py
│   ├── image_classifier.py
│   ├── risk_predictor.py
│   └── requirements.txt
├── models/               # AI model training
│   ├── train_image_classifier.py
│   ├── train_risk_predictor.py
│   ├── dataset_loader.py
│   └── saved_models/
└── dataset/              # Food images
    └── images/
```

## 🔌 API Endpoints

### Health Check
```
GET /health
Returns API status and model information
```

### Image Prediction
```
POST /predict-image
Content-Type: multipart/form-data
Body: {image: <file>}

Response: {
  "success": true,
  "prediction": "fresh" | "spoiled",
  "confidence": 0.95,
  "confidence_percentage": 95.0,
  "message": "..."
}
```

### Risk Prediction
```
POST /predict-risk
Content-Type: application/json
Body: {
  "food_type": "dairy" | "meat" | "seafood" | "produce" | "other",
  "storage_time_hours": 24,
  "temperature": 8
}

Response: {
  "success": true,
  "risk_percentage": 35.5,
  "risk_level": "low" | "medium" | "high",
  "safe_to_eat": true,
  "message": "..."
}
```

### Food Types
```
GET /food-types
Returns: {
  "food_types": ["dairy", "meat", "seafood", "produce", "other"]
}
```

## 🧠 AI Model Details

### Image Classification Model
- **Architecture**: MobileNetV2 + Custom Dense Layers
- **Input**: 224×224 RGB images
- **Output**: Fresh vs Spoiled classification with confidence score
- **Training Data**: Synthetic dummy dataset (100 images)
- **Framework**: TensorFlow/Keras

### Risk Prediction Model
- **Algorithm**: Random Forest Regressor (100 estimators)
- **Input Features**: Food type (encoded), storage time (hours), temperature (°C)
- **Output**: Contamination risk (0-100%)
- **Training Data**: Synthetic data (500 samples)
- **Framework**: Scikit-learn

## 🐛 Troubleshooting

### Issue: "Cannot connect to backend API"
**Solution**: 
- Make sure Flask server is running on port 5000
- Check that backend is activated: `cd backend && python app.py`

### Issue: "Models not found" error
**Solution**:
- Train models first: `cd models && python train_image_classifier.py && python train_risk_predictor.py`
- Models should be saved in `models/saved_models/`

### Issue: "Module not found" errors
**Solution**:
- Ensure all dependencies are installed: `pip install -r requirements.txt`
- Use virtual environment: `source backend_venv/bin/activate`

### Issue: Port already in use
**Solution**:
```bash
# Find process using port 5000
lsof -i :5000  # macOS/Linux
netstat -ano | findstr :5000  # Windows

# Kill the process (replace PID with actual process ID)
kill -9 <PID>  # macOS/Linux
taskkill /PID <PID> /F  # Windows
```

### Issue: CORS errors
**Solution**:
- Ensure Flask CORS is properly configured
- Check .env file has correct API URL: `REACT_APP_API_URL=http://localhost:5000`

## 📊 Testing the Application

### Test Case 1: Image Upload
1. Click on image upload area
2. Select a food image from your computer
3. Click "Analyze Image"
4. View freshness prediction with confidence score

### Test Case 2: Risk Assessment
1. Select a food type (e.g., "dairy")
2. Adjust storage time using slider (e.g., 24 hours)
3. Set temperature (e.g., 5°C)
4. Click "Assess Risk"
5. View risk percentage and safety recommendation

### Test Case 3: Combined Analysis
1. Complete both image analysis and risk assessment
2. View "Analysis Summary" section
3. See final recommendation

## 🎨 Customization

### Change API URL
Edit `frontend/.env`:
```
REACT_APP_API_URL=http://your-api-url:5000
```

### Modify Food Types
Edit `backend/app.py` - `valid_food_types` variable:
```python
valid_food_types = ['dairy', 'meat', 'seafood', 'produce', 'other']
```

### Adjust Model Parameters
Edit `models/train_image_classifier.py` or `models/train_risk_predictor.py`:
```python
train_image_classifier(epochs=20, batch_size=32)
```

### Change Risk Thresholds
Edit `backend/app.py` - `/predict-risk` endpoint:
```python
if risk_percentage < 30:  # Low risk threshold
    risk_level = 'low'
```

## 📦 Deployment

### Frontend Deployment (Vercel/Netlify)
```bash
cd frontend
npm run build
# Deploy 'build' folder to Vercel/Netlify
```

### Backend Deployment (Heroku/Railway)
```bash
# Add Procfile
# Deploy with Gunicorn
gunicorn app:app
```

## 📚 Additional Resources

- **TensorFlow Documentation**: https://www.tensorflow.org/
- **Flask Documentation**: https://flask.palletsprojects.com/
- **React Documentation**: https://react.dev/
- **Scikit-learn Documentation**: https://scikit-learn.org/

## 📄 LICENSE

MIT License - See LICENSE file for details

## 👥 Contributing

Contributions are welcome! Please follow these steps:
1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

## 📞 Support

For issues, questions, or suggestions:
- Open an issue on GitHub
- Check existing documentation
- Review troubleshooting section

---

**Made with ❤️ for food safety** | AgriSafe AI v1.0.0
