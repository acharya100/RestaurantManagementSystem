import uuid
from django.db import models
from users.models import User
from restaurants.models import Restaurant

class Review(models.Model):
    """
    custom review models
    """
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable= False
    )
    customer = models.ForeignKey(
        User, on_delete=models.CASCADE,
        related_name='reviews'
    )
    restaurant = models.ForeignKey(
        Restaurant, on_delete=models.CASCADE,
        related_name='reviews'
    )
    rating = models.FloatField()
    comment = models.CharField(max_length=200, blank=True, default='')

    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

    def __str__(self):
        return f"{self.restaurant.name} - {self.rating} stars"