from rest_framework import serializers
from .models import CustomUser

class CustomUserSerializer(serializers.Serializer):
    id = serializers.ReadOnlyField()
    username = serializers.CharField(max_length=200)
    name = serializers.CharField(max_length=200)
    email = serializers.EmailField()
    bio = serializers.CharField()
    date_created = serializers.ReadOnlyField()

    def create(self, validated_data):
        return CustomUser.objects.create_user(**validated_data)

class UserDetailSerialiser(CustomUserSerializer):
      def update(self, instance, validated_data):
            instance.email = validated_data.get('email', instance.email)
            instance.name = validated_data.get('name', instance.name)
            instance.bio = validated_data.get('bio', instance.bio)
            instance.save()
            return instance