from django.urls import path
from tasks.views import TaskList, TaskDetail, TaskInactive
urlpatterns = [
    path('<int:project_id>/boards/<int:board_id>/taskslists/<int:list_id>/tasks/', TaskList.as_view(), name='task_list'),
    path('<int:project_id>/boards/<int:board_id>/taskslists/<int:list_id>/tasks/<int:pk>/', TaskDetail.as_view(), name='task_detail'),
    path('<int:project_id>/boards/<int:board_id>/taskslists/<int:list_id>/tasks/inactive/<int:pk>/', TaskInactive.as_view(), name='task_inactive'),
]