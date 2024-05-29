from rest_framework import serializers
from core.models import Project
from core.models import Team, Collaborator


############### REORGANIZADO DE CODIGO #################################

####Serializador de proyectos para Listar y Eliminar####
class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = '__all__'

### Serializador de proyectos creacion de proyectos ####
class ProjectSerializerCreate(serializers.ModelSerializer):
    teams = serializers.PrimaryKeyRelatedField(queryset=Team.objects.all(), many=True)
    collabs = serializers.PrimaryKeyRelatedField(queryset=Collaborator.objects.all(), many=True)
    
    class Meta:
        model = Project
        fields = ['project_id', 'name', 'teams', 'collabs']

    def validate_name(self,value):
        user = self.context['request'].user
        if Project.objects.filter(name=value,propietary=user).exists():
            raise serializers.ValidationError("Ya tienen un proyecto con ese nombre")
        
        return value

    def create(self, validated_data):
        teams_data = validated_data.pop('teams', [])
        collabs_data = validated_data.pop('collabs', [])
        project = Project.objects.create(**validated_data)
        if teams_data:
            project.teams.set(teams_data)
        if collabs_data:
            project.collabs.set(collabs_data)
        return project

### Serializador de proyectos edicion de proyectos
class ProjectSerializerUpdate(serializers.ModelSerializer):
    teams = serializers.PrimaryKeyRelatedField(queryset=Team.objects.all(), many=True)
    collabs = serializers.PrimaryKeyRelatedField(queryset=Collaborator.objects.all(), many=True)

    class Meta:
        model = Project
        fields = ['project_id', 'name', 'teams', 'collabs','status']
        extra_kwargs = {
            'teams': {'required': False},
            'collabs': {'required': False},
        }

    def validate_name(self,value):
        user = self.context['request'].user
        if Project.objects.filter(name=value,propietary=user).exists():
            raise serializers.ValidationError("Ya tienen un proyecto con ese nombre")
        return value