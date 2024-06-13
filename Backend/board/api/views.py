from rest_framework import generics, permissions, status ,serializers
from board.api.serializer import BoardSerializer , BoardSerializerCreate
from rest_framework.exceptions import NotFound
from core.models import Board
from drf_spectacular.utils import extend_schema


class BoardListCreateApiView(generics.ListCreateAPIView):
    queryset = Board.objects.all()
    serializer_class = BoardSerializer
    permission_classes = [permissions.IsAuthenticated]



    def get_serializer_class(self):
        if self.request.method == 'POST':
            return BoardSerializerCreate
        return BoardSerializer

    """
    def get_queryset(self):
        id_project = self.request.GET.get('id_project')
        if id_project:
            return Board.objects.filter(is_active=True,membership_project=id_project)
        return Board.objects.filter(is_active=True)
    """
    def get_queryset(self):
        project_id = self.kwargs['project_id']
        return Board.objects.filter(membership_project=project_id, is_active=True)

    @extend_schema(
    tags=['Board'],
    summary='Lista Board',
    description=(
            'Lista Board (todos, y si se agrega /board?id_project=X trae solo las board del proyecto X)'
        ),
    )
    def get(self, request, *args, **kwargs):

        return super().get(request, *args, **kwargs)
    


    def perform_create(self, serializer):
        project_id = self.kwargs['project_id']
        serializer.save(membership_project_id=project_id)

        
    @extend_schema(
        tags=['Board'],
        summary='Creación de una Board', 
        description=('Crea una nueva Board.\n\n'
        'Crea una nueva board. datos solicitados:\n'
        '[title, membership_project]\n'
        )
    )
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)



class BoardDetailCreateApiView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Board.objects.all()
    serializer_class = BoardSerializerCreate
    permission_classes = [permissions.IsAuthenticated]

    def perform_update(self, serializer):
        serializer.save()


    def get_object(self):
        project_id = self.kwargs['project_id']
        board_id = self.kwargs['pk']
        
        try:
            board = Board.objects.get(pk=board_id, membership_project_id=project_id, is_active=True)
        except Board.DoesNotExist:
            raise NotFound("Esa board no corresponde al proyecto")
        
        return board

    @extend_schema(
    tags=['Board'],
    summary='UPDATE board', 
    description=('Actualizacion de.\n\n'
    )
    )
    def put(self, request, *args, **kwargs):
        return super().put(request, *args, **kwargs)
    
    @extend_schema(
    tags=['Board'],
    summary='UPDATE board parcial', 
    description=('Actualizacion de.\n\n'
    )
    )
    def patch(self, request, *args, **kwargs):
        return super().patch(request, *args, **kwargs)
    

    @extend_schema(
    tags=['Board'],
    summary='Trae board ', 
    description=('Actualizacion de.\n\n'
    )
    )
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)
    

    @extend_schema(
    tags=['Board'],
    summary='Elimina Board ', 
    description=('pone en is_Active = False.\n\n'
    )
    )
    def delete(self, request, *args, **kwargs):
        return super().delete(request, *args, **kwargs)
    

