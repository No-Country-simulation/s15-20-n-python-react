from rest_framework import serializers
from core.models import TasksList

class ListSerializerGet(serializers.ModelSerializer):
    class Meta:
        model = TasksList
        fields = '__all__'

    def get_queryset(self):
        return TasksList.objects.filter(is_active=True)
    
class ListSerializerPost(serializers.ModelSerializer):
    class Meta:
        model = TasksList
        fields = ['title', 'description', 'membership_board']

