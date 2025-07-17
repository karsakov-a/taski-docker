"""Сериализаторы для API Taski."""

from rest_framework import serializers

from .models import Task


class TaskSerializer(serializers.ModelSerializer):
    """Сериализатор для модели Task."""

    class Meta:
        """class Meta Сериализатора для модели Task."""

        model = Task
        fields = ('id', 'title', 'description', 'completed')
