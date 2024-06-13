from django.contrib import admin
from core.models import Comment


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['comment_id', 'user', 'text_comment', 'file_link', 'commented_task', 'is_active']
