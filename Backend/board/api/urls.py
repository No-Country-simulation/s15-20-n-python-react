from django.urls import path
from board.api.views import BoardApiListView , BoardApiCreateView


urlpatterns = [
    path('', BoardApiListView.as_view(), name='board-list'),
    path('create/',BoardApiCreateView.as_view(),name='board-create'),
]
