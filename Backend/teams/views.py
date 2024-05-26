from rest_framework import generics, permissions
from teams.serializers import TeamSerializer, RoleTypeSerializer, CollaboratorSerializer
from core.models import Team, RoleType, Collaborator
from drf_spectacular.utils import extend_schema

# Create your views here.


class TeamList(generics.ListCreateAPIView):
    permission_classes = (permissions.AllowAny, )
    queryset = Team.objects.all()
    serializer_class = TeamSerializer

    @extend_schema(
        tags=['Equipos'],
        request=TeamSerializer,
        responses=TeamSerializer,
        operation_id='Listado de Equipos',
        description='Listado de todos los Equipos',
    )
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    @extend_schema(
        tags=['Equipos'],
        request=TeamSerializer,
        responses=TeamSerializer,
        operation_id='Creación de Equipo',
        description='Crea un nuevo Equipo',
    )
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class TeamDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (permissions.AllowAny, )
    queryset = Team.objects.all()
    serializer_class = TeamSerializer

    @extend_schema(
        tags=['Equipos'],
        request=TeamSerializer,
        responses=TeamSerializer,
        operation_id='Muestra un Equipo especificado',
        description='Usado para mostrar el equipo especificado como parámetro en la URL.',
    )
    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    @extend_schema(
        tags=['Equipos'],
        request=TeamSerializer,
        responses=TeamSerializer,
        operation_id='Modificación del equipo especificado',
        description='Usado para modificar un equipo especificado como parámetro en la URL, debe proporcionar todos los valores del equipo.',
    )
    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    @extend_schema(
        tags=['Equipos'],
        request=TeamSerializer,
        responses=TeamSerializer,
        operation_id='Modificación parcial del equipo especificado',
        description='Modificación parcial del equipo especificado como parámetro en la URL. solo indique los valores que quiere modificar.',
    )
    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)

    @extend_schema(
        tags=['Equipos'],
        request=TeamSerializer,
        responses=TeamSerializer,
        operation_id='Eliminación del equipo especificado',
        description='Elimina el equipo especificado como parámetro en la URL.',
    )
    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


class RoleTypeList(generics.ListCreateAPIView):
    permission_classes = (permissions.AllowAny, )
    queryset = RoleType.objects.all()
    serializer_class = RoleTypeSerializer

    @extend_schema(
        tags=['Roles'],
        request=RoleTypeSerializer,
        responses=RoleTypeSerializer,
        operation_id='Listado de Roles',
        description='Listado de todos los Roles',
    )
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    @extend_schema(
        tags=['Roles'],
        request=RoleTypeSerializer,
        responses=RoleTypeSerializer,
        operation_id='Creación de Roles',
        description='Crea un nuevo Rol',
    )
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class RoleTypeDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (permissions.AllowAny, )
    queryset = RoleType.objects.all()
    serializer_class = RoleTypeSerializer

    @extend_schema(
        tags=['Roles'],
        request=RoleTypeSerializer,
        responses=RoleTypeSerializer,
        operation_id='Muestra un Rol especificado',
        description='Usado para mostrar el equipo especificado como parámetro en la URL.',
    )
    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    @extend_schema(
        tags=['Roles'],
        request=RoleTypeSerializer,
        responses=RoleTypeSerializer,
        operation_id='Modificación del Rol especificado',
        description='Usado para modificar un equipo especificado como parámetro en la URL, debe proporcionar todos los valores del equipo.',
    )
    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    @extend_schema(
        tags=['Roles'],
        request=RoleTypeSerializer,
        responses=RoleTypeSerializer,
        operation_id='Modificación parcial del Rol especificado',
        description='Modificación parcial del equipo especificado como parámetro en la URL. solo indique los valores que quiere modificar.',
    )
    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)

    @extend_schema(
        tags=['Roles'],
        request=RoleTypeSerializer,
        responses=RoleTypeSerializer,
        operation_id='Eliminación del Rol especificado',
        description='Elimina el equipo especificado como parámetro en la URL.',
    )
    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


class CollaboratorList(generics.ListCreateAPIView):
    permission_classes = (permissions.AllowAny, )
    queryset = Collaborator.objects.all()
    serializer_class = CollaboratorSerializer

    @extend_schema(
        tags=['Colaboradores'],
        request=CollaboratorSerializer,
        responses=CollaboratorSerializer,
        operation_id='Listado de Colaboradores',
        description='Listado de todos los Equipos',
    )
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    @extend_schema(
        tags=['Colaboradores'],
        request=CollaboratorSerializer,
        responses=CollaboratorSerializer,
        operation_id='Creación de Colaborador',
        description='Crea un nuevo Equipo',
    )
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class CollaboratorDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (permissions.AllowAny, )
    queryset = Collaborator.objects.all()
    serializer_class = CollaboratorSerializer

    @extend_schema(
        tags=['Colaboradores'],
        request=CollaboratorSerializer,
        responses=CollaboratorSerializer,
        operation_id='Muestra un Colaborador especificado',
        description='Usado para mostrar el equipo especificado como parámetro en la URL.',
    )
    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    @extend_schema(
        tags=['Colaboradores'],
        request=CollaboratorSerializer,
        responses=CollaboratorSerializer,
        operation_id='Modificación del Colaborador especificado',
        description='Usado para modificar un equipo especificado como parámetro en la URL, debe proporcionar todos los valores del equipo.',
    )
    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    @extend_schema(
        tags=['Colaboradores'],
        request=CollaboratorSerializer,
        responses=CollaboratorSerializer,
        operation_id='Modificación parcial del Colaborador especificado',
        description='Modificación parcial del equipo especificado como parámetro en la URL. solo indique los valores que quiere modificar.',
    )
    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)

    @extend_schema(
        tags=['Colaboradores'],
        request=CollaboratorSerializer,
        responses=CollaboratorSerializer,
        operation_id='Eliminación del Colaborador especificado',
        description='Elimina el equipo especificado como parámetro en la URL.',
    )
    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
