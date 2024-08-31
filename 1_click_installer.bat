@echo off
REM Change to the directory of the batch file
cd /d "%~dp0"

REM Create virtual environment using python
python -m venv venv

REM activate virtual environment
call venv\scripts\activate

REM Install dependencies
pip install -r DiffSynth_requirements_windows

REM Download models
python download_models.py