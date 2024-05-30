from rest_framework import generics, permissions
from files.serializers import FileSerializer, TaskSerializer
from core.models import File, Task
from drf_spectacular.utils import extend_schema

class FileDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (permissions.AllowAny, )
    queryset = File.objects.all()
    serializer_class = FileSerializer

    @extend_schema(
        tags=['Archivos'],
        request=FileSerializer,
        responses=FileSerializer,
        operation_id='Muestra un Archivo especificado',
        description='Usado para mostrar el archivo especificado como parámetro en la URL.',
    )
    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    @extend_schema(
        tags=['Archivos'],
        request=FileSerializer,
        responses=FileSerializer,
        operation_id='Modificación del Archivo especificado',
        description='Usado para modificar un equipo especificado como parámetro en la URL, debe proporcionar todos los valores del equipo.',
    )
    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    @extend_schema(
        tags=['Archivos'],
        request=FileSerializer,
        responses=FileSerializer,
        operation_id='Modificación parcial del Archivo especificado',
        description='Modificación parcial del equipo especificado como parámetro en la URL. solo indique los valores que quiere modificar.',
    )
    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)

    @extend_schema(
        tags=['Archivos'],
        request=FileSerializer,
        responses=FileSerializer,
        operation_id='Eliminación del Archivo especificado',
        description='Elimina el equipo especificado como parámetro en la URL.',
    )
    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)