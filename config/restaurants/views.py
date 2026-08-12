from rest_framework.views import APIView
from rest_framework.response import Response

from restaurants.models import Restaurant
from restaurants.serializers import RestaurantSerializer


class RestaurantListAPIView(APIView):
    def get(self, request):
        restaurants = Restaurant.objects.all()
        serializer = RestaurantSerializer(restaurants, many = True)

        return Response(serializer.data)

    def post(self, request):
        serializer = RestaurantSerializer(data = request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors)

class RestaurantDetailAPIView(APIView):
    def put(self, request, pk):
        restaurant = Restaurant.objects.get(id = pk)
        serializer = RestaurantSerializer(restaurant, data = request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors)

    def delete(self, request, pk):
        restaurant = Restaurant.objects.get(id=pk)
        restaurant.delete()

        return Response(
            {
                'message': 'Restaurant deleted successfully'
            }
        )