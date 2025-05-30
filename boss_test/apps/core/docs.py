from rest_framework import serializers


class APIExceptionResponseSerializer(serializers.Serializer):
    detail = serializers.CharField()
    error_code = serializers.CharField()
