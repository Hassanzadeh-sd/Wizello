from rest_framework import serializers
from ..models import Task


class TaskModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = [
            'id',
            'subject',
            'description',
            'deadline',
            'owner',
            'assignee',
        ]


class TaskUpdateModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = [
            'id',
            'deadline',
            'assignee',
        ]
