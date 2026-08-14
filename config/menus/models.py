import uuid
from django.db import models
from users.models import User
from restaurants.models import Restaurant


class Menu(models.Model):
    """
    custom menu models
    """
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    customer = models.ForeignKey(
        User, on_delete=models.CASCADE,
        related_name='menus'
    )
    restaurant = models.ForeignKey(
        Restaurant, on_delete=models.CASCADE,
        related_name='menus'
    )
    image = models.ImageField(
        upload_to='menus',
        blank= True, null=True
    )
    is_available = models.BooleanField(default=True)
    price = models.DecimalField(max_digits=11, decimal_places=2)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name