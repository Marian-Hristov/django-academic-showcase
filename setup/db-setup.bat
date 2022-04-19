@echo off
rem Call config.bat
call config.bat

rem Add the database
psql -U postgres -f database-setup.sql
rem Add the models to the DB
python ..\manage.py makemigrations
python ..\manage.py migrate
python ..\manage.py createsuperuser