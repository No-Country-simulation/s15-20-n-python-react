from django.contrib import admin
from core.models import TasksList


@admin.register(TasksList)
class TasksListAdmin(admin.ModelAdmin):
    list_display = ['list_id', 'title', 'description', 'membership_board', 'is_active']

