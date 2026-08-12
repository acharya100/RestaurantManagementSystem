from rest_framework import serializers
from reviews.models import Review

class ReviewSerializer(serializers.ModelSerializer):
    """
    custom review serializers
    """
    class Meta:
        model = Review
        fields = [
            'id', 'customer', 'restaurant',
            'rating', 'comment',
            'updated_at', 'created_at'
        ]