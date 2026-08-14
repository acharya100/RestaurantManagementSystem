import uuid
from django.db import models
from users.models import User
from restaurants.models import Restaurant


class Reservation(models.Model):
    """
    custom reservation models
    """
    class State(models.TextChoices):
        PENDING = 'PENDING', 'Pending'
        BOOKED = 'BOOKED', 'Booked'
        OPEN = 'OPEN', 'Open'
        CANCELLED = 'CANCELLED', 'Cancelled'

    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )
    customer = models.ForeignKey(
        User, on_delete=models.CASCADE,
        related_name='reservations'
    )
    restaurant = models.ForeignKey(
        Restaurant, on_delete=models.CASCADE,
        related_name='reservations'
    )
    table_number = models.PositiveIntegerField(default=1)
    number_of_guests = models.PositiveBigIntegerField(default=1)
    table_name = models.CharField(max_length=150, blank = True)
    state = models.CharField(
        max_length=20,
        choices = State.choices,
        default = State.OPEN
    )
    reservation_date = models.DateField()
    reservation_time = models.TimeField()
    special_request = models.CharField(max_length=500, blank=True)

    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Table Number {self.table_number} for {self.customer.name}"