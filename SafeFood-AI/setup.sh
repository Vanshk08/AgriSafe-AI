#!/bin/bash

# AgriSafe AI Setup Script for macOS/Linux

echo ""
echo "========================================"
echo "AgriSafe AI - Setup Script"
echo "========================================"
echo ""

# Check Python installation
if ! command -v python3 &> /dev/null; then
    echo "ERROR: Python 3 is not installed"
    echo "Please install Python 3.8+ from https://www.python.org/"
    exit 1
fi

# Check Node.js installation
if ! command -v node &> /dev/null; then
    echo "ERROR: Node.js is not installed"
    echo "Please install Node.js from https://nodejs.org/"
    exit 1
fi

echo "✓ Python and Node.js detected"
echo ""

# Create virtual environment
echo "Step 1: Creating Python virtual environment..."
python3 -m venv backend_venv
source backend_venv/bin/activate
echo "✓ Virtual environment created"

# Install backend dependencies
echo ""
echo "Step 2: Installing backend dependencies..."
cd backend
pip install -r requirements.txt
cd ..
echo "✓ Backend dependencies installed"

# Install model training dependencies
echo ""
echo "Step 3: Installing model training dependencies..."
cd models
pip install -r requirements.txt
cd ..
echo "✓ Model training dependencies installed"

# Install frontend dependencies
echo ""
echo "Step 4: Installing frontend dependencies..."
cd frontend
npm install
cd ..
echo "✓ Frontend dependencies installed"

echo ""
echo "========================================"
echo "Setup Complete!"
echo "========================================"
echo ""
echo "Next steps:"
echo "1. Activate virtual environment:"
echo "   source backend_venv/bin/activate"
echo ""
echo "2. Train AI Models:"
echo "   cd models"
echo "   python train_image_classifier.py"
echo "   python train_risk_predictor.py"
echo ""
echo "3. Start Backend Server (in terminal 1):"
echo "   cd backend"
echo "   python app.py"
echo ""
echo "4. Start Frontend (in terminal 2):"
echo "   cd frontend"
echo "   npm start"
echo ""
echo "For detailed instructions, see README.md"
echo ""
