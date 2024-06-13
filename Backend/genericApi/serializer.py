from rest_framework import serializers
from core.models import Project, Team, Collaborator, Board, TasksList, Task, LabelTask

class LabelTaskSerializerAPI(serializers.ModelSerializer):
    class Meta:
        model = LabelTask
        fields = ['label_text', 'status', 'is_active']

class TaskSerializerAPI(serializers.ModelSerializer):
    labels = LabelTaskSerializerAPI(many=True)
    assigned_users = serializers.StringRelatedField(many=True)
    
    class Meta:
        model = Task
        fields = ['task_id', 'title', 'description', 'create_at', 'expiration_at', 'labels', 'assigned_users', 'status', 'is_active']

class TasksListSerializerAPI(serializers.ModelSerializer):
    tasks = TaskSerializerAPI(many=True, read_only=True, source='task_set')
    
    class Meta:
        model = TasksList
        fields = ['list_id', 'title', 'description', 'membership_board', 'status', 'is_active', 'tasks']

class BoardSerializerAPI(serializers.ModelSerializer):
    tasks_lists = TasksListSerializerAPI(many=True, read_only=True, source='taskslist_set')
    
    class Meta:
        model = Board
        fields = ['board_id', 'title', 'membership_project', 'status', 'is_active', 'tasks_lists']

class TeamSerializerAPI(serializers.ModelSerializer):
    members = serializers.StringRelatedField(many=True)
    
    class Meta:
        model = Team
        fields = ['team_id', 'name', 'members', 'status', 'is_active']

class CollaboratorSerializerAPI(serializers.ModelSerializer):
    user = serializers.StringRelatedField()
    
    class Meta:
        model = Collaborator
        fields = ['collab_id', 'role', 'user', 'status', 'is_active']

class ProjectSerializerAPI(serializers.ModelSerializer):
    teams = TeamSerializerAPI(many=True)
    collabs = CollaboratorSerializerAPI(many=True)
    boards = BoardSerializerAPI(many=True, read_only=True, source='board_set')
    
    class Meta:
        model = Project
        fields = ['project_id', 'name', 'teams', 'collabs', 'status', 'is_active', 'boards']