from rest_framework import serializers
from reservations.models import Reservation

class ReservationSerializer(serializers.ModelSerializer):
    """
    custom reservation serialzers
    """
    class Meta:
        model = Reservation
        fields = [
            'id', 'customer', 'restaurant',
            'status', 'table_number', 'number_of_guests',
            'reservation_date', 'reservation_time',
            'special_request', 'created_at', 'updated_at'
        ]