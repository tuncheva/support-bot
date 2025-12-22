@echo off
setlocal

REM Ensure we run with the project virtualenv interpreter so dependencies (Flask, etc.) are available.
echo Starting Flask web app (webapp\app.py)

IF EXIST ".venv\Scripts\python.exe" (
  set "PYTHONPATH=%CD%\src"
  ".venv\Scripts\python.exe" -m webapp.app
) ELSE (
  echo WARNING: .venv not found. Falling back to system python.
  set "PYTHONPATH=%CD%\src"
  python -m webapp.app
)

pause
