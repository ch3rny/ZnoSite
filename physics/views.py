from rest_framework import viewsets
from .serializers import TaskSerializer, ThemeSerializer, BundleSerializer
from .models import Task, Theme, Bundle
from url_filter.integrations.drf import DjangoFilterBackend


class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all().order_by('number')
    serializer_class = TaskSerializer
    filter_backends = [DjangoFilterBackend]
    filter_fields = ['id', 'year', 'theme', 'type', 'zno_type']


class ThemeViewSet(viewsets.ModelViewSet):
    queryset = Theme.objects.all().order_by('id')
    serializer_class = ThemeSerializer
    filter_backends = [DjangoFilterBackend]
    filter_fields = ['name']


class BundleViewSet(viewsets.ModelViewSet):
    queryset = Bundle.objects.all().order_by('-edited_date')
    serializer_class = BundleSerializer
    filter_backends = [DjangoFilterBackend]
    filter_fields = ['author_id', 'shared']
