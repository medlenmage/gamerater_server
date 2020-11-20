from django.db import models
from django.conf import settings

class Category(models.Model):
    name = models.CharField(mox_length=75)
