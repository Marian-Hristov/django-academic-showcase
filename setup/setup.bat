@echo off
rem set machine specific config
call config.bat

rem activate venv
if exist ..\.venv\ (
    ..\.venv\Scripts\activate
) else (
    virtualenv ..\.venv
    ..\.venv\Scripts\activate
    pip install -r ..\requirements.txt
)
