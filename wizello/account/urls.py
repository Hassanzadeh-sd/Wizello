from django.urls import path
from .views import (
    EmployeeListView, EmployeeDeactiveView, EmployeeRegisterView,
    EmployeeAdminListView, EmployeeAdminDeactiveView, EmployeeAdminUpdateView)

app_name = 'account'

urlpatterns = [
    # employee
    path('employee/', EmployeeListView.as_view(), name="employeelist"),
    path('employee/register/', EmployeeRegisterView.as_view(),
         name="employeeregister"),
    path('employee/deactive/<int:pk>/', EmployeeDeactiveView.as_view(),
         name="employeedeactive"),
    # admin
    path('employee/admin/', EmployeeAdminListView.as_view(),
         name="employeeadminlist"),
    path('employee/admin/deactive/<int:pk>/', EmployeeAdminDeactiveView.as_view(),
         name="employeeadmindeactive"),
    path('employee/admin/update/<int:pk>/', EmployeeAdminUpdateView.as_view(),
         name="employeeadminupdate"),
]
