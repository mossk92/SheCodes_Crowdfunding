from django.contrib.auth.models import AbstractUser
from django.db import models
from datetime import date

# Create your models here.
class CustomUser(AbstractUser):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    bio = models.TextField(default='')
    date_created = models.DateField(default=date.today)
    pass
    def __str__(self):
        #display as just the username (no {})
        return self.username