from rest_framework import generics, permissions, status
from core.models import Project
from projects.api.serializer import ProjectSerializer ,ProjectSerializerNew , ProjectSerializerCreate
from rest_framework.exceptions import PermissionDenied
from rest_framework.response import Response

class ProjectCreateView(generics.CreateAPIView):
    """Creacion de un nuevo Proyecto (valida nombre si ya esta usado por el usuario)

    Args:
        'name' (str): Nombre del proyecto
        'propietary' (pk): id del propietario (esto lo tengo que ver con validacion de usr)
        'teams' (List): lista de equipo (required:False)
        'collabs' (List): lista de colaboradores (required:False)

    """
    queryset = Project.objects.all()
    serializer_class = ProjectSerializerCreate
    permission_classes = [permissions.IsAuthenticated]

    
    def perform_create(self, serializer):
        # Verifica que el usuario esté autenticado
        if self.request.user.is_authenticated:
            serializer.save(propietary=self.request.user)
        else:
            raise serializer.ValidationError("El usuario debe estar autenticado para crear un proyecto.")
        


class ProjectListView(generics.ListAPIView):
    """GET trae todos los projectos de la propiedad del usuario autenticado
    """
    serializer_class = ProjectSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Project.objects.filter(propietary=self.request.user)

class ProjectDetailView(generics.RetrieveAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Project.objects.filter(propietary=self.request.user)


class ProjectUpdateView(generics.UpdateAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializerNew
    permission_classes = [permissions.IsAuthenticated]

    def perform_update(self, serializer):
        project = self.get_object()
        if project.propietary != self.request.user:
            raise PermissionDenied("No tiene permisos para modificar este Proyecto.")
        serializer.save()

"""
class ProjectDeleteView(generics.DestroyAPIView):
    queryset = Project.objects.all()
    permission_classes = [permissions.IsAuthenticated]

    def perform_destroy(self, instance):
        if instance.propietary != self.request.user:
            raise PermissionDenied("No eres el propietario para poder eliminar este Proyecto.")
        instance.delete()
    
    def delete(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response({"detail": "Proyecto eliminado correctamente."}, status=status.HTTP_204_NO_CONTENT)
""" 
class ProjectDeleteView(generics.DestroyAPIView):
    queryset = Project.objects.all()
    permission_classes = [permissions.IsAuthenticated]

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        if instance.propietary != self.request.user:
            raise PermissionDenied("No eres el propietario para poder eliminar este Proyecto.")
        self.perform_destroy(instance)
        return Response({"detail": "Proyecto eliminado correctamente."}, status=status.HTTP_204_NO_CONTENT)