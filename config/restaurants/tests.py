import datetime

from django.test import TestCase

from restaurants.models import Restaurant
from users.models import User


class RestaurantModelTests(TestCase):
    def test_restaurant_can_be_created_without_description(self):
        owner = User.objects.create_user(
            username='restaurant-owner',
            email='restaurant-owner@example.com',
            password='strong-password-123',
            role=User.Role.OWNER,
        )

        restaurant = Restaurant.objects.create(
            name='Sample Restaurant',
            email='sample@example.com',
            owner=owner,
            opening_time=datetime.time(9, 0),
            closing_time=datetime.time(22, 0),
        )

        self.assertEqual(restaurant.description, '')
        self.assertTrue(restaurant)
