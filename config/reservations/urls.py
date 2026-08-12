from django.urls import path
from reservations.views import ReservationListAPIView, ReservationDetailAPIView

urlpatterns = [
    path('reservations/', ReservationListAPIView.as_view(), name = 'reservation-list'),
    path('reservations/<uuid:pk>/', ReservationDetailAPIView.as_view(), name = 'reservation-detail')
]
