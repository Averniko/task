from celery import app
from django.contrib.sessions.models import Session
from datetime import datetime

from backend.settings import r
from urls.models import Url


@app.shared_task
def clean():
    dt = datetime.now()
    ids = Session.objects.filter(expire_date__lt=dt).values_list('pk', flat=True)
    r.delete(list(ids.all()))
    Url.objects.filter(session_key__in=ids).delete()

