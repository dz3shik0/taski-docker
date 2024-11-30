"""Views."""
from rest_framework import status, viewsets
from rest_framework.response import Response

from .models import Task
from .serializers import TaskSerializer


class TaskView(viewsets.ModelViewSet):
    """Вьювсет модели Task."""

    serializer_class = TaskSerializer
    queryset = Task.objects.all()

    def destroy(self, *args, **kwargs):
        """Удаляет указанный объект и возвращает его сериализованные данные."""
        serializer = self.get_serializer(self.get_object())
        super().destroy(*args, **kwargs)
        return Response(serializer.data, status=status.HTTP_200_OK)
