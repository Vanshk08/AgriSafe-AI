# SaveFood AI - Development Guide

## 🎯 For Developers

This guide helps developers understand and extend the SafeFood AI project.

## Project Architecture

### Frontend Architecture
```
App (Main Component)
├── Header (Status, Navigation)
├── ImageUploader Component
│   ├── File Input Handler
│   ├── Preview Manager
│   └── API Integration
├── RiskPredictor Component
│   ├── Form Management
│   ├── Input Validation
│   └── API Integration
└── Results Display
    └── Combined Analysis
```

### Backend Architecture
```
Flask App
├── Routes
│   ├── /health - Status check
│   ├── /predict-image - ML inference
│   ├── /predict-risk - ML inference
│   └── /food-types - Data endpoint
├── Image Classification Module
│   ├── Model Loading
│   ├── Image Preprocessing
│   └── Prediction Logic
└── Risk Prediction Module
    ├── Feature Preparation
    ├── Model Loading
    └── Prediction Logic
```

### AI Model Structure
```
Image Classifier
├── MobileNetV2 (Base)
├── GlobalAveragePooling2D
├── Dense(256) + Dropout
├── Dense(128) + Dropout
└── Dense(2) + Softmax

Risk Predictor
└── RandomForest
    └── 100 Estimators
```

## Code Style

### Python
- Follow PEP 8 guidelines
- Use meaningful variable names
- Add docstrings to functions
- Keep functions focused and small

### JavaScript/React
- Use functional components with hooks
- Follow React naming conventions
- Add JSDoc comments for complex functions
- Use CSS modules or styled-components

## Adding New Features

### Add New Food Type
1. Update `FOOD_TYPES` in `backend/config.py`
2. Update risk model if needed (retrain)
3. Update risk predictor validation in `app.py`
4. Update frontend dropdown display

### Add New API Endpoint
1. Create function in `app.py`
2. Add route decorator `@app.route('/endpoint', methods=['POST/GET'])`
3. Add error handling and validation
4. Document in `API_DOCUMENTATION.md`
5. Test with curl or Postman
6. Update frontend to call endpoint

### Improve Model Accuracy
1. Update training script
2. Collect or generate better training data
3. Adjust model architecture (layers, parameters)
4. Tune hyperparameters
5. Retrain models
6. Evaluate metrics
7. Confirm improvements

### Update UI/Styling
1. Modify component `.css` files
2. Test responsive design (mobile/tablet/desktop)
3. Use CSS variables for consistent theming
4. Ensure accessibility (ARIA labels, color contrast)

## Testing

### Manual Testing
1. **Image Prediction**: Upload various food images
2. **Risk Prediction**: Try different combinations of inputs
3. **Error Handling**: Test with invalid inputs
4. **API Health**: Check /health endpoint
5. **Responsiveness**: Test on different screen sizes

### Unit Testing (Future)
```bash
# Backend tests
pytest tests/

# Frontend tests
npm test
```

## Deployment

### Production Checklist
- [ ] Set DEBUG = False in Flask
- [ ] Use production database
- [ ] Set SECRET_KEY
- [ ] Update CORS_ORIGINS
- [ ] Use environment variables
- [ ] Enable HTTPS
- [ ] Set up logging
- [ ] Configure error monitoring
- [ ] Test all API endpoints
- [ ] Performance test models
- [ ] Document deployment steps

### Environment Variables
```
# Backend
FLASK_ENV=production
FLASK_DEBUG=False
SECRET_KEY=<random-secret>
API_HOST=0.0.0.0
API_PORT=5000

# Frontend
REACT_APP_API_URL=https://api.safefood.ai
```

## Performance Optimization

### Frontend
- Lazy load images
- Minify CSS/JS
- Use production React build
- Enable gzip compression
- Implement caching

### Backend
- Cache model predictions (optional)
- Use connection pooling
- Implement request rate limiting
- Optimize database queries (if using DB)
- Use CDN for static files

### Models
- Consider model quantization
- Convert TensorFlow to TensorFlow Lite
- Implement inference caching
- Use GPU acceleration if available
- Monitor inference time

## Monitoring

### Logging
```python
import logging
logger = logging.getLogger(__name__)
logger.info("Message")
logger.error("Error message")
```

### Metrics to Track
- API response time
- Model inference time
- Error rates
- User engagement
- Model accuracy degradation

## Database Integration (Future)

### Setup
```python
from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy(app)

# Create models
class Prediction(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    image_path = db.Column(db.String(200))
    prediction = db.Column(db.String(50))
    confidence = db.Column(db.Float)
    timestamp = db.Column(db.DateTime)
```

## Extending with New Models

### Add a New Classification Task
1. Create new model training script
2. Train and save model
3. Create inference module
4. Add API endpoint
5. Update frontend with new component
6. Document new feature

Example: Add spoilage severity classification
```python
# backend/spoilage_classifier.py
class SpoilageClassifier:
    def predict(self, image_path):
        # Returns: mild, moderate, severe
        pass

# In app.py
@app.route('/predict-spoilage', methods=['POST'])
def predict_spoilage():
    # Implementation
    pass
```

## Security Considerations

### File Upload Security
- ✅ Validate file extensions
- ✅ Check file size limits
- ✅ Store in temporary directory
- ✅ Clean up after processing
- ✅ Use secure filenames

### API Security
- [ ] Implement authentication (JWT recommended)
- [ ] Add rate limiting
- [ ] Validate all inputs
- [ ] Sanitize error messages
- [ ] Use HTTPS in production
- [ ] Add CORS restrictions

### Code Security
- [ ] Keep dependencies updated
- [ ] Use environment variables for secrets
- [ ] Don't commit sensitive data
- [ ] Regular security audits
- [ ] Use parameterized queries (if DB)

## Useful Commands

```bash
# Backend debugging
python -m pdb scripts.py  # Python debugger

# Frontend debugging
npm run build --analyze  # Analyze bundle size

# Model analysis
tensorboard --logdir=logs/

# Performance profiling
python -m cProfile app.py
```

## Troubleshooting Development

### Issue: Models not training
- Check RAM availability (need 4GB+)
- Verify dataset exists
- Check TensorFlow/sklearn versions
- Try with fewer epochs first

### Issue: API crashes on request
- Check error logs
- Validate input data
- Test model independently
- Check for memory leaks

### Issue: Frontend not updating
- Clear cache: Ctrl+Shift+Del
- Rebuild: npm run build
- Restart dev server
- Check console for errors

## Contributing Guidelines

1. Create feature branch: `git checkout -b feature/your-feature`
2. Make changes with clear commits
3. Test thoroughly
4. Update documentation
5. Submit pull request with description
6. Address review comments
7. Merge when approved

---

**Happy Coding! 🚀**
