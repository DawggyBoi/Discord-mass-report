@echo off
title Report Bot Launcher - Developed By acceleration.back
color 0A

echo Installing dependencies...
pip install -r requirements.txt

echo.
echo Starting the bot...
python start.py

echo.
echo Script finished. Press any key to exit.
pause >nul
