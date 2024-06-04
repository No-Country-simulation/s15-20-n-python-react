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
        fields = ['title', 'membership_project']


