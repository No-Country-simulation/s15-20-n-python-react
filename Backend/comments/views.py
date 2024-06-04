from rest_framework import generics, permissions
from comments.serializers import CommentSerializerGet, CommentSerializerPost
from core.models import Comment, Task
from drf_spectacular.utils import extend_schema
from cloudinary import uploader
from cloudinary import api

class CommentAPIViewList(generics.ListAPIView):
    
    @extend_schema(
        tags=['Comentarios'],
        operation_id='Muestra el listado de comentarios',
        description='Usado para mostrar los comentarios de la tarea especificada como parámetro en la URL.',
    )
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
    
class CommentAPIViewCreate(generics.CreateAPIView):
    
    @extend_schema(
        tags=['Comentarios'],
        operation_id='Guarda un comentario cargado',
        description='Usado para guardar el comentario da la tarea que recibe como parámetro en la URL.',
    )
    def post(self, request, *args, **kwargs):
        queryset = Comment.objects.all()
        serializer_class = CommentSerializerPost
        
        return self.create(request, *args, **kwargs)

        
    def perform_create(self, serializer):
        # Verifica que el usuario esté autenticado
        
        if self.request.file:
            file = self.request.file
            file_uploaded = uploader.upload(
            file,
            folder='PML',
            resource_type = 'image',
            use_filename = True
            )
        
            file_url = file_uploaded['secure_url']
            serializer.save(file_link=file_url)
        else:
            pass

class CommentAPIViewDelete(generics.DestroyAPIView):
        queryset = Comment.objects.all()
        
        def delete(self, request, *args, **kwargs):
            instance = self.get_object()
            if instance.is_active:
                instance.is_active = False
                instance.save()
                return instance
            else:
                return("Comment not found")
            

"""
class FileDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (permissions.AllowAny, )
    queryset = Comment.objects.all()
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

    
"""