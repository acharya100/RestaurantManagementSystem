import uuid
from django.db import models
from users.models import User
from restaurants.models import Restaurant

class Reservation(models.Model):
    """
    custom reservation models
    """
    class Status(models.TextChoices):
        PENDING = 'PENDING', 'pending'
        RESERVED = 'RESERVED', 'reserved'
        CANCELLED = 'CANCELLED', 'cancelled'

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
    status = models.CharField(
        max_length=20,
        choices=Status.choices,
        default=Status.PENDING
    )
    table_number = models.PositiveIntegerField(default = 1)
    number_of_guests = models.PositiveIntegerField(default = 1)
    reservation_date = models.DateField()
    reservation_time = models.TimeField()
    special_request = models.TextField(blank = True)

    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

    def __str__(self):
        return f"Reservation{self.id} - Table {self.table_number}"