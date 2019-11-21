from django.urls import path
from .views import (
    OrganizationListAPIView,
    OrganizationCreateAPIView,
    OrganizationUpdateAPIView,
    OrganizationDeleteAPIView,)

urlpatterns = [
    path('', OrganizationListAPIView.as_view(), name="organizationlistAPI"),
    path('create/', OrganizationCreateAPIView.as_view(),
         name="organizationcreateAPI"),
    path('update/<int:pk>/', OrganizationUpdateAPIView.as_view(),
         name="organizationupdateAPI"),
    path('delete/<int:pk>/', OrganizationDeleteAPIView.as_view(),
         name="organizationdeleteAPI"),
]
