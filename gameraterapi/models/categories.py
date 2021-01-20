from django.db import models
from django.conf import settings

class Category(models.Model):
    name = models.CharField(max_length=75)
