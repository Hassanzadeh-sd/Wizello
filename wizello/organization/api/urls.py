from django.urls import path
from .views import (OrganizationListAPIView)

urlpatterns = [
    path('', OrganizationListAPIView.as_view(), name="organizationlistAPI"),
]
