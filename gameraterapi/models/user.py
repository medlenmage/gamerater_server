from django.db import models
from django.conf import settings
from django.db.models.deletion import CASCADE

class User(models.Model):
    password = models.CharField(max_length=25)
    last_login = 
    is_superuser =
    username =
    first_name =
    last_name =
    email =
    is_staff =
    is_active =
    date_joined = 
    group =
    user_permissions =