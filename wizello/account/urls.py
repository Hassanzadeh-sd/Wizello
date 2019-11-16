from django.urls import path
from .views import (
    AccountListView, AccountDeactiveView)

app_name = 'account'

urlpatterns = [
    # request
    path('', AccountListView.as_view(), name="accountlist"),
    path('deactive/<int:pk>/', AccountDeactiveView.as_view(), name="accountdeactive"),
]
