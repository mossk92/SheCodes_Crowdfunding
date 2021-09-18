from django.contrib.auth import get_user_model
from django.db import models
from django.db.models import Sum

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
     owner = models.ForeignKey(
          get_user_model(),
          on_delete=models.CASCADE,
          related_name='owner_projects'
     )

     def pledge_total(self):
          return Pledge.objects.filter(project=self.id).aggregate(Sum('amount'))

class Pledge(models.Model):
     amount = models.IntegerField()
     comment = models.CharField(max_length=200)
     project = models.ForeignKey(
           'Project',
           on_delete=models.CASCADE,
           related_name='pledges'
     )
     supporter = models.ForeignKey(
          get_user_model(),
          on_delete=models.CASCADE,
          related_name='supporter_pledges'
     )