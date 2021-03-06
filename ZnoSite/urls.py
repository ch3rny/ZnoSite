"""ZnoSite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from physics import urls as physicsUrls
from feedback import urls as feedbackUrls
from rest_framework.documentation import include_docs_urls

routeLists = [
    physicsUrls.routeList,
    feedbackUrls.routeList,
]

router = routers.DefaultRouter()
for routeList in routeLists:
    for route in routeList:
        router.register(route[0], route[1])

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('auth/', include('authentication.urls')),
    path('accounts/', include('allauth.urls')),
    path('docs/', include_docs_urls(title='My API title'))
]
