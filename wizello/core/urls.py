from django.urls import path, include
from .views import (
    DashboardView,
    IndexView)

app_name = 'core'

urlpatterns = [
    path('dashboard/', DashboardView.as_view(), name="home"),
    path('', include('django.contrib.auth.urls')),
    path('', IndexView.as_view(), name="index"),
]
