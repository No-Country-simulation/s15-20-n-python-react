from django.contrib.auth import get_user_model
from users.serializers import UserSerializer
from rest_framework import generics, permissions
from drf_spectacular.utils import extend_schema
from rest_framework_simplejwt.views import TokenObtainPairView

# Instance of User model
User = get_user_model()

# Create your views here.


class UserList(generics.ListCreateAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()

    @extend_schema(
        tags=['Usuarios'],
        operation_id='Listado de Usuarios',
        description='Listado de todos los usuarios',
    )
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    @extend_schema(
        tags=['Usuarios'],
        operation_id='Creación de Usuario',
        description='Adjunta un objeto con los valores indicados para crear un nuevo Usuario',
    )
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    @extend_schema(
        tags=['Usuarios'],
        operation_id='Muestra un usuario especificado',
        description='Usado para mostrar un usuario especificado como parámetro en la URL.',
    )
    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    @extend_schema(
        tags=['Usuarios'],
        operation_id='Modificación del Usuario especificado.',
        description='Adjunta un objeto con los valores indicados para modificar un usuario especificado como parámetro en la URL, debe proporcionar en el cuerpo de la petición todos los valores del objeto usuario.',
    )
    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    @extend_schema(
        tags=['Usuarios'],
        operation_id='Modificación de datos del Usuario especificado.',
        description='Adjunta un objeto con los valores indicados para modificar un usuario especificado como parámetro en la URL, debe proporcionar en el cuerpo de la petición solo los datos a modificar.',
    )
    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)

    @extend_schema(
        tags=['Usuarios'],
        operation_id='Borrado de Usuario especificado',
        description='Elimina el registro del usuario especificado como parámetro en la URL.',
    )
    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
