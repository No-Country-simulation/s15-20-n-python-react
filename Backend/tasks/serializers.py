from rest_framework import serializers
from core.models import Task


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = [
            'title',
            'description',
            'expiration_at',
            'labels',
            'assigned_users',
        ]
