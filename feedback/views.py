from rest_framework import viewsets
from .serializers import ReviewSerializer
from .models import Review


class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all().order_by('created_time')
    serializer_class = ReviewSerializer
