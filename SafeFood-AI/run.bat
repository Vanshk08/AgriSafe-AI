@echo off
REM AgriSafe AI - Startup Script for Windows
REM Automatically sets up and runs the entire application

echo.
echo ========================================
echo AgriSafe AI - Startup Script
echo ========================================
echo.

REM Check if Python is installed
python --version >nul 2>&1
if errorlevel 1 (
    echo ERROR: Python is not installed or not in PATH
    pause
    exit /b 1
)

REM Check if Node.js is installed
node --version >nul 2>&1
if errorlevel 1 (
    echo ERROR: Node.js is not installed or not in PATH
    pause
    exit /b 1
)

echo Prerequisites found
echo.

REM Store current directory
set PROJECT_ROOT=%cd%

echo Setting up Backend...
cd backend

REM Create virtual environment if it doesn't exist
if not exist "..\backend_venv\" (
    echo Creating virtual environment...
    python -m venv ..\backend_venv
)

REM Activate virtual environment
call ..\backend_venv\Scripts\activate.bat

REM Install dependencies
echo Installing backend dependencies...
pip install -q -r requirements.txt >nul 2>&1

REM Start backend
echo Starting Flask backend on port 5000...
title AgriSafe AI - Backend
start cmd /k python app.py

timeout /t 3 /nobreak
echo Backend started
echo.

REM Navigate to frontend
cd ..\frontend

REM Install npm dependencies if needed
if not exist "node_modules\" (
    echo Installing frontend dependencies...
    call npm install --silent
)

REM Start frontend
echo Starting React frontend on port 3000...
title AgriSafe AI - Frontend
call npm start

echo.
echo ========================================
echo AgriSafe AI is Running!
echo ========================================
echo.
echo Frontend:  http://localhost:3000
echo Backend:   http://localhost:5000
echo.
echo Close this window to stop the application
pause
