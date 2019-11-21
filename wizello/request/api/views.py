from django.db.models import Q
from django.shortcuts import get_object_or_404
from django.utils import timezone
from rest_framework import generics
from rest_framework import permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import RequestModelSerializer
from ..models import Request, Employee


class RequestListAPIView(generics.ListAPIView):
    serializer_class = RequestModelSerializer
    permission_classes = [permissions.IsAdminUser]

    def get_queryset(self):
        qs = Request.objects.filter(
            position="M").filter(user__employee__organization=None).filter(agreement=None)
        return qs


class RequestAcceptAPIView(APIView):
    permission_classes = (permissions.IsAdminUser,)

    def get(self, request, pk, format=None):
        obj_request = get_object_or_404(Request, pk=pk)
        obj_request.agreement = timezone.now()
        objEmployee = Employee.objects.get(user=obj_request.user)
        objEmployee.position = obj_request.position
        objEmployee.organization = obj_request.organization
        objEmployee.save()
        obj_request.save()
        message = "Change User Position"
        return Response({"message": message}, status=400)


class RequestDeleteAPIView(generics.DestroyAPIView):
    queryset = Request.objects.all()
    serializer_class = RequestModelSerializer
    permission_classes = [permissions.IsAdminUser]
