from django.contrib import admin

from boss_media_group.apps.tasks.models import Task


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'completed', 'created_at')
    list_filter = ('completed',)
    search_fields = ('title',)
