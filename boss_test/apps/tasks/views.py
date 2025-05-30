from rest_framework import viewsets, permissions
from django_filters.rest_framework import DjangoFilterBackend

from .docs import tasks_scheme
from .filters import TaskSearchFilter
from .models import Task
from .serializers import TaskSerializer


@tasks_scheme
class TaskViewSet(viewsets.ModelViewSet):
    serializer_class = TaskSerializer
    permission_classes = [permissions.IsAuthenticated]

    filter_backends = [DjangoFilterBackend, TaskSearchFilter]
    filterset_fields = ['completed']
    search_fields = ['title']
    ordering_fields = ['id', 'created_at']
    ordering = ['-id']

    def get_queryset(self):
        return Task.objects.filter(user=self.request.user.id).order_by('-created_at')

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
