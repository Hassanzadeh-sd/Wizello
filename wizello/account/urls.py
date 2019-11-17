from django.urls import path
from .views import (
    EmployeeListView, EmployeeDeactiveView, EmployeeRegisterView)

app_name = 'account'

urlpatterns = [
    # employee
    path('employee/', EmployeeListView.as_view(), name="employeelist"),
    path('employee/register/', EmployeeRegisterView.as_view(),
         name="employeeregister"),
    path('employee/deactive/<int:pk>/', EmployeeDeactiveView.as_view(),
         name="employeedeactive"),
]
