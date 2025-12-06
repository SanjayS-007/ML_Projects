@echo off
REM Simplest Jupyter Lab Starter - Shows URL to copy
REM Use this if START_JUPYTER.bat has permission issues

cd /d D:\ML_Projects
call ml_env\Scripts\activate.bat

echo.
echo ========================================
echo   Starting Jupyter Lab
echo ========================================
echo.
echo Look for the URL below that starts with:
echo http://localhost:8888/lab?token=...
echo.
echo Copy and paste it into your browser!
echo.
echo ========================================
echo.

jupyter lab --no-browser

pause
