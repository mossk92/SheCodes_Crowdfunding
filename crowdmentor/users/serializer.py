from rest_framework import serializers
from .models import CustomUser

class CustomUserSerializer(serializers.Serializer):
    id = serializers.ReadOnlyField()
    username = serializers.CharField(max_length=200)
    email = serializers.CharField(max_length=200)
    name = serializers.CharField(max_length=200)
    email = serializers.EmailField()
    bio = serializers.CharField()
    date_created = serializers.DateField()
    def create(self, validated_data):
        return CustomUser.objects.create(**validated_data)