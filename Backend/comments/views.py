from rest_framework import generics, permissions
from comments.serializers import CommentSerializerGet, CommentSerializerPost
from core.models import Comment, Task
from drf_spectacular.utils import extend_schema
from cloudinary import uploader
from cloudinary import api

class FileViewList(generics.ListAPIView):
    
    @extend_schema(
        tags=['Archivos'],
        request=CommentSerializerGet,
        responses=CommentSerializerGet,
        operation_id='Muestra el listado de comentarios',
        description='Usado para mostrar los comentarios de la tarea especificada como parámetro en la URL.',
    )
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
    
class FileViewCreate(generics.CreateAPIView):
    
    @extend_schema(
        tags=['Archivos'],
        request=CommentSerializerPost,
        responses=CommentSerializerPost,
        operation_id='Guarda un comentario cargado',
        description='Usado para guardar el comentario da la tarea que recibe como parámetro en la URL.',
    )
    def post(self, request, *args, **kwargs):
        file = request.files['file']
        file_uploaded = uploader.upload(
            file,
            folder='PML',
            resource_type = 'image',
            use_filemname = True
            )
        
        file_url = file_uploaded['secure_url']
        return self.create(request, *args, **kwargs)

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

    @extend_schema(
        tags=['Archivos'],
        request=FileSerializer,
        responses=FileSerializer,
        operation_id='Eliminación del Archivo especificado',
        description='Elimina el archivo especificado como parámetro en la URL.',
    )
    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
"""