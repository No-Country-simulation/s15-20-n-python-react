from django.urls import path
#from board.api.views import BoardApiListView , BoardApiCreateView, BoardApiDestroyView , BoardApiUpdateView
from board.api.views import BoardListCreateApiView, BoardDetailCreateApiView

urlpatterns = [
    path('list/', BoardListCreateApiView.as_view(), name='board-list'),
    path('detail/<int:pk>/',BoardDetailCreateApiView.as_view(), name='board-detail'),
]

"""
urlpatterns = [
    path('', BoardApiListView.as_view(), name='board-list'),
    path('create/',BoardApiCreateView.as_view(),name='board-create'),
    path('<int:pk>/delete/', BoardApiDestroyView.as_view(), name='board-delete'),
    path('<int:pk>/update/', BoardApiUpdateView.as_view(), name='board-delete'),
]


"""