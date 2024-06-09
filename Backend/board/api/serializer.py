from rest_framework import serializers
from core.models import Board


class BoardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Board
        fields = '__all__'

    def get_queryset(self):
        return Board.objects.filter(is_active=True)
        

class BoardSerializerCreate(serializers.ModelSerializer):
    class Meta:
        model = Board
        fields = ['board_id', 'title']


    def validate_title(self, value):
        membership_project = self.context['request'].data.get('membership_project')
        if Board.objects.filter(title=value, membership_project=membership_project).exists():
            raise serializers.ValidationError("Ya existe un tablero con ese nombre en el proyecto")
        return value



