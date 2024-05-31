from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from users.views import UserList, UserDetail

# Create your routes here.
urlpatterns = [
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('list/', UserList.as_view(), name='user_list'),
    path('detail/<int:pk>/', UserDetail.as_view(), name='user_detail'),
]
