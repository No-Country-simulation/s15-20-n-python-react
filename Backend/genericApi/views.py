from rest_framework import generics, permissions
from core.models import Project

from genericApi.serializer import ProjectSerializerAPI
from rest_framework.response import Response

class UserProjectsApiView(generics.GenericAPIView):
    serializer_class = ProjectSerializerAPI
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, *args, **kwargs):
        user = request.user
        projects = Project.objects.filter(propietary=user)
        serializer = self.get_serializer(projects, many=True)
        return Response(serializer.data)