from django.urls import path
from files.views import FileDetail


urlpatterns = [
    path('task/files/detail/<int:pk>/', FileDetail.as_view(), name='file_detail'),
]