from rest_framework import generics, permissions
from board.api.serializer import BoardSerializer , BoardSerializerCreate
from core.models import Board

class BoardApiListView(generics.ListAPIView):
    serializer_class = BoardSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Board.objects.filter(is_active=True)


class BoardApiCreateView(generics.CreateAPIView):
    queryset = Board.objects.all()
    serializer_class = BoardSerializerCreate
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)