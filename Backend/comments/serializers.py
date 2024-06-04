from rest_framework import serializers
from core.models import Comment, Task
from django.contrib.auth import get_user_model

User = get_user_model()


class CommentSerializerGet(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'

class CommentSerializerPost(serializers.Serializer):
    user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())
    commented_task = serializers.PrimaryKeyRelatedField(queryset=Task.objects.all())
    class Meta:
        model = Comment
        fields = ['user', 'text_comment', 'file', 'commented_task']
        extra_kwargs = {
            'file': {'required': False},
            'text_comment': {'required': False},
        }
        