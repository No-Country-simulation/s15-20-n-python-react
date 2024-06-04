from rest_framework import generics, permissions, status
from board.api.serializer import BoardSerializer , BoardSerializerCreate
from rest_framework.response import Response
from core.models import Board

class BoardApiListView(generics.ListAPIView):
    serializer_class = BoardSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        id_project = self.request.GET.get('id_project')
        if id_project:
            return Board.objects.filter(is_active=True,membership_project=id_project)
        else:
            return Board.objects.filter(is_active=True)
        #return Board.objects.all()


class BoardApiCreateView(generics.CreateAPIView):
    queryset = Board.objects.all()
    serializer_class = BoardSerializerCreate
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
    

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

    def put(self, request, *args, **kwargs):
        return super().put(request, *args, **kwargs)