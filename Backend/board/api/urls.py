from django.urls import path
#from board.api.views import BoardApiListView , BoardApiCreateView, BoardApiDestroyView , BoardApiUpdateView
from board.api.views import BoardListCreateApiView, BoardDetailCreateApiView

urlpatterns = [
    path('<int:project_id>/boards/', BoardListCreateApiView.as_view(), name='board-list'),
    path('<int:project_id>/boards/<int:pk>/',BoardDetailCreateApiView.as_view(), name='board-detail'),
]
