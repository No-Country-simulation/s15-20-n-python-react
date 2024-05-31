from django.urls import path
from teams.views import TeamList, TeamDetail, RoleTypeList, RoleTypeDetail, CollaboratorList, CollaboratorDetail


# Create your routes here.
urlpatterns = [
  path('team/list/', TeamList.as_view(), name='team_list'),
  path('team/detail/<int:pk>/', TeamDetail.as_view(), name='team_detail'),
  path('role/list/', RoleTypeList.as_view(), name='role_type_list'),
  path('role/detail/<int:pk>/', RoleTypeDetail.as_view(), name='role_type_detail'),
  path('collaborator/list/', CollaboratorList.as_view(), name='collaborator_list'),
  path('collaborator/detail/<int:pk>/', CollaboratorDetail.as_view(), name='collaborator_detail'),
]