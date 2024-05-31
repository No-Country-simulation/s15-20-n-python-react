from django.http import HttpResponse
from rest_framework import generics

from health.models import HealthTest
from health.serializers import HealthSerializer


# Create your views here.
class HealthListView(generics.ListCreateAPIView):
    serializer_class = HealthSerializer
    queryset = HealthTest.objects.all()

    def index(request):
        response = HealthTest.objects.first()
        return HttpResponse(response)
