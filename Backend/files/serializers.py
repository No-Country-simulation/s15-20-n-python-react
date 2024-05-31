from rest_framework import serializers
from core.models import File, Task


class FileSerializer(serializers.Serializer):
    class Meta:
        model = File
        fields = ['title', 'link']
        
class TaskSerializer(serializers.Serializer):
    class Meta:
        model = Task
        fields = ['title']