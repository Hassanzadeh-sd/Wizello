from django.urls import path, include
from .views import (
    IndexView)

app_name = 'core'

urlpatterns = [
    path('dashboard/', IndexView.as_view(), name="home"),
    path('', include('django.contrib.auth.urls')),
]
