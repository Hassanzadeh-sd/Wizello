from django.urls import path, include
from .views import (
    OrganizationListView, OrganizationCreateView,
    OrganizationUpdateView, OrganizationDeleteView
)

app_name = 'organization'

urlpatterns = [
    path('', OrganizationListView.as_view(), name="organizationlist"),
    path('create/', OrganizationCreateView.as_view(), name="organizationcreate"),
    path('update/<int:pk>/', OrganizationUpdateView.as_view(),
         name="organizationupdate"),
    path('delete/<int:pk>/', OrganizationDeleteView.as_view(),
         name="organizationdelete"),
]
