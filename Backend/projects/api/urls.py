
from django.urls import path
#from projects.api.views import ProjectCreateView, ProjectUpdateView, ProjectDetailView, ProjectListView ,  ProjectDeleteView , ProjectListApi
from projects.api.views import ProjectListCreateApiView , ProjectDetailCreateApiView
urlpatterns = [
    path('list/',ProjectListCreateApiView.as_view(), name = 'project_list' ),
    path('detail/<int:pk>/',ProjectDetailCreateApiView.as_view(), name = 'project_detail' ),
]
