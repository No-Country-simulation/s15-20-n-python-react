from rest_framework import serializers
from core.models import Board


class BoardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Board
        fields = '__all__'


class BoardSerializerCreate(serializers.ModelSerializer):
    class Meta:
        model = Board
        fields = ['title', 'membership_project']
