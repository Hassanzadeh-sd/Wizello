from rest_framework import generics
from django.db.models import Q
from rest_framework import permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import OrganizationModelSerializer
from ..models import Organization


class OrganizationListAPIView(generics.ListAPIView):
    queryset = Organization.objects.all()
    serializer_class = OrganizationModelSerializer
    permission_classes = [permissions.IsAdminUser]


class OrganizationCreateAPIView(generics.CreateAPIView):
    serializer_class = OrganizationModelSerializer
    permission_classes = [permissions.IsAdminUser]


class OrganizationUpdateAPIView(generics.UpdateAPIView):
    queryset = Organization.objects.all()
    serializer_class = OrganizationModelSerializer
    permission_classes = [permissions.IsAdminUser]


class OrganizationDeleteAPIView(generics.DestroyAPIView):
    queryset = Organization.objects.all()
    serializer_class = OrganizationModelSerializer
    permission_classes = [permissions.IsAdminUser]
