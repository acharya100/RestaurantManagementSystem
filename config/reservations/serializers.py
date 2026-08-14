from rest_framework import serializers
from reservations.models import Reservation

class ReservationSerializer(serializers.ModelSerializer):
    """
    custom reservation serialzers
    """
    class Meta:
        model = Reservation
        fields = [
            'id', 'customer', 'restaurant', 'table_name',
            'state', 'table_number', 'number_of_guests',
            'reservation_date', 'reservation_time',
            'special_request', 'created_at', 'updated_at'
        ]