from rest_framework import serializers
from core.models import Project, Team, Collaborator, Board, TasksList, Task, Comment, File, LabelTask

class LabelTaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = LabelTask
        fields = ['label_text', 'status', 'is_active']

class TaskSerializer(serializers.ModelSerializer):
    labels = LabelTaskSerializer(many=True)
    assigned_users = serializers.StringRelatedField(many=True)
    
    class Meta:
        model = Task
        fields = ['task_id', 'title', 'description', 'create_at', 'expiration_at', 'labels', 'assigned_users', 'status', 'is_active']

class TasksListSerializer(serializers.ModelSerializer):
    tasks = TaskSerializer(many=True, read_only=True, source='task_set')
    
    class Meta:
        model = TasksList
        fields = ['list_id', 'title', 'description', 'membership_board', 'status', 'is_active', 'tasks']

class BoardSerializer(serializers.ModelSerializer):
    tasks_lists = TasksListSerializer(many=True, read_only=True, source='taskslist_set')
    
    class Meta:
        model = Board
        fields = ['board_id', 'title', 'membership_project', 'status', 'is_active', 'tasks_lists']

class TeamSerializer(serializers.ModelSerializer):
    members = serializers.StringRelatedField(many=True)
    
    class Meta:
        model = Team
        fields = ['team_id', 'name', 'members', 'status', 'is_active']

class CollaboratorSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField()
    
    class Meta:
        model = Collaborator
        fields = ['collab_id', 'role', 'user', 'status', 'is_active']

class ProjectSerializer(serializers.ModelSerializer):
    teams = TeamSerializer(many=True)
    collabs = CollaboratorSerializer(many=True)
    boards = BoardSerializer(many=True, read_only=True, source='board_set')
    
    class Meta:
        model = Project
        fields = ['project_id', 'name', 'teams', 'collabs', 'status', 'is_active', 'boards']