from django.urls import path, include
from .views import (
    RequestManagerListView, RequestManagerAcceptView,
    RequestListView, RequestCreateView, RequestDeleteView)

app_name = 'request'

urlpatterns = [
    # request
    path('', RequestListView.as_view(), name="requestlist"),
    path('manager/', RequestManagerListView.as_view(), name="requestmanagerlist"),
    path('create/', RequestCreateView.as_view(), name="requestcreate"),
    path('manager/accept/<int:pk>/',
         RequestManagerAcceptView.as_view(), name="requestaccept"),
    path('delete/<int:pk>/', RequestDeleteView.as_view(), name="requestdelete"),
]
