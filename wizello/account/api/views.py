from rest_framework import generics
from django.db.models import Q
from rest_framework import permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import EmployeeModelSerializer
from ..models import Employee


class EmployeeListAPIView(generics.ListAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeModelSerializer
    permission_classes = [permissions.IsAdminUser]


class EmployeeUpdateAPIView(generics.UpdateAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeModelSerializer
    permission_classes = [permissions.IsAdminUser]


class EmployeeDeactiveAPIView(generics.DestroyAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeModelSerializer
    permission_classes = [permissions.IsAdminUser]
