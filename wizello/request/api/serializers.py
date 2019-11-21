from rest_framework import serializers
from ..models import Request


class RequestModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Request
        fields = [
            'id',
            'organization',
            'position',
            'user',
            'agreement',
        ]
