from rest_framework import serializers
from django.urls import reverse
from ..models import Employee


class EmployeeModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = [
            'id',
            'user',
            'organization',
            'position',
        ]
