@echo off
REM AgriSafe AI - Supabase Setup Helper for Windows

echo.
echo ========================================
echo AgriSafe AI - Supabase Configuration
echo ========================================
echo.

echo Step 1: Get your Supabase connection string
echo Go to: https://supabase.com/dashboard
echo Navigate to: Settings ^>= Database ^>= Connection String
echo.

set /p CONNECTION_STRING="Enter your Supabase PostgreSQL connection string: "

REM Validate connection string
echo.
echo Testing connection string...

if not "%CONNECTION_STRING:postgresql://=%"=="%CONNECTION_STRING%" (
    echo Valid PostgreSQL connection string
) else (
    echo ERROR: Invalid connection string (must start with postgresql://)
    pause
    exit /b 1
)

REM Update backend .env
echo.
echo Updating backend\.env...

REM Use PowerShell to update file (more reliable)
powershell -Command ^
    "$content = Get-Content 'backend\.env'; " ^
    "$content = $content -replace '^DATABASE_URL=.*', 'DATABASE_URL=%CONNECTION_STRING%'; " ^
    "Set-Content 'backend\.env' $content"

if %ERRORLEVEL% EQU 0 (
    echo Updated backend\.env successfully
) else (
    echo Could not update backend\.env (try manually)
)

REM Test connection
echo.
echo Testing database connection...

cd backend
python -c "import os; from sqlalchemy import create_engine, text; engine = create_engine(os.getenv('DATABASE_URL')); conn = engine.connect(); print('✅ Connected to Supabase!'); conn.close()"

if %ERRORLEVEL% EQU 0 (
    echo.
    echo Success! Supabase is configured.
    echo.
    echo Next steps:
    echo 1. Start backend:  python app.py
    echo 2. Start frontend: npm start
    echo 3. Check database: https://supabase.com/dashboard
) else (
    echo Connection test failed. Please check your credentials.
)

pause
