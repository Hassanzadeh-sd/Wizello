from rest_framework import serializers
from django.urls import reverse
from ..models import Organization


class OrganizationModelSerializer(serializers.ModelSerializer):
    employeeCount = serializers.SerializerMethodField()

    class Meta:
        model = Organization
        fields = [
            'name',
            'employeeCount',
        ]

    def get_employeeCount(self, obj):
        return obj.employee.count()
