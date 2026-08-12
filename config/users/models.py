import uuid
from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    """
    custom user models
    """
    class Role(models.TextChoices):
        ADMIN = 'ADMIN', 'Administrator'
        OWNER = 'OWNER', 'Owner'
        MANAGER = 'MANAGER', 'Manager'
        CHEF = 'CHEF', 'Chef'
        WAITER = 'WAITER', 'Waiter'
        CASHIER = 'CASHIER', 'Cashier'
        CUSTOMER = 'CUSTOMER', 'Customer'

    id = models.UUIDField(
        primary_key = True,
        default = uuid.uuid4,
        editable = False
    )
    email = models.EmailField(unique = True)
    phone_number = models.CharField(max_length=20, blank = True)
    date_of_birth = models.DateField(blank = True, null = True)
    bio = models.TextField(blank = True)
    image = models.ImageField(
        upload_to = 'profiles/',
        blank = True, null = True)
    role = models.CharField(
        max_length =20,
        choices = Role.choices,
        default = Role.CUSTOMER
    )

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.email