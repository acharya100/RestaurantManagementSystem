from rest_framework import serializers
from restaurants.models import Restaurant

class RestaurantSerializer(serializers.ModelSerializer):
    """
    custom restaurant serializers
    """
    class Meta:
        model = Restaurant
        fields = [
            'id', 'name', 'description',
            'email', 'phone_number', 'owner',
            'is_opened', 'address', 'opening_time',
            'closing_time', 'created_at', 'updated_at'
        ]