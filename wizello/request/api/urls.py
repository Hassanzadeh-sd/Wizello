from django.urls import path
from .views import (
    RequestListAPIView,
    RequestAcceptAPIView,
    RequestDeleteAPIView,
)

urlpatterns = [
    path('', RequestListAPIView.as_view(), name="requestlistAPI"),
    path('accept/<int:pk>/', RequestAcceptAPIView.as_view(),
         name="requestacceptAPI"),
    path('delete/<int:pk>/', RequestDeleteAPIView.as_view(),
         name="requestdeleteAPI"),
]
