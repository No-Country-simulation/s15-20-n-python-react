from rest_framework import generics, permissions
from lists.api.serializer import ListSerializerGet, ListSerializerPost
from core.models import TasksList
from drf_spectacular.utils import extend_schema


class ListsListCreateApiView(generics.ListCreateAPIView):
    queryset = TasksList.objects.all()
    serializer_class = ListSerializerGet
    #permission_classes = [permissions.IsAuthenticated]


    def get_serializer_class(self):
        if self.request.method == 'POST':
            return ListSerializerPost
        return ListSerializerGet
    

    def get_queryset(self):
        id_list = self.request.GET.get('list_id')
        if id_list:
            return TasksList.objects.filter(is_active=True,membership_board=id_list)
        return TasksList.objects.filter(is_active=True)

    @extend_schema(
    tags=['Listas'],
    summary='Genera una lista de Listas',
    description=(
            'Muestra todas las listas del tablero o la lista solicitada si se pasa el id (/lists?id_list=N)'
        ),
    )
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)
    
    @extend_schema(
        tags=['Listas'],
        summary='Creación de una Lista', 
        description=('Crea una nueva Lista.\n\n'
        'Crea una nueva lista. Datos solicitados:\n'
        '[title, description, membership_board]\n'
        )
    )
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)


class ListDetailUpdateApiView(generics.RetrieveUpdateDestroyAPIView):
    queryset = TasksList.objects.all()
    serializer_class = ListSerializerPost
    #permission_classes = [permissions.IsAuthenticated]

    def perform_update(self, serializer):
        serializer.save()


    @extend_schema(
    tags=['Listas'],
    summary='Actualización de lista', 
    description=('Actualizacion de todos los datos de una lista.\n\n'
    )
    )
    def put(self, request, *args, **kwargs):
        return super().put(request, *args, **kwargs)
    
    @extend_schema(
    tags=['Listas'],
    summary='Actualización parcial de lista', 
    description=('Actualizacion de una parte de los datos de una lista.\n\n'
    )
    )
    def patch(self, request, *args, **kwargs):
        return super().patch(request, *args, **kwargs)
    
    @extend_schema(
    tags=['Listas'],
    summary='Borrado de lista', 
    description=('Borrado definitivo de una lista.\n\n'
    )
    )
    def delete(self, request, *args, **kwargs):
        instance = self.get_object()
        if instance.is_active:
            instance.is_active = False
            instance.save()
            return instance
        else:
            return("List not found")