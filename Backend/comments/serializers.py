from rest_framework import serializers
from core.models import Comment, Task


class FileSerializer(serializers.Serializer):
    class Meta:
        model = Comment
        fields = ['title', 'link']
        
class TaskSerializer(serializers.Serializer):
    class Meta:
        model = Task
        fields = ['title']