from rest_framework import serializers
from .models import Review


class ReviewSerializer(serializers.ModelSerializer):
    attachment = serializers.FileField(use_url=False)

    class Meta:
        model = Review
        fields = '__all__'

    def create(self, validated_data):
        return Review.objects.create(**validated_data)

