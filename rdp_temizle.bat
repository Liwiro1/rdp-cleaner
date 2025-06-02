@echo off
chcp 65001 >nul

REM Python kontrolü
python --version >nul 2>&1
if %errorlevel% neq 0 (
    exit /b 1
)

REM Dosya kontrolü
if not exist "rdp_temizle.py" (
    exit /b 1
)

REM Python scriptini sessiz modda çalıştır
python rdp_temizle.py --silent