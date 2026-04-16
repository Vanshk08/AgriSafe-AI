# Vercel Configuration Files

This directory contains the serverless function configuration for Vercel deployment.

## Files

- **`index.py`** - Main Flask application exported as Vercel serverless function
- **`requirements.txt`** - Python dependencies for the API

## How It Works

1. When deployed to Vercel, the `index.py` file is automatically converted into a serverless function
2. All requests to `/api/*` routes are handled by this function
3. Frontend assets are served from `frontend/build`
4. Database connections use PostgreSQL (configured via `DATABASE_URL` environment variable)

## Setup Instructions

### 1. Set Environment Variables on Vercel

Go to your Vercel project settings and add these environment variables:

- **`DATABASE_URL`** - PostgreSQL connection string (from Neon, Supabase, etc.)
  - Example: `postgresql://user:password@host:5432/dbname`
- **`REACT_APP_API_URL`** - Your Vercel deployment URL
  - Example: `https://your-project.vercel.app`

### 2. Deploy

Simply push to GitHub and Vercel will automatically:
1. Install dependencies from `api/requirements.txt`
2. Build React frontend
3. Deploy the serverless API
4. Serve everything on your Vercel domain

## Testing Locally

To test the API locally before deploying:

```bash
# Install dependencies
pip install -r api/requirements.txt

# Run the Flask app
python -c "from api.index import app; app.run(debug=True)"
```

Then visit `http://localhost:5000/api/health`

## Troubleshooting

### 404 Errors
- Make sure all routes start with `/api/`
- Check that frontend build was completed
- Verify environment variables are set

### Database Connection Issues
- Verify `DATABASE_URL` is correctly set in Vercel settings
- Check that your PostgreSQL database is accessible
- Ensure the database URL includes the correct credentials

### Model Loading Errors
- Models are optional - the API will work without them but with limited functionality
- To enable ML features, upload model files to `/models/saved_models/`
