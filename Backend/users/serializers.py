from rest_framework import serializers
from django.contrib.auth import get_user_model
from django.contrib.auth.password_validation import validate_password
from django.core import exceptions

from projects.api.serializer import ProjectSerializerCreate

# Instance of User model
User = get_user_model()

# Serializer for User model


class UserSerializer(serializers.ModelSerializer):
    projects = ProjectSerializerCreate(many=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'projects']
        extra_kwargs = {'password': {'write_only': True}, }

    def create(self, validated_data):
        user = User(**validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user
