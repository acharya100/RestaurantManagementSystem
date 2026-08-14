from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import get_object_or_404

from reservations.models import Reservation
from reservations.serializers import ReservationSerializer


class ReservationListAPIView(APIView):
    """
    custom reservation views for reservationlistapiview
    """
    def get(self, request):
        reservations = Reservation.objects.all()
        serializer = ReservationSerializer(reservations, many = True)

        return Response(serializer.data)

    def post(self, request):
        serializer = ReservationSerializer(data= request.data)

        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data)
        return Response(serializer.errors)


class ReservationDetailAPIView(APIView):
    """
    custom reservation views for reservationdetailapiview
    """
    def put(self, request, pk):
        reservation = get_object_or_404(Reservation, id=pk)
        serializer = ReservationSerializer(reservation, data = request.data)

        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data)
        return Response(serializer.errors)

    def delete(self, request,pk):
        reservation = get_object_or_404(Reservation, id=pk)
        reservation.delete()

        return Response(status = 204)