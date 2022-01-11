
python -m venv venv
.\venv\Scripts\activate.bat
python -m pip install -r requirements.txt

@REM Start uvicorn server
@REM uvicorn --app-dir src agent:app --reload 



