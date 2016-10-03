from __future__ import unicode_literals
from django.db import models
import datetime

class User(models.Model):
    user_id = models.CharField(maxlength=10)
    user_password = models.
