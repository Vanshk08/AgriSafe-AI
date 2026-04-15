# 🚀 Deploy AgriSafe AI to Vercel

Complete guide to host your AgriSafe AI application on Vercel.

## 📋 Prerequisites

1. **Vercel Account** - Sign up at https://vercel.com
2. **GitHub Account** - Link your repo to Vercel
3. **Cloud Database** - PostgreSQL or MongoDB (SQLite won't work on Vercel)

---

## 🔄 Architecture Overview

```
Your Machine (Development)
  ├── Frontend (React) → Vercel Edge Network
  ├── Backend (Flask) → Vercel Functions
  └── Database → PostgreSQL/MongoDB (External)
```

---

## 📦 Step 1: Prepare for Deployment

### 1.1 Create `vercel.json` in project root

```json
{
  "buildCommand": "npm run build --prefix frontend",
  "outputDirectory": "frontend/build",
  "installCommand": "npm install --prefix frontend && pip install -r requirements.txt",
  "env": {
    "REACT_APP_API_URL": "@api_url",
    "DATABASE_URL": "@database_url",
    "SECRET_KEY": "@secret_key"
  }
}
```

### 1.2 Create Backend Directory for Vercel Functions

```bash
mkdir -p api
```

### 1.3 Create `api/requirements.txt`

```
Flask==3.0.0
Flask-CORS==4.0.0
Flask-SQLAlchemy==3.1.1
python-dotenv==1.0.0
scikit-learn==1.3.0
tensorflow==2.13.0
Pillow==9.5.0
gunicorn==21.2.0
```

### 1.4 Create `api/index.py` (Vercel Function)

```python
"""
AgriSafe AI Backend - Vercel Function
Converts Flask app to Vercel serverless function
"""
import sys
import os
from pathlib import Path

# Add parent directory to path
sys.path.insert(0, str(Path(__file__).parent.parent / 'backend'))

from flask import Flask, request, jsonify
from flask_cors import CORS
import os

# Import from backend
from backend.config import (
    SQLALCHEMY_DATABASE_URI, SQLALCHEMY_TRACK_MODIFICATIONS,
    ALLOWED_EXTENSIONS, MAX_FILE_SIZE, FOOD_TYPES
)

app = Flask(__name__)
CORS(app)

# Configuration
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL', 'sqlite:///agrisafe.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['MAX_CONTENT_LENGTH'] = MAX_FILE_SIZE

# Import models and routes
from backend.models import db
from backend.app import (
    get_batch_details, predict_image_endpoint, predict_risk_endpoint,
    submit_agricultural_input, health_check
)

db.init_app(app)

# Routes
@app.before_request
def create_tables():
    """Create database tables if they don't exist"""
    with app.app_context():
        db.create_all()

@app.route('/health', methods=['GET'])
def health():
    return health_check()

@app.route('/food-types', methods=['GET'])
def food_types():
    return jsonify({'food_types': FOOD_TYPES})

@app.route('/predict-image', methods=['POST'])
def predict_image():
    return predict_image_endpoint()

@app.route('/predict-risk', methods=['POST'])
def predict_risk():
    return predict_risk_endpoint()

@app.route('/agricultural-input', methods=['POST'])
def agricultural_input():
    return submit_agricultural_input()

@app.route('/batch/<batch_id>', methods=['GET'])
def batch_details(batch_id):
    return get_batch_details(batch_id)

# Vercel handler
from werkzeug.serving import WSGIRequestHandler

def handler(request):
    with app.request_context(request.environ):
        return app.full_dispatch_request()
```

---

## 🗄️ Step 2: Set Up Cloud Database

### Option A: PostgreSQL (Recommended)

**Using Supabase (Free tier available):**

1. Go to https://supabase.com
2. Sign up and create a new project
3. Copy the PostgreSQL connection string
4. Format: `postgresql://user:password@host:port/database`

**Using Vercel Postgres:**

1. Create a Vercel account
2. Link PostgreSQL in Vercel Dashboard → Storage → Create PostgreSQL database
3. Copy connection string

### Option B: MongoDB

**Using MongoDB Atlas:**

1. Go to https://mongodb.com/cloud/atlas
2. Create a free cluster
3. Copy the connection string
4. Format: `mongodb+srv://user:password@cluster.mongodb.net/database`

---

## 🔐 Step 3: Environment Variables on Vercel

1. Go to **Vercel Dashboard** → Your Project → **Settings** → **Environment Variables**
2. Add these variables:

```
REACT_APP_API_URL: https://your-project.vercel.app/api
DATABASE_URL: postgresql://user:password@host:port/database
SECRET_KEY: your-random-secret-key-here
```

---

## 📤 Step 4: Deploy Frontend

### 4.1 Push to GitHub

```bash
cd SafeFood-AI
git add .
git commit -m "Prepare for Vercel deployment"
git push origin main
```

### 4.2 Connect to Vercel

1. Go to https://vercel.com/new
2. Click **Import Project**
3. Select your GitHub repository
4. Configure:
   - **Framework Preset**: Next.js (if using) or None
   - **Root Directory**: `./frontend`
   - **Build Command**: `npm run build`
   - **Output Directory**: `build`

### 4.3 Add Environment Variables

In Vercel dashboard:
```
REACT_APP_API_URL=https://your-project.vercel.app/api
```

### 4.4 Deploy

Click **Deploy** and wait for completion.

---

## 🔌 Step 5: Deploy Backend Functions

### 5.1 Create API Routes Structure

```
api/
├── index.py (main handler)
├── requirements.txt
├── health.py (health check)
├── predict.py (predictions)
└── agricultural.py (agricultural data)
```

### 5.2 Create `api/health.py`

```python
from flask import jsonify
import os

def health_check():
    return jsonify({
        "status": "healthy",
        "database": "connected",
        "models_loaded": True,
        "timestamp": "2026-04-15"
    }), 200
```

### 5.3 Push Changes

```bash
git add api/
git commit -m "Add Vercel serverless functions"
git push origin main
```

Vercel will automatically detect the `api/` directory and deploy functions.

---

## 🔗 Step 6: Update Frontend API URL

After deployment, update frontend environment:

1. Go to Vercel Dashboard
2. Project → Settings → Environment Variables
3. Update `REACT_APP_API_URL` to your Vercel API endpoint

---

## 📊 Step 7: Database Migration

### Migrate from SQLite to PostgreSQL

```sql
-- Create tables on PostgreSQL
-- (Vercel will handle this with SQLAlchemy)

-- Or use migration tools:
# pip install alembic
# alembic init migrations
# alembic upgrade head
```

---

## ✅ Verification Checklist

- [ ] Frontend builds and deploys successfully
- [ ] Frontend accessible at `https://your-project.vercel.app`
- [ ] Backend API functions deployed
- [ ] API health check: `https://your-project.vercel.app/api/health`
- [ ] Database connected and accessible
- [ ] Environment variables configured
- [ ] Frontend can reach backend API
- [ ] Image upload works
- [ ] Predictions functioning

---

## 🐛 Troubleshooting

### Issue: `DATABASE_URL not found`

**Solution:**
```python
# In config.py
import os
DATABASE_URL = os.getenv('DATABASE_URL')
if not DATABASE_URL:
    raise ValueError("DATABASE_URL environment variable is required")
```

### Issue: Module imports fail

**Solution:**
- Ensure relative imports in `api/index.py`
- Add `__init__.py` files in all directories

### Issue: Models can't load

**Solution:**
```python
# Use absolute paths
MODEL_PATH = '/tmp/model.pkl'  # Vercel's /tmp directory
```

### Issue: Cold starts slow

**Solution:**
- Use lightweight models
- Cache model in memory
- Use Edge Functions for faster response

---

## 🚀 Advanced: Use Vercel Edge Functions

For faster CORS and API handling:

```bash
# Create serverless function
mkdir -p api/middleware
```

Create `api/middleware/cors.py`:

```python
from flask_cors import CORS

def setup_cors(app):
    CORS(app, 
        origins=["https://your-project.vercel.app"],
        methods=["GET", "POST", "OPTIONS"],
        allow_headers=["Content-Type"]
    )
```

---

## 📚 Useful Links

- **Vercel Docs**: https://vercel.com/docs
- **Vercel Functions**: https://vercel.com/docs/functions/serverless-functions
- **Flask on Vercel**: https://vercel.com/docs/samples/flask
- **Supabase**: https://supabase.com
- **MongoDB Atlas**: https://mongodb.com/cloud/atlas

---

## 📞 Next Steps

1. Create Vercel account and link GitHub
2. Set up PostgreSQL database (Supabase recommended)
3. Add environment variables to Vercel
4. Deploy frontend
5. Set up backend functions
6. Test API endpoints
7. Monitor logs in Vercel Dashboard

**Your AgriSafe AI will be live at: `https://your-project.vercel.app`** 🎉

