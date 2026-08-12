import uuid
from django.db import models

from restaurants.models import Restaurant


class Menu(models.Model):
    """
    custom menu models
    """

    id = models.UUIDField(
        primary_key = True,
        default = uuid.uuid4,
        editable = False
        )
    restaurant = models.ForeignKey(
        Restaurant, on_delete= models.CASCADE,
        related_name= 'menus'
    )
    name = models.CharField(max_length = 125)
    price = models.DecimalField(max_digits = 12, decimal_places=2)
    description = models.TextField(blank=True, default='')
    is_available = models.BooleanField(default = True)
    image = models.ImageField(
        upload_to = 'menu',
        blank = True, null = True
    )

    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

    def __str__(self):
        return self.name