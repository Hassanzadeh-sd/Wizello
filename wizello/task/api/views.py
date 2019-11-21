from django.db.models import Q
from django.shortcuts import get_object_or_404
from rest_framework import generics
from rest_framework import permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import TaskModelSerializer, TaskUpdateModelSerializer
from ..models import Task


class TaskListAPIView(generics.ListAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskModelSerializer
    permission_classes = [permissions.IsAdminUser]


class TaskUpdateAPIView(generics.UpdateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskUpdateModelSerializer
    permission_classes = [permissions.IsAdminUser]


class TaskDeleteAPIView(generics.DestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskModelSerializer
    permission_classes = [permissions.IsAdminUser]
