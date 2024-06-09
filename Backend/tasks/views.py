from rest_framework import generics, permissions, status
from tasks.serializers import TaskSerializer
from core.models import Task
from drf_spectacular.utils import extend_schema
from rest_framework.response import Response

# Create your views here.
class TaskList(generics.ListCreateAPIView):
    permission_classes = [permissions.AllowAny, ]
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

    def get_queryset(self):
        return Task.objects.filter(is_active=True)

    @extend_schema(
        tags=['tareas'],
        operation_id='creacion de tareas',
        description='Se crea una nueva tarea',
    )
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)    
    
    @extend_schema(
        tags=['tareas'],
        operation_id='listado de tareas',
        description='Se listan todas las tareas',
    )
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

class TaskDetail(generics.RetrieveUpdateAPIView):
    permission_classes = [permissions.AllowAny, ]
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

    def get_queryset(self):
        return Task.objects.filter(is_active=True)

    @extend_schema(
        tags=['tareas'],
        operation_id='obtener tarea',
        description='Se obtiene una tarea',
    )
    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    @extend_schema(
        tags=['tareas'],
        operation_id='actualizar tarea',
        description='Se actualiza una tarea',
    )
    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    @extend_schema(
        tags=['tareas'],
        operation_id='actualizar parcialmente tarea',
        description='Se actualiza parcialmente una tarea',
    )
    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)
    
class TaskInactive(generics.DestroyAPIView):
    permission_classes = [permissions.AllowAny, ]
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

    def get_queryset(self):
        return Task.objects.filter(is_active=True)

    @extend_schema(
        tags=['tareas'],
        operation_id='borrar tarea',
        description='Se marca una tarea como inactiva en lugar de eliminarla',
    )
    def delete(self, request, *args, **kwargs):
        task = self.get_object()
        task.is_active = False
        task.save()
        return Response(status=status.HTTP_204_NO_CONTENT)