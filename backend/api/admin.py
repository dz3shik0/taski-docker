"""Admin configuration for the Task model.

This module registers the Task model in the Django admin panel
and customizes its display options.
"""
from django.contrib import admin
from .models import Task


class TaskAdmin(admin.ModelAdmin):
    """Настройки админ-панели для модели Task."""

    list_display = ('title', 'description', 'completed')


admin.site.register(Task, TaskAdmin)
