from rest_framework import serializers

from boss_test.apps.parser.models import TechCompany


class TechCompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = TechCompany
        fields = '__all__'
