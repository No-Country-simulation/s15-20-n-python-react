from rest_framework import generics, permissions
from tasks.serializers import TaskSerializer, CommentSerializer
from core.models import Task, Comment
from drf_spectacular.utils import extend_schema

# Create your views here.
class TaskList(generics.ListCreateAPIView):
    permission_classes = [permissions.AllowAny]
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

    @extend_schema(
        tags=['Tasks'],
        operation_id='creacion de tareas',
        description='se crea una nueva tarea',
    )
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
    
    @extend_schema(
        tags=['Tasks'],
        operation_id='listado de tareas',
        description='se listan todas las tareas',
    )
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


class TaskDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [permissions.AllowAny]
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

    @extend_schema(
        tags=['Tasks'],
        operation_id='actualizar tareas',
        description='se actualiza una tarea',
    )
    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    @extend_schema(
        tags=['Tasks'],
        operation_id='borrar tareas',
        description='se elimina una tarea',
    )
    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)



