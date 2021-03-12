from django.db import models
from simple_history import register
from django.contrib.auth.models import User, Group


register(User)
register(Group)

# Create your models here.


class User(models.Model):
    username = models.CharField(max_length=16)
    avatar = models.FileField(upload_to='avatar')
