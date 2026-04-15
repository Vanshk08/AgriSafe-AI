# AgriSafe AI Project Structure

## Folder Overview

```
AgriSafe-AI/
├── frontend/                    # React frontend application
│   ├── public/
│   │   └── index.html          # Main HTML file
│   ├── src/
│   │   ├── components/         # React components
│   │   │   ├── ImageUploader.js
│   │   │   ├── ImageUploader.css
│   │   │   ├── RiskPredictor.js
│   │   │   └── RiskPredictor.css
│   │   ├── App.js              # Main app component
│   │   ├── App.css             # App styles
│   │   └── index.js            # React entry point
│   ├── .env                    # Environment variables
│   └── package.json            # Dependencies
│
├── backend/                     # Flask backend API
│   ├── app.py                  # Main Flask application
│   ├── image_classifier.py     # Image classification module
│   ├── risk_predictor.py       # Risk prediction module
│   ├── requirements.txt        # Python dependencies
│   └── uploads/                # Temporary image uploads
│
├── models/                      # AI model training scripts
│   ├── train_image_classifier.py      # Image model training
│   ├── train_risk_predictor.py        # Risk model training
│   ├── dataset_loader.py              # Dataset utilities
│   ├── requirements.txt               # Model training dependencies
│   └── saved_models/                  # Trained model files
│       ├── food_classifier.h5         # TensorFlow model
│       └── risk_predictor.pkl         # Scikit-learn model
│
└── dataset/                     # Food image dataset
    └── images/
        ├── fresh/              # Fresh food images
        └── spoiled/            # Spoiled food images
```

## Architecture Overview

### Frontend
- **Framework**: React 18
- **Styling**: CSS3
- **API Communication**: Axios

### Backend
- **Framework**: Flask
- **API**: RESTful endpoints
- **CORS**: Enabled for frontend communication

### AI Models
1. **Image Classifier**: TensorFlow/Keras with MobileNetV2 transfer learning
2. **Risk Predictor**: Scikit-learn Random Forest

## Technology Stack

| Component | Technology |
|-----------|-----------|
| Frontend | React, Axios, CSS3 |
| Backend | Flask, Python 3.8+ |
| Image Model | TensorFlow 2.13, Keras |
| Risk Model | Scikit-learn Random Forest |
| Dataset | Synthetic images, CSV data |

## Key Features

✓ Image-based food contamination detection
✓ Risk prediction based on food properties
✓ Real-time predictions with confidence scores
✓ API error handling and validation
✓ Responsive UI design
✓ Complete training pipelines
