@echo on
SETLOCAL ENABLEEXTENSIONS

echo ========================================
echo [INFO] Проверка наличия Python...
echo ========================================

where python >nul 2>&1
IF %ERRORLEVEL% NEQ 0 (
    echo [INFO] Python не найден. Скачиваю установщик...

    powershell -Command "Start-BitsTransfer -Source https://www.python.org/ftp/python/3.10.11/python-3.10.11-amd64.exe -Destination python-installer.exe"

    echo [INFO] Устанавливаю Python 3.10.11 (может занять 1-2 минуты)...
    start /wait python-installer.exe /quiet InstallAllUsers=1 PrependPath=1 Include_test=0

    del python-installer.exe

    echo [INFO] Python успешно установлен и добавлен в PATH.
) ELSE (
    echo [INFO] У вас уже установлен Python:
    python --version
)

echo ========================================
echo [INFO] Устанавливаю/обновляю pip...
echo ========================================
python -m ensurepip --upgrade
python -m pip install --upgrade pip

echo ========================================
echo [INFO] Устанавливаю pyarrow...
echo ========================================
python -m pip install pyarrow

echo.
echo ========================================
echo [OK] Установка завершена. Теперь вы можете запускать программу.
echo ========================================
pause
