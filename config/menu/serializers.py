from rest_framework import serializers
from menu.models import Menu

class MenuSerializer(serializers.ModelSerializer):
    """
    custom menu serializers
    """
    class Meta:
        model = Menu
        fields = [
            'id', 'restaurant', 'name',
            'price', 'description', 'is_available',
            'image', 'created_at', 'updated_at'
        ]