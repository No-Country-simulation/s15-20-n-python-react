from rest_framework import generics, permissions
from comments.serializers import CommentSerializerGet, CommentSerializerPost
from core.models import Comment, Task, Board, Project
from drf_spectacular.utils import extend_schema
from cloudinary import uploader
from cloudinary import api

class CommentAPIView(generics.ListCreateAPIView):
    queryset = Comment.objects.all()
    
    @extend_schema(
        tags=['Comentarios'],
        operation_id='Muestra el listado de comentarios',
        description='Usado para mostrar los comentarios de la tarea especificada como parámetro en la URL.',
    )
    def get(self, request, *args, **kwargs):
        serializer_class = CommentSerializerGet
        return self.list(request, *args, **kwargs)
    
    @extend_schema(
        tags=['Comentarios'],
        operation_id='Guarda un comentario cargado',
        description='Usado para guardar el comentario da la tarea que recibe como parámetro en la URL.',
    )
    def post(self, request, *args, **kwargs):
        serializer_class = CommentSerializerPost
        return self.create(request, *args, **kwargs)

        
    def perform_create(self, serializer):
        
        project = Project.objects.get(self.request.project_id)
        board = Board.objects.get(self.request.board_id)
        task = Task.objects.get(self.request.task_id)
        
        user = project.propietary
        project_name = project.name
        board_name = board.title
        task_name = task.title
        
        if self.request.file:
            file = self.request.file
            file_uploaded = uploader.upload(
            file,
            folder=f'PML/{user}/{project_name}/{board_name}/{task_name}',
            resource_type = 'image',
            use_filename = True
            )
        
            file_url = file_uploaded['secure_url']
            serializer.save(file_link=file_url)
        else:
            pass
    

class CommentDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Comment.objects.all()
    
    @extend_schema(
        tags=['Comentarios'],
        operation_id='Obtiene un comentario específico',
        description='Usado para obtener el comentario de la tarea que recibe como parámetro en la URL, incluyendo la imagen adjunta.',
    )     
    def get(self, request, *args, **kwargs):
        serializer_class = CommentSerializerGet
        return self.retrieve(request, *args, **kwargs)

    @extend_schema(
        tags=['Comentarios'],
        operation_id='Modifica un comentario específico',
        description='Usado para modificar el comentario de la tarea que recibe como parámetro en la URL.',
    ) 
    def put(self, request, *args, **kwargs):
        serializer_class = CommentSerializerPost
        return self.update(request, *args, **kwargs)
    
    @extend_schema(
        tags=['Comentarios'],
        operation_id='Modifica parcialmente un comentario específico',
        description='Usado para modificar una parte del comentario de la tarea que recibe como parámetro en la URL.',
    ) 
    def patch(self, request, *args, **kwargs):
        serializer_class = CommentSerializerPost
        return self.partial_update(request, *args, **kwargs)
    
    @extend_schema(
        tags=['Comentarios'],
        operation_id='Elimina un comentario específico',
        description='Usado para borrar el comentario de la tarea que recibe como parámetro en la URL.',
    )    
    def delete(self, request, *args, **kwargs):
        serializer_class = CommentSerializerGet
        instance = self.get_object()
        if instance.is_active:
            instance.is_active = False
            instance.save()
            return instance
        else:
            return("Comment not found")
            