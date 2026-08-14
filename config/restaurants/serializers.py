from rest_framework import serializers
from restaurants.models import Restaurant

class RestaurantSerializer(serializers.ModelSerializer):
    """
    custom restaurant serializers
    """
    class Meta:
        model = Restaurant
        fields = [
            'id', 'email', 'name',
            'description', 'phone_number', 'owner',
            'image', 'address', 'is_open', 'opening_time',
            'closing_time', 'created_at', 'updated_at'
        ]