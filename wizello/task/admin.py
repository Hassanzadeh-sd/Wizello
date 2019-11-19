from django.contrib import admin
from .models import Task


@admin.register(Task)
class TaskAdminView(admin.ModelAdmin):
    list_display = ('subject', 'owner', 'deadline', 'get_assignee')
    fields = ['deadline', 'assignee']
