from django.contrib.auth.models import AbstractUser
from django.db import models
from datetime import date
from rest_framework.authtoken.models import Token
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver

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

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)