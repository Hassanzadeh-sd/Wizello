from django.urls import path, include
from .views import (
    RequestListView, RequestCreateView, RequestAcceptView, RequestDeleteView)

app_name = 'request'

urlpatterns = [
    # request
    path('', RequestListView.as_view(), name="requestlist"),
    path('create/', RequestCreateView.as_view(), name="requestcreate"),
    path('accept/<int:pk>/', RequestAcceptView.as_view(), name="requestaccept"),
    path('delete/<int:pk>/', RequestDeleteView.as_view(), name="requestdelete"),
]
