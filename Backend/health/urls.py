from django.urls import path
from . import views

urlpatterns = [
    path("", views.HealthListView.index, name="index"),
]
