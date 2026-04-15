#!/bin/bash

# AgriSafe AI - Startup Script for macOS/Linux
# Automatically sets up and runs the entire application

set -e  # Exit on error

echo "🚀 AgriSafe AI - Startup Script"
echo "================================"
echo ""

# Check if Python is installed
if ! command -v python3 &> /dev/null; then
    echo "❌ Python 3 is not installed. Please install Python first."
    exit 1
fi

# Check if Node.js is installed
if ! command -v node &> /dev/null; then
    echo "❌ Node.js is not installed. Please install Node.js first."
    exit 1
fi

echo "✅ Prerequisites found"
echo ""

# Navigate to project root
PROJECT_ROOT=$(dirname "$0")
cd "$PROJECT_ROOT"

echo "📦 Setting up Backend..."
cd backend

# Create virtual environment if it doesn't exist
if [ ! -d "../backend_venv" ]; then
    echo "🔧 Creating virtual environment..."
    python3 -m venv ../backend_venv
fi

# Activate virtual environment
source ../backend_venv/bin/activate

# Install dependencies
echo "📥 Installing backend dependencies..."
pip install -q -r requirements.txt

# Start backend in background
echo "🎯 Starting Flask backend on port 5000..."
python app.py &
BACKEND_PID=$!

echo "✅ Backend started (PID: $BACKEND_PID)"
echo ""

# Navigate to frontend
cd ../frontend

# Install npm dependencies if needed
if [ ! -d "node_modules" ]; then
    echo "📥 Installing frontend dependencies..."
    npm install --quiet
fi

# Start frontend
echo "🎨 Starting React frontend on port 3000..."
npm start &
FRONTEND_PID=$!

echo "✅ Frontend started (PID: $FRONTEND_PID)"
echo ""

echo "================================"
echo "🎉 AgriSafe AI is Running!"
echo "================================"
echo ""
echo "📍 Frontend:  http://localhost:3000"
echo "📍 Backend:   http://localhost:5000"
echo ""
echo "Press Ctrl+C to stop both services"
echo ""

# Wait for background processes
wait
