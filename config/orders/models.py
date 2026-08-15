import uuid
from django.db import models
from users.models import User
from restaurants.models import Restaurant
from menus.models import Menu


class Order(models.Model):
    """
    custom order models
    """
    class Status(models.TextChoices):
        PENDING = 'PENDING', 'Pending'
        RECEIVED = 'RECEIVED', 'Received'
        PROCESSING = 'PROCESSING', 'Processing'
        READY = 'READY', 'Ready'
        DELIVERED = 'DELIVERED', 'Delivered'
        CANCELLED = 'CANCELLED', 'Cancelled'

    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable = False
    )
    customer = models.ForeignKey(
        User, on_delete=models.CASCADE,
        related_name='orders'
    )
    restaurant = models.ForeignKey(
        Restaurant, on_delete=models.CASCADE,
        related_name='orders'
    )
    status = models.CharField(
        max_length=20,
        choices = Status.choices,
        default = Status.PENDING
    )
    total_price = models.DecimalField(max_digits=16, decimal_places=2)
    description = models.TextField(blank=True)

    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Order by {self.customer.name}"


class OrderItem(models.Model):
    """
    custom order item models
    """
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
    )
    order = models.ForeignKey(
        Order, on_delete=models.CASCADE,
        related_name='orderitems'
    )
    menu = models.ForeignKey(
        Menu, on_delete=models.CASCADE,
        related_name='orderitems'
    )
    quantity = models.PositiveBigIntegerField()
    unit_price = models.DecimalField(max_digits=10, decimal_places=2)

    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.quantity} X {self.menu.name}"