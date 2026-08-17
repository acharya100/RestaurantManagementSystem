from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from rest_framework import status
from restaurants.models import Restaurant
from restaurants.serializers import RestaurantSerializer


class RestaurantListAPIView(APIView):
    """
    custom restaurant views containing userlistapiview
    """
    def get(self, request):
        restaurants = Restaurant.objects.all()
        serializer = RestaurantSerializer(restaurants, many = True)

        return Response(serializer.data)

    def post(self, request):
        serializer = RestaurantSerializer(data = request.data)

        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class RestaurantDetailAPIView(APIView):
    """
    custom restaurant views containing userdetailapiview
    """
    def get(self, request, pk):
        restaurant = get_object_or_404(Restaurant, id=pk)
        serializer = RestaurantSerializer(restaurant)

        return Response(serializer.data)

    def put(self, request, pk):
        restaurant = get_object_or_404(Restaurant, id=pk)
        serializer = RestaurantSerializer(restaurant, data=request.data)

        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        restaurant = get_object_or_404(Restaurant, id=pk)
        restaurant.delete()

        return Response(status = status.HTTP_204_NO_CONTENT)
        