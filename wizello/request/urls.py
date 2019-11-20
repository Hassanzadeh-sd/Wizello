from django.urls import path, include
from .views import (
    RequestManagerListView, RequestManagerAcceptView,
    RequestListView, RequestCreateView, RequestDeleteView,
    RequestAdminListView, RequestAdminAcceptView)

app_name = 'request'

urlpatterns = [
    # request
    path('', RequestListView.as_view(), name="requestlist"),
    path('create/', RequestCreateView.as_view(), name="requestcreate"),
    path('delete/<int:pk>/', RequestDeleteView.as_view(), name="requestdelete"),
    # Manager
    path('manager/', RequestManagerListView.as_view(), name="requestmanagerlist"),
    path('manager/accept/<int:pk>/',
         RequestManagerAcceptView.as_view(), name="requestaccept"),
    # Admin
    path('admin/', RequestAdminListView.as_view(), name="requestadminlist"),
    path('admin/accept/<int:pk>/',
         RequestAdminAcceptView.as_view(), name="requestadminaccept"),
]
