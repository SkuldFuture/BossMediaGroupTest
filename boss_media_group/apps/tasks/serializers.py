from rest_framework import serializers

from boss_media_group.apps.tasks.models import Task


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'
        read_only_fields = ['user', 'created_at', 'updated_at']
