from django.contrib import admin
from .models import Request


@admin.register(Request)
class RequestAdminView(admin.ModelAdmin):
    list_display = ('organization', 'user', 'position')
