@echo off
REM Change to the directory containing main.py
cd /d "C:\Users\user....."

REM Activate the Conda environment
call conda activate screenshot

REM Run the Python script
python main.py

REM Pause to keep the window open (optional)
pause