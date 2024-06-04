from rest_framework import generics, permissions, status ,serializers
from board.api.serializer import BoardSerializer , BoardSerializerCreate
from rest_framework.response import Response
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
    

    def get_queryset(self):
        id_project = self.request.GET.get('id_project')
        if id_project:
            return Board.objects.filter(is_active=True,membership_project=id_project)
        return Board.objects.filter(is_active=True)

    @extend_schema(
    tags=['Board'],
    summary='Lista Board',
    description=(
            'Lista Board (todos, y si se agrega /board?id_project=X trae solo las board del proyecto X)'
        ),
    )
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)
    
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



"""



@extend_schema(
    tags=['Board'],
    summary='Eliminacion de una Board', 
    description=('Cambia estado is_active a False.\n\n'
    )
)
class BoardApiDestroyView(generics.DestroyAPIView):
    queryset = Board.objects.all()
    serializer_class = BoardSerializer
    permission_classes = [permissions.IsAuthenticated]

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.is_active = False
        instance.save()
        return Response({"detail": "tablero eliminado correctamente."}, status=status.HTTP_204_NO_CONTENT)
    
class BoardApiUpdateView(generics.UpdateAPIView):
    queryset = Board.objects.all()
    serializer_class = BoardSerializer
    permission_classes = [permissions.IsAuthenticated]

    
    def perform_update(self, serializer):
        serializer.save()
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

        """