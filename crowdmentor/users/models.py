from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
class CustomUser(AbstractUser):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    bio = models.TextField()
    date_created = models.DateTimeField()
    pass
    def __str__(self):
        #display as just the username (no {})
        return self.username