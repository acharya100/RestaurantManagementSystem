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
            'description', 'status', 'total_price',
            'created_at', 'updated_at'
        ]


class OrderItemSerializer(serializers.ModelSerializer):
    """
    custom order item serializers
    """
    class Meta:
        model = OrderItem
        fields = [
            'id', 'order', 'menu',
            'unit_price', 'quantity',
            'created_at', 'updated_at'
        ]