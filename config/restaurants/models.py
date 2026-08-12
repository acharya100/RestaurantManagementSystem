import uuid
from django.db import models
from users.models import User


class Restaurant(models.Model):
    """
    custom restaurant models
    """
    id = models.UUIDField(
        primary_key = True,
        default = uuid.uuid4,
        editable = False
    )
    name = models.CharField(max_length = 170)
    description = models.TextField(blank=True, default='')
    email = models.EmailField(unique = True)
    phone_number = models.CharField(max_length = 20, blank = True)
    owner = models.ForeignKey(
        User, on_delete = models.CASCADE,
        related_name = 'restaurants'
    )
    is_opened = models.BooleanField(default = True)
    address = models.CharField(max_length = 100, blank = True)
    opening_time = models.TimeField()
    closing_time = models.TimeField()

    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

    def __str__(self):
        return self.name