from django.urls import path
from reviews.views import ReviewListAPIView, ReviewDetailAPIView

urlpatterns = [
    path('reviews/', ReviewListAPIView.as_view(), name = 'review-list'),
    path('reviews/<uuid:pk>/', ReviewDetailAPIView.as_view(), name = 'review-detail')
]
