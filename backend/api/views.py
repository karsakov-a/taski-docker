"""Представления (views) для API Taski."""

from rest_framework import status, viewsets
from rest_framework.response import Response

from .models import Task
from .serializers import TaskSerializer


class TaskView(viewsets.ModelViewSet):
    """API эндпоинт для управления задачами."""

    serializer_class = TaskSerializer
    queryset = Task.objects.all()

    def destroy(self, *args, **kwargs):
        """Функция destroy."""
        serializer = self.get_serializer(self.get_object())
        super().destroy(*args, **kwargs)
        return Response(serializer.data, status=status.HTTP_200_OK)
