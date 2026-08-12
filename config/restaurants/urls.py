from django.urls import path
from restaurants.views import RestaurantListAPIView, RestaurantDetailAPIView

urlpatterns = [
    path('restaurants/', RestaurantListAPIView.as_view(), name = 'restaurant-list'),
    path('restaurants/<uuid:pk>/', RestaurantDetailAPIView.as_view(), name = 'restaurant-detail')
]