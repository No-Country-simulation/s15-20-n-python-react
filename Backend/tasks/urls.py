from django.urls import path
from tasks.views import TaskList, TaskDetail
urlpatterns = [
    path('list/', TaskList.as_view(), name='task_list'),
    path('detail/<int:pk>/', TaskDetail.as_view(), name='task_detail'),
]