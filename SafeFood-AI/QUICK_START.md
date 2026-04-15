# AgriSafe AI - Quick Reference Guide

## 🚀 Quick Start Commands

### Terminal 1: Train Models
```bash
cd models
python train_image_classifier.py
python train_risk_predictor.py
```

### Terminal 2: Run Backend
```bash
cd backend
python app.py
# Backend will run on http://localhost:5000
```

### Terminal 3: Run Frontend
```bash
cd frontend
npm start
# App will open at http://localhost:3000
```

## 📝 Common Commands

### Backend
```bash
# Activate virtual environment (Windows)
backend_venv\Scripts\activate

# Activate virtual environment (macOS/Linux)
source backend_venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Run Flask server
python app.py

# Run with specific host/port
python -c "from app import app; app.run(host='0.0.0.0', port=5000, debug=True)"
```

### Frontend
```bash
# Install dependencies
npm install

# Start development server
npm start

# Build for production
npm run build

# Run tests
npm test
```

### Models
```bash
# Train image classifier (5-10 minutes)
python train_image_classifier.py

# Train risk predictor (1-2 minutes)
python train_risk_predictor.py

# View training output
# Models saved in: models/saved_models/
```

## 🐛 Debugging

### Check Backend Health
```bash
curl http://localhost:5000/health
```

### View Backend Logs
```bash
# In backend terminal, look for error messages
# Enable debug mode in Flask for more details
```

### Check Frontend Console
```bash
# Open browser DevTools (F12)
# Check Console tab for errors
# Check Network tab for API calls
```

## 📦 File Locations

```
models/saved_models/
├── food_classifier.h5       # Image classification model (50MB)
├── risk_predictor.pkl       # Risk prediction model (1MB)

dataset/images/
├── fresh/                   # Fresh food images (100 images)
├── spoiled/                 # Spoiled food images (100 images)

frontend/
├── src/components/          # React components
├── public/                  # Static files
└── node_modules/            # Dependencies (not in repo)

backend/
├── uploads/                 # Temporary image uploads
└── __pycache__/            # Python cache (not in repo)
```

## 🔗 URLs

- **Frontend**: http://localhost:3000
- **Backend**: http://localhost:5000
- **Health Check**: http://localhost:5000/health
- **API Docs**: See README.md

## 💡 Tips

1. **Keep terminals open**: You need all 3 running simultaneously
2. **Check API status**: Look for success badge in top right
3. **Clear browser cache**: If UI looks wrong, hard refresh (Ctrl+F5)
4. **Kill hung processes**: Use `taskkill /PID <PID> /F` (Windows) or `kill -9 <PID>` (Mac/Linux)
5. **Monitor memory**: Large models can use significant RAM
6. **Test APIs directly**: Use curl or Postman to test endpoints

## 🆘 Emergency Help

### Reset Everything
```bash
# Stop all servers (Ctrl+C)
# Delete virtual environment
rm -rf backend_venv  # macOS/Linux
rmdir /s backend_venv  # Windows

# Delete node_modules
rm -rf frontend/node_modules  # macOS/Linux
rmdir /s frontend\node_modules  # Windows

# Run setup script again
# Windows: setup.bat
# macOS/Linux: bash setup.sh
```

### Port Conflicts
```bash
# Windows - Find process on port 5000
netstat -ano | findstr :5000
taskkill /PID <PID> /F

# macOS/Linux - Find process on port 5000
lsof -i :5000
kill -9 <PID>
kill -9 $(lsof -t -i :5000)  # One-liner
```

## 📊 Project Status

- ✅ Backend API - Complete
- ✅ Frontend UI - Complete
- ✅ Image Classification Model - Ready
- ✅ Risk Prediction Model - Ready
- ✅ Documentation - Complete
- ✅ Setup Scripts - Complete

---

**Last Updated**: 2024
**Version**: 1.0.0
