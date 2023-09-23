@echo off
setlocal EnableDelayedExpansion

@REM start ..\venv\Scripts\activate.bat

echo %~dp0

start chrome http://127.0.0.1:8000
python manage.py runserver %*

pause
