from django.contrib import admin
from .models import Task, Comment

# Register your models here.

#========================TASK ADMIN========================
@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'status', 'due_date', 'created_at', 'updated_at', 'user')
    list_filter = ('status', 'due_date')
    search_fields = ('title',)

#==========================COMMENT ADMIN=====================
@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('text',)
    list_filter = ('task', 'user', 'created_at')
    search_fields = ('created_at',)