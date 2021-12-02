from celery import app


@app.shared_task
def clean():
    pass
