from django.urls import path
from lists.api.views import ListsListCreateApiView, ListDetailUpdateApiView


urlpatterns = [
    path('taskslists/', ListsListCreateApiView.as_view(), name='list-of-lists'),
    path('listedit/<int:pk>/',ListDetailUpdateApiView.as_view(), name='edit-list'),
]