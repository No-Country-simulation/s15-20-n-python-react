
from django.urls import path
from projects.api.views import ProjectCreateView, ProjectUpdateView, ProjectDetailView, ProjectListView ,  ProjectDeleteView

urlpatterns = [
    path('create/', ProjectCreateView.as_view(), name='projects-create'), #postman
    path('my_projects/', ProjectListView.as_view(), name='my_projects-list'), #postman
    path('my_project/<int:pk>', ProjectDetailView.as_view(), name='my_project-id'),#postman
    path('my_project/update/<int:pk>', ProjectUpdateView.as_view(), name='projects-update'), #postman
    path('my_project/delete/<int:pk>', ProjectDeleteView.as_view(),name= 'projects-delete') #postman
]


