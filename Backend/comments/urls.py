from django.urls import path
from comments.views import CommentAPIView, CommentDetailAPIView


urlpatterns = [
    path('<int:project_id>/boards/<int:board_id>/taskslists/<int:list_id>/tasks/<int:task_id>/comments/', CommentAPIView.as_view(), name='comments_list'),
    path('<int:project_id>/boards/<int:board_id>/taskslists/<int:list_id>/tasks/<int:task_id>/comments/<int:pk>/', CommentDetailAPIView.as_view(), name='comment_detail'),
]