from django.urls import path
from board.api.views import BoardApiListView , BoardApiCreateView, BoardApiDestroyView


urlpatterns = [
    path('', BoardApiListView.as_view(), name='board-list'),
    path('create/',BoardApiCreateView.as_view(),name='board-create'),
    path('<int:pk>/delete/', BoardApiDestroyView.as_view(), name='board-delete'),
]
