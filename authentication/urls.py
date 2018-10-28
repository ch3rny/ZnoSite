from django.urls import path
from rest_framework_jwt.views import refresh_jwt_token
from . import views


urlpatterns = [
    path('google/', views.GoogleLogin.as_view(), name='google_login'),
    path('refresh_token/', refresh_jwt_token)
]