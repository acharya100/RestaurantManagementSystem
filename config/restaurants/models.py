import uuid
from django.db import models
from users.models import User

class Restaurant(models.Model):
    """
    custom restaurant models
    """
    id = models.UUIDField(
        primary_key= True,
        default=uuid.uuid4,
        editable = False
    )
    email = models.EmailField(unique=True)
    name = models.CharField(max_length=189)
    description = models.TextField(blank = True)
    phone_number = models.CharField(max_length=20, blank=True)
    owner = models.ForeignKey(
        User, on_delete=models.CASCADE,
        related_name='restaurants'
    )
    image = models.ImageField(
        upload_to='restaurants/',
        blank = True, null = True)
    address = models.CharField(max_length=180, blank= True)
    is_open = models.BooleanField(default=True)
    opening_time = models.TimeField()
    closing_time = models.TimeField()

    created_at = models.DateTimeField(auto_now= True)
    updated_at = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return self.name