from rest_framework import serializers
from .models import Project

class ProjectSerializer(serializers.Serializer):
     id = serializers.ReadOnlyField()
     title = serializers.CharField(max_length=200)
     description = serializers.CharField(max_length=None)
     goal = serializers.IntegerField()
     image = serializers.URLField()
     is_open = serializers.BooleanField()
     date_created = serializers.DateTimeField()
     owner = serializers.CharField(max_length=200)
     category = serializers.CharField(max_length=200)
     location = serializers.CharField(max_length=200)

     #this will be called for POST /projects to create a new projects
     def create(self, validated_data):
           return Project.objects.create(**validated_data)