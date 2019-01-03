from rest_framework import serializers
from .models import Task, Theme, Bundle, TestAnswer


class ThemeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Theme
        fields = ('name',)


class TaskSerializer(serializers.ModelSerializer):
    task_image = serializers.ImageField(use_url=False, label='Завдання')

    class Meta:
        model = Task
        fields = ('id', 'url', 'year', 'number', 'zno_type', 'theme', 'type', 'task_image', 'correct_answer')
        depth = 1


class BundleSerializer(serializers.ModelSerializer):
    cover = serializers.ImageField(use_url=False, label='Обкладинка', allow_empty_file=True, allow_null=True, required=False)

    class Meta:
        model = Bundle
        fields = ('id', 'url', 'name', 'cover', 'author_id', 'created_date', 'edited_date', 'tasks', 'shared')


class TestAnswerSerializer(serializers.ModelSerializer):
    theme = serializers.SlugRelatedField(
        slug_field='name',
        queryset=Theme.objects.all().order_by('id')
     )

    class Meta:
        model = TestAnswer
        fields = ('id', 'url', 'user', 'task', 'theme', 'user_answer', 'is_true', 'date')


class ReadTestSerializer(serializers.ModelSerializer):
    theme = serializers.SlugRelatedField(
        slug_field='name',
        queryset=Theme.objects.all().order_by('id')
     )
    user = serializers.PrimaryKeyRelatedField(read_only=True)
    task = TaskSerializer()

    class Meta:
        model = TestAnswer
        fields = ('id', 'url', 'user', 'task', 'theme', 'user_answer', 'is_true', 'date')
        depth = 1
