from rest_framework import serializers
from menus.models import  Menu

class MenuSerializer(serializers.ModelSerializer):
    """
    custom menu serializers
    """
    class Meta:
        model = Menu
        fields = [
            'id', 'name', 'description',
            'customer', 'restaurant', 'image',
            'is_available', 'price',
            'created_at', 'updated_at'
        ]
    