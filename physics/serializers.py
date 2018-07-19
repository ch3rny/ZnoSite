from rest_framework import serializers
from .models import Task, Theme


class ThemeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Theme
        fields = ('name',)


class TaskSerializer(serializers.ModelSerializer):
    task_image = serializers.ImageField(use_url=True)

    class Meta:
        model = Task
        fields = ('url', 'year', 'number', 'zno_type', 'theme', 'type', 'task_image', 'correct_answer')
        depth = 1
