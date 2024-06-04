from rest_framework import generics, permissions, status, filters
from core.models import Project
from projects.api.serializer import ProjectSerializer , ProjectSerializerCreate , ProjectSerializerUpdate
from rest_framework.exceptions import PermissionDenied
from rest_framework.response import Response
from drf_spectacular.utils import extend_schema



############### REORGANIZADO DE CODIGO #################################

### VIEW LISTA DE PROYECTOS : 
@extend_schema(
    tags=['Proyectos'], 
    summary='Listado de Proyectos', 
    description='Obtiene una lista de todos los proyectos pertenecientes al usuario autenticado.',
)
class ProjectListView(generics.ListAPIView):
    serializer_class = ProjectSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [filters.SearchFilter]
    search_field = ["status"]

    def get_queryset(self):
        status = self.request.GET.get('status')
        if status:
            return Project.objects.filter(propietary=self.request.user, status=status)
        else:
            return Project.objects.filter(propietary=self.request.user)

### VIEW CREACION DE PROYECTO
@extend_schema(
    tags=['Proyectos'], 
    summary='Creación de un Proyecto', 
    description=('Crea un nuevo proyecto validando que el nombre no esté ya en uso por el usuario.\n\n'
    '**Status: se crea el proyecto con status Planning automaticamente**\n'
    )
)
class ProjectCreateView(generics.CreateAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializerCreate
    permission_classes = [permissions.IsAuthenticated]
    

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
    
    def perform_create(self, serializer):
        # Verifica que el usuario esté autenticado
        if self.request.user.is_authenticated:
            serializer.save(propietary=self.request.user)
        else:
            raise serializer.ValidationError("El usuario debe estar autenticado para crear un proyecto.")

### VIEW DETALLE UN PROYECTO : 
@extend_schema(
    tags=['Proyectos'],
    summary='Detalle de Proyecto',
    description='Obtiene los detalles de un proyecto específico perteneciente al usuario autenticado.',
)
class ProjectDetailView(generics.RetrieveAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Project.objects.filter(propietary=self.request.user)

### VIEW EDICION DE PROYECTO:
class ProjectUpdateView(generics.UpdateAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializerUpdate
    permission_classes = [permissions.IsAuthenticated]

    def perform_update(self, serializer):
        project = self.get_object()
        if project.propietary != self.request.user:
            raise PermissionDenied("No tiene permisos para modificar este Proyecto.")
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

### VIEW ELIMINACION DE PROYECTO:
@extend_schema(
    tags=['Proyectos'], 
    summary='Eliminación de Proyecto', 
    description='Elimina un proyecto específico perteneciente al usuario autenticado.'
)
class ProjectDeleteView(generics.DestroyAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    permission_classes = [permissions.IsAuthenticated]

    def destroy(self, request, *args, **kwargs): #modifico el metodo para que lo ponga en false en is_active
        instance = self.get_object()
        if instance.propietary != self.request.user:
            raise PermissionDenied("No eres el propietario para poder eliminar este Proyecto.")
        self.perform_destroy(instance)
        return Response({"detail": "Proyecto eliminado correctamente."}, status=status.HTTP_204_NO_CONTENT)