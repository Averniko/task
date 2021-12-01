from django.db import models
from django.contrib.sessions.models import Session


class Url(models.Model):
    subpart = models.CharField(max_length=128, null=False, blank=False)
    redirect = models.CharField(max_length=512, null=False, blank=False)
    session_key = models.CharField(max_length=128, null=False, blank=False)
