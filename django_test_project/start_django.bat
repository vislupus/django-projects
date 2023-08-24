@echo off
echo http://127.0.0.1:8000
start chrome http://127.0.0.1:8000
python manage.py runserver %*
pause
