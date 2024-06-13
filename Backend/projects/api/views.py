from rest_framework import generics, permissions, status
from core.models import Project
from projects.api.serializer import ProjectSerializerCreate 
from rest_framework.exceptions import PermissionDenied
from rest_framework.response import Response
from drf_spectacular.utils import extend_schema


class ProjectListCreateApiView(generics.ListCreateAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializerCreate
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        status = self.request.GET.get('status')
        if status:
            return Project.objects.filter(propietary=self.request.user, status=status, is_active=True)
        return Project.objects.filter(propietary=self.request.user, is_active=True)
        
    @extend_schema(
        tags=['Proyectos'],
        summary='Listado de Proyectos',
        description='Obtiene una lista de todos los proyectos activos pertenecientes al usuario autenticado. Puede filtrarse por estado utilizando el parámetro de consulta "status". Ejemplo: project?status=Planning',
    )
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)
    

    @extend_schema(
        tags=['Proyectos'],
        summary='Creación de un Proyecto',
        description=(
            'Crea un nuevo proyecto validando que el nombre no esté ya en uso por el usuario.\n\n'
            '**Status:** se crea el proyecto con status Planning automáticamente.'
        ),
    )
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)
    
    def perform_create(self, serializer):
        if self.request.user.is_authenticated:
            serializer.save(propietary=self.request.user, status='In_progress')
        else:
            raise PermissionDenied("El usuario debe estar autenticado para crear un proyecto.")


class ProjectDetailCreateApiView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializerCreate
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Project.objects.filter(propietary=self.request.user,is_active=True)
    

    @extend_schema(
        tags=['Proyectos'],
        summary='Detalle de Proyecto',
        description='Obtiene los detalles de un proyecto específico perteneciente al usuario autenticado.',
    )
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    def perform_update(self, serializer):
        project = self.get_object()
        if project.propietary != self.request.user:
            raise PermissionDenied("No tiene permisos para modificar este proyecto.")
        serializer.save()
    
    @extend_schema(
        tags=['Proyectos'],
        summary='Actualización de Proyecto',
        description=(
            'Actualiza los detalles de un proyecto específico perteneciente al usuario autenticado.\n\n'
            '**Status:**\n'
            '- `Planning`\n'
            '- `In progress`\n'
            '- `Completed`\n'
            '- `Cancelled`\n'
        ),
    )
    def put(self, request, *args, **kwargs):
        return super().put(request, *args, **kwargs)
    
    @extend_schema(
        tags=['Proyectos'],
        summary='Actualización de Proyecto (parcial)',
        description=(
            'Actualiza los detalles parciales de un proyecto específico perteneciente al usuario autenticado.\n\n'
            '**Status:**\n'
            '- `Planning`\n'
            '- `In progress`\n'
            '- `Completed`\n'
            '- `Cancelled`\n'
        ),
    )
    def patch(self, request, *args, **kwargs):
        return super().patch(request, *args, **kwargs)
    

    @extend_schema(
        tags=['Proyectos'],
        summary='elimina Proyecto',
        description=(
            'is_Active = false'
        ),
    )
    def delete(self, request, *args, **kwargs):
        return super().delete(request, *args, **kwargs)
    

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        if instance.propietary != self.request.user:
            raise PermissionDenied("No eres el propietario para poder eliminar este proyecto.")
        instance.is_active = False
        instance.save()
        return Response({"detail": "Proyecto eliminado correctamente."}, status=status.HTTP_204_NO_CONTENT)

