from rest_framework import viewsets
from .serializers import TaskSerializer, ThemeSerializer
from .models import Task, Theme
from url_filter.integrations.drf import DjangoFilterBackend


class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    filter_backends = [DjangoFilterBackend]
    filter_fields = ['year', 'theme', 'type', 'zno_type']


class ThemeViewSet(viewsets.ModelViewSet):
    queryset = Theme.objects.all()
    serializer_class = ThemeSerializer
    filter_backends = [DjangoFilterBackend]
    filter_fields = ['name']