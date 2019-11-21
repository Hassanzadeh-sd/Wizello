from django.urls import path
from .views import (
    EmployeeListAPIView,
    EmployeeUpdateAPIView,
    EmployeeDeactiveAPIView,
)

urlpatterns = [
    path('', EmployeeListAPIView.as_view(), name="employeelistAPI"),
    path('update/<int:pk>/', EmployeeUpdateAPIView.as_view(),
         name="employeedeactiveAPI"),
    path('deactive/<int:pk>/', EmployeeDeactiveAPIView.as_view(),
         name="employeedeleteAPI"),
]
