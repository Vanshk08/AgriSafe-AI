# 🚀 Setup Supabase PostgreSQL for AgriSafe AI

Complete guide to set up and connect Supabase PostgreSQL to your AgriSafe AI application.

---

## 📋 Step 1: Create Supabase Account

1. Go to **https://supabase.com**
2. Sign up with GitHub or Email
3. Create a new organization
4. Create a new project

**Settings:**
- **Project Name**: `agrisafe-ai`
- **Database Password**: Save this securely!
- **Region**: Choose closest to you (US East recommended)
- **Pricing**: Free tier is sufficient for development

---

## 🔑 Step 2: Get Connection String

1. Go to **Project Settings** → **Database**
2. Copy the connection string under "Connection string" → "URI"

**Format:**
```
postgresql://postgres:PASSWORD@host:5432/postgres
```

**Example:**
```
postgresql://postgres:mypassword123@db.xyz.supabase.co:5432/postgres
```

---

## 🔧 Step 3: Update Environment Variables

### Backend `.env` File

Update `backend/.env`:

```bash
# Database Configuration
DATABASE_URL=postgresql://postgres:YOUR_PASSWORD@YOUR_HOST:5432/postgres

# Flask Configuration
SECRET_KEY=your-super-secret-key-change-this
FLASK_ENV=development
```

**Replace:**
- `YOUR_PASSWORD` → Your Supabase database password
- `YOUR_HOST` → Your Supabase host (from connection string)

### Frontend `.env` File

Already configured in `frontend/.env`:
```
REACT_APP_API_URL=http://localhost:5000
```

---

## 📦 Step 4: Install PostgreSQL Client (Optional)

To test database connection locally:

```bash
# macOS
brew install postgresql

# Windows (with Homebrew)
choco install postgresql

# Linux
sudo apt-get install postgresql-client
```

---

## 🔌 Step 5: Test Connection

### Test from Terminal

```bash
# Replace with your connection string
psql "postgresql://postgres:PASSWORD@host:5432/postgres"

# If connected, you'll see:
# postgres=#
```

### Test from Python

```python
import os
from sqlalchemy import create_engine, text

DATABASE_URL = os.getenv('DATABASE_URL')
engine = create_engine(DATABASE_URL)

with engine.connect() as connection:
    result = connection.execute(text("SELECT 1"))
    print("✅ Connected to Supabase!")
```

Run:
```bash
cd backend
python -c "import os; from sqlalchemy import create_engine, text; engine = create_engine(os.getenv('DATABASE_URL')); print('✅ Connected!' if engine.connect() else '❌ Failed')"
```

---

## 🗂️ Step 6: Run Database Migrations

### Initialize Database Tables

When Flask app starts, it automatically creates tables via:

```python
@app.before_request
def create_tables():
    db.create_all()
```

Or manually:

```bash
cd backend
python -c "from app import app, db; app.app_context().push(); db.create_all(); print('✅ Tables created!')"
```

---

## ✅ Step 7: Verify in Supabase Dashboard

1. Go to **Supabase Dashboard** → Your Project
2. Click **SQL Editor** on left sidebar
3. Run this query:

```sql
SELECT table_name 
FROM information_schema.tables 
WHERE table_schema = 'public';
```

**Should show:**
- `agricultural_inputs`
- `environmental_data`
- `contamination_risks`
- `food_safety_scores`
- `prediction_history`

---

## 🚀 Step 8: Start Application with Supabase

### Backend

```bash
cd backend

# Activate virtual environment
# Windows
..\backend_venv\Scripts\activate
# macOS/Linux
source ../backend_venv/bin/activate

# Start Flask (will connect to Supabase)
python app.py
```

**Should show:**
```
INFO:__main__:Models loaded successfully
* Running on http://127.0.0.1:5000
```

### Frontend

```bash
cd frontend
npm start
```

---

## 📊 Step 9: Monitor Database in Supabase

### View Data

1. Go to **Supabase Dashboard** → **Table Editor**
2. Select any table to view data
3. Insert/View/Update records in real-time

### View Logs

```sql
-- Check recent data
SELECT * FROM agricultural_inputs ORDER BY created_at DESC LIMIT 10;
SELECT * FROM prediction_history ORDER BY created_at DESC LIMIT 10;
SELECT * FROM food_safety_scores ORDER BY calculated_at DESC LIMIT 10;
```

---

## 🔒 Security Best Practices

### 1. Use Row-Level Security (RLS)

```sql
-- Enable RLS
ALTER TABLE agricultural_inputs ENABLE ROW LEVEL SECURITY;

-- Allow all for development (NOT for production)
CREATE POLICY "Allow all for development"
ON agricultural_inputs
FOR ALL
USING (true);
```

### 2. Rotate Password Regularly

1. Supabase Dashboard → **Settings** → **Database**
2. Click **Reset Password**
3. Update `.env` file

### 3. Never Commit `.env`

Verify `.env` is in `.gitignore`:
```bash
cat .gitignore | grep ".env"
```

Should show:
```
.env
.env.local
```

---

## 🌐 Step 10: Deploy to Vercel with Supabase

### Set Environment Variable on Vercel

1. Go to **Vercel Dashboard** → Your Project
2. **Settings** → **Environment Variables**
3. Add:
   ```
   DATABASE_URL = postgresql://postgres:YOUR_PASSWORD@YOUR_HOST:5432/postgres
   REACT_APP_API_URL = https://your-project.vercel.app/api
   SECRET_KEY = your-production-secret-key
   ```

4. Redeploy

---

## 🐛 Troubleshooting

### Issue: `could not connect to server`

**Solution:**
- Check internet connection
- Verify password is correct
- Ensure project is not paused
- Check IP whitelist (Supabase allows all by default)

```bash
# Test connection
psql "postgresql://postgres:PASSWORD@host:5432/postgres" -c "SELECT 1"
```

### Issue: `no such table`

**Solution:**
```bash
# Recreate tables
cd backend
python -c "from app import app, db; app.app_context().push(); db.drop_all(); db.create_all()"
```

### Issue: `permission denied`

**Solution:**
```sql
-- Grant permissions
GRANT ALL PRIVILEGES ON ALL TABLES IN SCHEMA public TO postgres;
GRANT ALL PRIVILEGES ON ALL SEQUENCES IN SCHEMA public TO postgres;
```

---

## 📝 Configuration Files

### `backend/.env`
```env
DATABASE_URL=postgresql://postgres:PASSWORD@host:5432/postgres
SECRET_KEY=your-secret-key
FLASK_ENV=development
```

### `backend/config.py`
```python
import os

SQLALCHEMY_DATABASE_URI = os.getenv(
    'DATABASE_URL',
    'sqlite:///agrisafe.db'
)
SQLALCHEMY_TRACK_MODIFICATIONS = False
```

---

## ✨ Benefits of Supabase

✅ **Free Tier**: 500MB storage, perfect for development  
✅ **PostgreSQL**: Industry-standard database  
✅ **Real-time**: WebSocket support built-in  
✅ **Backups**: Daily automated backups  
✅ **Scalable**: Easy to upgrade when needed  
✅ **Dashboard**: Beautiful SQL editor and table viewer  

---

## 🔗 Useful Links

- **Supabase Docs**: https://supabase.com/docs
- **Connection Strings**: https://supabase.com/docs/guides/database/connecting-to-postgres
- **Row-Level Security**: https://supabase.com/docs/guides/auth/row-level-security
- **PostgreSQL Tutorial**: https://www.postgresql.org/docs/

---

## 📞 Next Steps

1. ✅ Create Supabase account
2. ✅ Get PostgreSQL connection string
3. ✅ Update `.env` file
4. ✅ Test connection
5. ✅ Start application
6. ✅ Verify tables in Supabase dashboard
7. ✅ Deploy to Vercel

**Your AgriSafe AI is now using Supabase PostgreSQL!** 🎉

