from rest_framework import serializers
from core.models import Project

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = '__all__'

class ProjectSerializerNew(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ['project_id', 'name', 'teams', 'collabs']
        extra_kwargs = {
            'teams': {'required': False},
            'collabs': {'required': False},
        }


class ProjectSerializerCreate(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ['project_id', 'name', 'teams', 'collabs']
        extra_kwargs = {
            'teams': {'required': False},
            'collabs': {'required': False},
        }

    def validate_name(self,value):
        user = self.context['request'].user
        if Project.objects.filter(name=value,propietary=user).exists():
            raise serializers.ValidationError("Ya tienen un proyecto con ese nombre")
        return value


