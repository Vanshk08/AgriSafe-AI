#!/bin/bash

# AgriSafe AI - Supabase Setup Helper
# This script helps you configure Supabase connection

echo "🚀 AgriSafe AI - Supabase Configuration"
echo "======================================"
echo ""

# Get Supabase connection string
echo "📋 Step 1: Get your Supabase connection string"
echo "Go to: https://supabase.com/dashboard"
echo "Navigate to: Settings → Database → Connection String"
echo ""

read -p "Enter your Supabase PostgreSQL connection string: " CONNECTION_STRING

# Extract components
echo ""
echo "🔍 Validating connection string..."

if [[ $CONNECTION_STRING == postgresql://* ]]; then
    echo "✅ Valid PostgreSQL connection string"
else
    echo "❌ Invalid connection string (must start with postgresql://)"
    exit 1
fi

# Update backend .env
echo ""
echo "📝 Updating backend/.env..."
sed -i "s|DATABASE_URL=.*|DATABASE_URL=$CONNECTION_STRING|" backend/.env

if [ $? -eq 0 ]; then
    echo "✅ backend/.env updated"
else
    echo "⚠️  Could not update backend/.env (try manually)"
fi

# Test connection
echo ""
echo "🧪 Testing database connection..."
cd backend

python3 << EOF
import os
import sys
from sqlalchemy import create_engine, text

try:
    engine = create_engine(os.getenv('DATABASE_URL'))
    with engine.connect() as conn:
        result = conn.execute(text("SELECT NOW()"))
        print("✅ Successfully connected to Supabase!")
        print(f"   Server time: {result.fetchone()[0]}")
except Exception as e:
    print(f"❌ Connection failed: {e}")
    sys.exit(1)
EOF

if [ $? -eq 0 ]; then
    echo ""
    echo "🎉 Supabase is configured!"
    echo ""
    echo "📚 Next steps:"
    echo "1. Start backend:  python app.py"
    echo "2. Start frontend: npm start"
    echo "3. Check database: Go to https://supabase.com/dashboard"
else
    echo "⚠️  Connection test failed. Please check your credentials."
fi
