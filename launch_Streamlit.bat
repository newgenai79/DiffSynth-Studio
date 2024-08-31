@echo off
REM Change to the directory of the batch file
cd /d "%~dp0"

REM Activate the virtual environment
call venv\scripts\activate

REM Run app.py
python -m streamlit run apps/streamlit/DiffSynth_Studio.py