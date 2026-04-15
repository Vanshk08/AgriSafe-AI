# SafeFood AI - Implementation & Setup Guide

## Quick Start

### 1. Install Backend Dependencies

```bash
cd backend
pip install -r requirements.txt
```

**New dependencies added:**
- Flask-SQLAlchemy>=3.0.0 (database ORM)
- requests>=2.31.0 (for optional weather API integration)

### 2. Initialize Database

```bash
# Option A: Automatic (on first API call)
# Database will be created automatically when you run the Flask app

# Option B: Manual initialization
python
>>> from app import app, db, models
>>> with app.app_context():
>>>     db.create_all()
>>> exit()
```

### 3. Start Backend Server

```bash
python app.py
```

Server will run on: `http://localhost:5000`

**First run output:**
```
 * Running on http://0.0.0.0:5000 (Press CTRL+C to quit)
```

### 4. Install Frontend Dependencies

```bash
cd frontend
npm install
```

### 5. Start Frontend Development Server

```bash
npm start
```

App will run on: `http://localhost:3000`

Browser will automatically open the application.

---

## Testing the New Features

### Test 1: Submit Agricultural Data

```bash
curl -X POST http://localhost:5000/agricultural-input \
  -H "Content-Type: application/json" \
  -d '{
    "crop_type": "vegetables",
    "irrigation_source": "groundwater",
    "days_since_harvest": 2,
    "pesticide_used": "Glyphosate",
    "days_since_pesticide": 5,
    "temperature": 28,
    "humidity": 75
  }'
```

**Expected Response:**
```json
{
  "success": true,
  "batch_id": "BATCH-XXXXX",
  "agricultural_data": {...},
  "environmental_data": {...}
}
```

### Test 2: Get Agricultural Risk

```bash
curl -X GET http://localhost:5000/agricultural-risk/BATCH-XXXXX
```

**Expected Response:**
```json
{
  "success": true,
  "batch_id": "BATCH-XXXXX",
  "risks": {
    "overall_risk": {
      "risk_score": 45.2,
      "risk_level": "medium",
      "probability_score": 0.452
    },
    "chemical_risk": {...},
    "biological_risk": {...},
    "environmental_risk": {...},
    "harvest_safety": {...}
  }
}
```

### Test 3: Calculate Food Safety Score

```bash
curl -X POST http://localhost:5000/food-safety-score/BATCH-XXXXX \
  -H "Content-Type: application/json" \
  -d '{}'
```

**Expected Response:**
```json
{
  "success": true,
  "batch_id": "BATCH-XXXXX",
  "safety_score": {
    "overall_score": 62,
    "agricultural_practices_score": 70,
    "environmental_risk_score": 55,
    "ai_prediction_score": 65,
    "safe_for_consumption": true
  },
  "recommendations": [...],
  "advisory_summary": {...}
}
```

### Test 4: Get Batch Traceability

```bash
curl -X GET http://localhost:5000/batch/BATCH-XXXXX
```

Returns complete batch data including:
- Agricultural input
- Environmental conditions
- Contamination risks
- Safety score
- Prediction history
- Traceability path

---

## UI Navigation

### Agricultural Analysis Workflow

```
1. Click "🌾 Agricultural Analysis" tab
   ↓
2. Fill out Agricultural Form
   - Batch ID (auto-generated)
   - Crop type
   - Pesticide/fertilizer info
   - Irrigation source
   - Farm location
   - Environmental data
   ↓
3. Submit Form → Batch created
   ↓
4. View Contamination Risk Display
   - Switch between tabs: Overview, Chemical, Biological, Environmental, Safety
   - Review risk cards with scores
   - Check harvest safety status
   ↓
5. Review Prevention Recommendations
   - Sort by: Priority, Category, Impact
   - Read actionable recommendations
   - Check implementation guide
   ↓
6. Track Batch Traceability
   - Use Batch ID to track through supply chain
```

### Traditional Mode

```
1. Click "🍎 Traditional Analyzer" tab
   ↓
2. Use existing features:
   - Image upload
   - Risk predictor
   - Batch upload
   - Scan history
   - Statistics
```

---

## Common Issues & Solutions

### Issue: "Models not found" error on startup
```
ERROR: Models not loaded yet. Train models first.
```

**Solution:**
```bash
# Navigate to models directory
cd models

# Train image classifier (takes 5-10 minutes)
python train_image_classifier.py

# Train risk predictor (takes 1-2 minutes)
python train_risk_predictor.py

# Models will be saved to: ../backend/../models/saved_models/
```

### Issue: Database connection error
```
ERROR: Could not connect to database
```

**Solutions:**
1. Verify SQLite file exists: `backend/safefood.db`
2. Check file permissions: `chmod 644 safefood.db`
3. Reset database:
   ```bash
   rm safefood.db
   python app.py  # Will recreate
   ```

### Issue: CORS errors when frontend calls backend
```
ERROR: Access to XMLHttpRequest blocked by CORS policy
```

**Solution:**
1. Ensure backend is running on port 5000
2. Check CORS is enabled in `app.py`:
   ```python
   CORS(app)  # Should be present
   ```
3. Update frontend .env if backend is on different host:
   ```bash
   # .env
   REACT_APP_API_URL=http://your-backend-host:5000
   ```

### Issue: "Batch ID already exists"
```
ERROR: Batch ID BATCH-XXXXX already exists
```

**Solution:**
- Each agricultural submission must have unique batch ID
- System auto-generates unique IDs - don't reuse them
- Click "Generate New" button in form to get new ID

---

## Environment Variables

### Frontend (.env)
```bash
# .env in frontend/
REACT_APP_API_URL=http://localhost:5000
```

### Backend (.env)
```bash
# .env in backend/
DATABASE_URL=sqlite:///safefood.db
# or
DATABASE_URL=postgresql://user:password@localhost/safefood
```

---

## Database Schema Inspection

### View all tables

```python
python
>>> from app import db, app
>>> with app.app_context():
>>>     from models import AgriculturalInput, EnvironmentalData, ContaminationRisk, FoodSafetyScore, PredictionHistory
>>>     print(db.inspect(db.engine).get_table_names())
```

### Query example: All batches with high risk

```python
python
>>> from app import db, app
>>> from models import AgriculturalInput, ContaminationRisk
>>> with app.app_context():
>>>     high_risk = ContaminationRisk.query.filter(ContaminationRisk.risk_score > 70).all()
>>>     for risk in high_risk:
>>>         print(f"Batch {risk.batch_id}: {risk.risk_level} {risk.contamination_type}")
```

---

## Production Deployment

### Environment Setup
```bash
# Set Flask to production
export FLASK_ENV=production
export FLASK_DEBUG=0

# Use PostgreSQL instead of SQLite
export DATABASE_URL=postgresql://user:pass@host/db

# Secret key for sessions
export SECRET_KEY=your-secret-key-here
```

### Run Production Server
```bash
# Option A: Gunicorn (recommended)
gunicorn -w 4 -b 0.0.0.0:5000 app:app

# Option B: Flask built-in (not recommended for production)
python app.py
```

---

## Monitoring & Logging

### Enable detailed logging

```python
# Add to app.py
import logging
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
```

### Check logs for errors

```bash
# View Flask logs
tail -f flask.log

# Check database logs
tail -f safefood.db
```

---

## Performance Optimization

### Database Indexing
```python
# Batch ID lookup is optimized (indexed)
AgriculturalInput.query.filter_by(batch_id=batch_id).first()  # Fast

# Add more indexes as needed in models.py
batch_id = db.Column(db.String(50), index=True)
```

### API Response Caching
```python
# Consider caching risk calculations for same batch
# if recalculated within short timeframe
```

---

## Troubleshooting Checklist

- [ ] Backend running on port 5000
- [ ] Frontend running on port 3000
- [ ] API health check passes: `GET /health`
- [ ] Database tables created: `safefood.db` exists
- [ ] Models trained and present in `./models/saved_models/`
- [ ] No CORS errors in browser console
- [ ] Agricultural form submits without errors
- [ ] Risk calculation completes successfully
- [ ] Safety score generates recommendations
- [ ] Batch traceability shows all data

---

## Next Steps

1. **Test all features** using the checklist above
2. **Train ML models** if not already done
3. **Load sample data** using the API examples
4. **Review recommendations** generated for sample batches
5. **Customize thresholds** in `config.py` as needed
6. **Integrate with your system** or supply chain partners

---

## Documentation Links

- [API Documentation](./API_DOCUMENTATION.md) - Complete endpoint reference
- [Project Structure](./PROJECT_STRUCTURE.md) - File organization
- [Upgrade Guide](./UPGRADE_GUIDE.md) - Feature details
- [Project Completion](./PROJECT_COMPLETION.md) - Status and timeline

---

**Version:** 2.0.0  
**Last Updated:** April 15, 2026
