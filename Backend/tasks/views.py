from rest_framework import generics, permissions
from tasks.serializers import TaskSerializer
from core.models import Task
from drf_spectacular.utils import extend_schema

# Create your views here.
class TaskList(generics.ListCreateAPIView):
    permission_classes = [permissions.AllowAny]
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

    @extend_schema(
        tags=['Tasks'],
        operation_id='creacion de tareas',
        description='Se crea una nueva tarea',
    )
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)    
    
    @extend_schema(
        tags=['Tasks'],
        operation_id='listado de tareas',
        description='Se listan todas las tareas',
    )
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

class TaskDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [permissions.AllowAny]
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

    @extend_schema(
        tags=['Tasks'],
        operation_id='actualizar tarea',
        description='Se actualiza una tarea',
    )
    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    @extend_schema(
        tags=['Tasks'],
        operation_id='actualizar parcialmente tarea',
        description='Se actualiza parcialmente una tarea',
    )
    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)

    @extend_schema(
        tags=['Tasks'],
        operation_id='borrar tarea',
        description='Se elimina una tarea',
    )
    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
