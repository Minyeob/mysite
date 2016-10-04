from __future__ import unicode_literals
from django.db import models
import datetime

class User(models.Model):
    user_id = models.CharField(max_length=20)
    user_password = models.CharField(max_length=10)
    name = models.CharField(max_length=5)
    email = models.EmailField(max_length=70, null=True, unique=True, blank=True)
