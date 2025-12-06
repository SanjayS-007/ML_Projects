@echo off
REM Jupyter Lab Starter - Avoids File Permission Errors
REM The --no-browser flag prevents the file:/// error

cd /d D:\ML_Projects
call ml_env\Scripts\activate.bat

echo.
echo ========================================
echo   Starting Jupyter Lab
echo ========================================
echo.
echo Look for the line that says:
echo   http://localhost:8888/lab?token=...
echo.
echo Copy that FULL URL and paste it in your browser!
echo.
echo ========================================
echo.

REM Start Jupyter WITHOUT auto-browser (this fixes the permission error)
jupyter lab --no-browser

pause
