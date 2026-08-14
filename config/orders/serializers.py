from rest_framework import serializers
from orders.models import Order, OrderItem

class OrderSerializer(serializers.ModelSerializer):
    """
    custom order serializers
    """
    class Meta:
        model = Order
        fields = [
            'id', 'customer', 'restaurant',
            'status', 'total_price',
            'description', 'created_at', 'updated_at'
        ]

class OrderItemSerializer(serializers.ModelSerializer):
    """
    custom order item serializers
    """
    class Meta:
        model = OrderItem
        fields = [
            'id', 'order', 'menu', 'quantity',
            'unit_price', 'created_at', 'updated_at'
        ]