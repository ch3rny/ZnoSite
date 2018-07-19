from django.conf.urls import url, include
from rest_framework import routers
from physics import views

router = routers.DefaultRouter()
router.register(r'tasks', views.TaskViewSet)
router.register(r'theme', views.ThemeViewSet)

urlpatterns = [
    url(r'', include(router.urls)),
    url(r'api/', include('rest_framework.urls', namespace='rest_framework'))
]