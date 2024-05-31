from rest_framework import serializers

from .models import HealthTest

# Create your serializers here.


class HealthSerializer(serializers.ModelSerializer):
    class Meta:
        model = HealthTest
        fields = ['message', 'created']
        extra_fields = {'created': {'read_only': True},
                        'message': {'read_only': True}}
