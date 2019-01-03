from rest_framework import viewsets
from .serializers import *
from .models import Task, Theme, Bundle, TestAnswer
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


class TestAnswerViewSet(viewsets.ModelViewSet):
    queryset = TestAnswer.objects.all().order_by('-date')
    serializer_class = TestAnswerSerializer
    filter_backends = [DjangoFilterBackend]
    filter_fields = ['user']


class ReadTestAnswerViewSet(viewsets.ModelViewSet):
    queryset = TestAnswer.objects.all().order_by('-date')
    serializer_class = ReadTestSerializer
    filter_backends = [DjangoFilterBackend]
    filter_fields = ['user']
