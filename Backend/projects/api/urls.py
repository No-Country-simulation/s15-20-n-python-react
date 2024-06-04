
from django.urls import path
#from projects.api.views import ProjectCreateView, ProjectUpdateView, ProjectDetailView, ProjectListView ,  ProjectDeleteView , ProjectListApi
from projects.api.views import ProjectListCreateApiView , ProjectDetailCreateApiView
urlpatterns = [
    path('list/',ProjectListCreateApiView.as_view(), name = 'project_list' ),
    path('detail/<int:pk>/',ProjectDetailCreateApiView.as_view(), name = 'project_detail' ),
]


"""
urlpatterns = [
    path('list/', ProjectListView.as_view(), name='project-list'), #ok
    path('list/', ProjectCreateView.as_view(), name='project-create'), #ok
    path('detail/<int:pk>/', ProjectDetailView.as_view(), name='project-detail'),# ok
    path('detail/<int:pk>/', ProjectUpdateView.as_view(), name='project-update'), #ok
    path('detail/<int:pk>/', ProjectDeleteView.as_view(), name='project-delete'), #ok
]

"""


