@echo off

call %~dp0telegram_bot\venv\Scripts\activate

cd %~dp0telegram_bot

set TOKEN=6179599258:AAEBenfmjNmpoqPgWNojTERvm9C1obQJGec

python bot_telegram.py

pause