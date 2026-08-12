import uuid
from django.db import models
from users.models import User
from restaurants.models import Restaurant
from menu.models import Menu


class Order(models.Model):
    """
    custom order models
    """
    class Status(models.TextChoices):
        PENDING = 'PENDING', 'pending'
        RECEIVED = 'RECEIVED', 'received'
        PROCESSING = 'PROCESSING', 'processing'
        READY = 'READY', 'ready'
        DELIVERED = 'DELIVERED', 'delivered'
        CANCELLED = 'CANCELLED', 'cancelled'

    id = models.UUIDField(
        primary_key = True,
        default = uuid.uuid4,
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
    description = models.TextField(blank=True, default='')
    status = models.CharField(
        max_length = 20,
        choices = Status.choices,
        default = Status.PENDING
    )
    total_price = models.DecimalField(max_digits=16, decimal_places=2)

    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

    def __str__(self):
        return f"Order by {self.customer.email}"


class OrderItem(models.Model):
    """
    custom order item models
    """
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )
    order = models.ForeignKey(
        Order, on_delete=models.CASCADE,
        related_name='order_items',
        blank = True, null = True
    )
    menu = models.ForeignKey(
        Menu, on_delete=models.CASCADE,
        related_name='order_items'
    )
    unit_price = models.DecimalField(max_digits=12, decimal_places=2)
    quantity = models.PositiveIntegerField(default=1)

    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

    def __str__(self):
        return f"{self.quantity} x {self.menu.name}"
