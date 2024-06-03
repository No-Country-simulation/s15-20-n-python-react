
from django.urls import path
from projects.api.views import ProjectCreateView, ProjectUpdateView, ProjectDetailView, ProjectListView ,  ProjectDeleteView 

urlpatterns = [
    path('', ProjectListView.as_view(), name='project-list'), #ok
    path('create/', ProjectCreateView.as_view(), name='project-create'), #ok
    path('<int:pk>/', ProjectDetailView.as_view(), name='project-detail'),# ok
    path('<int:pk>/update/', ProjectUpdateView.as_view(), name='project-update'), #ok
    path('<int:pk>/delete/', ProjectDeleteView.as_view(), name='project-delete'), #ok
]


