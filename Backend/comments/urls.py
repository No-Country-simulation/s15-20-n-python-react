from django.urls import path
from comments.views import CommentAPIView, CommentDetailAPIView


urlpatterns = [
    path('list/', CommentAPIView.as_view(), name='comments_list'),
    path('create/', CommentAPIView.as_view(), name='comment_create'),
    path('detail/<int:pk>/', CommentDetailAPIView.as_view(), name='comment_detail'),
]