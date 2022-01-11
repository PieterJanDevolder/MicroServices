@REM Start fast api
start cmd /C uvicorn api:app --reload

@REM Start celery worker
@REM start cmd /C celery -A celery_worker.celery worker --loglevel=debug -P gevent
start cmd /C celery -A celery_worker.celery worker --loglevel=info -P eventlet

@REM Start celery flower (ui)
start cmd /c celery -A celery_worker.celery flower --port=5555