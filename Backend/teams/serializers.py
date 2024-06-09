from rest_framework import serializers
from core.models import Team, RoleType, Collaborator

# Create your serializers here.


class TeamSerializer(serializers.Serializer):
    members = serializers.StringRelatedField(many=True)

    class Meta:
        model = Team
        fields = ['name', 'members']


class RoleTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = RoleType
        fields = ['role_type']


class CollaboratorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Collaborator
        fields = ['role', 'user']
