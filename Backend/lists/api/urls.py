from django.urls import path
from lists.api.views import ListsListCreateApiView, ListDetailUpdateApiView


urlpatterns = [
    path('<int:project_id>/boards/<int:board_id>/taskslists/', ListsListCreateApiView.as_view(), name='list-of-lists'),
    path('<int:project_id>/boards/<int:board_id>/taskslists/<int:pk>/',ListDetailUpdateApiView.as_view(), name='list-detail'),
]