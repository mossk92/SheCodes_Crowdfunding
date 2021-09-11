from django.db import models

# Create your models here.
class Project(models.Model):
     title = models.CharField(max_length=200)
     description = models.TextField()
     category = models.CharField(max_length=200)
     location = models.CharField(max_length=200)
     goal = models.IntegerField()
     image = models.URLField()
     is_open = models.BooleanField()
     date_created = models.DateTimeField()
     owner = models.CharField(max_length=200)