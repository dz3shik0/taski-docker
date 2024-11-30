"""Сериализаторы."""
from rest_framework import serializers

from .models import Task


class TaskSerializer(serializers.ModelSerializer):
    """Сериализатор модели Task."""

    class Meta:
        """class Meta."""

        model = Task
        fields = ('id', 'title', 'description', 'completed')
