from rest_framework.views import APIView
from rest_framework.response import Response

from reservations.models import Reservation
from reservations.serializers import ReservationSerializer


class ReservationListAPIView(APIView):
    def get(self, request):
        reservations = Reservation.objects.all()
        serializer = ReservationSerializer(reservations, many = True)

        return Response(serializer.data)

    def post(self, request):
        serializer = ReservationSerializer(data = request.data)

        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data)
        return Response(serializer.errors)

class ReservationDetailAPIView(APIView):
    def put(self, request, pk):
        reservation = Reservation.objects.get(id =pk)
        serializer = ReservationSerializer(reservation, data = request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
    
        return Response(serializer.errors)

    def delete(self, request, pk):
        reservation = Reservation.objects.get(id=pk)
        reservation.delete()

        return Response(
            {
            'message': 'Reservation deleted successfully'
            }
        )