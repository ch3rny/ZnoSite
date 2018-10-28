from physics import views


routeList = (
    (r'tasks', views.TaskViewSet),
    (r'theme', views.ThemeViewSet),
    (r'bundles', views.BundleViewSet)
)
