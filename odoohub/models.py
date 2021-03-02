from django.db import models

# Create your models here.


from django.db import models
from viewflow.models import Process


class HelloWorldProcess(Process):
    text = models.CharField(max_length=150)
    approved = models.BooleanField(default=False)


class QingJiaProcess(Process):
    text = models.CharField(max_length=150)
    days = models.CharField(max_length=150)
    demo = models.CharField(max_length=150)
    submit = models.BooleanField(default=False)
    submit_note = models.CharField(max_length=150)
    approved = models.BooleanField(default=False)
