@echo off
REM SafeFood AI Setup Script for Windows

echo.
echo ========================================
echo SafeFood AI - Setup Script
echo ========================================
echo.

REM Check Python installation
python --version >nul 2>&1
if errorlevel 1 (
    echo ERROR: Python is not installed or not in PATH
    echo Please install Python 3.8+ from https://www.python.org/
    pause
    exit /b 1
)

REM Check Node.js installation
node --version >nul 2>&1
if errorlevel 1 (
    echo ERROR: Node.js is not installed or not in PATH
    echo Please install Node.js from https://nodejs.org/
    pause
    exit /b 1
)

echo ✓ Python and Node.js detected
echo.

REM Create virtual environment
echo Step 1: Creating Python virtual environment...
python -m venv backend_venv
call backend_venv\Scripts\activate.bat
echo ✓ Virtual environment created

REM Install backend dependencies
echo.
echo Step 2: Installing backend dependencies...
cd backend
pip install -r requirements.txt
cd ..
echo ✓ Backend dependencies installed

REM Install model training dependencies
echo.
echo Step 3: Installing model training dependencies...
cd models
pip install -r requirements.txt
cd ..
echo ✓ Model training dependencies installed

REM Install frontend dependencies
echo.
echo Step 4: Installing frontend dependencies...
cd frontend
call npm install
cd ..
echo ✓ Frontend dependencies installed

echo.
echo ========================================
echo Setup Complete!
echo ========================================
echo.
echo Next steps:
echo 1. Train AI Models (in separate terminal):
echo    cd models
echo    python train_image_classifier.py
echo    python train_risk_predictor.py
echo.
echo 2. Start Backend Server:
echo    cd backend
echo    python app.py
echo.
echo 3. Start Frontend (in another terminal):
echo    cd frontend
echo    npm start
echo.
echo For detailed instructions, see README.md
echo.

pause
