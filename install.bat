@echo off
echo Instalando Toolbar para Windows...

:: Instala Python caso não esteja instalado
where python >nul 2>nul || (
    echo Python não encontrado. Baixando Python...
    powershell -Command "Start-Process 'https://www.python.org/ftp/python/3.10.0/python-3.10.0-amd64.exe' -Wait"
)

:: Instalar dependências
pip install -r requirements.txt

:: Rodar o programa
python toolbar/app.py
