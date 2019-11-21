from django.db.models import Q
from django.shortcuts import get_object_or_404
from rest_framework import generics
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


class EmployeeDeactiveAPIView(APIView):
    permission_classes = (permissions.IsAdminUser,)

    def get(self, request, pk, format=None):
        obj_employee = get_object_or_404(Employee, pk=pk)
        obj_employee.organization = None
        obj_employee.position = "E"
        obj_employee.save()
        message = "Deactive User"
        return Response({"message": message}, status=400)
