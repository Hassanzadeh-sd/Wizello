from django.urls import path
from .views import (
    TaskListAPIView,
    TaskUpdateAPIView,
    TaskDeleteAPIView,
)

urlpatterns = [
    path('', TaskListAPIView.as_view(), name="tasklistAPI"),
    path('update/<int:pk>/', TaskUpdateAPIView.as_view(),
         name="taskupdateAPI"),
    path('delete/<int:pk>/', TaskDeleteAPIView.as_view(),
         name="taskdeleteAPI"),
]
