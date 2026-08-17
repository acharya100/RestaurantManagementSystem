from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from rest_framework import status
from menus.models import Menu
from menus.serializers import MenuSerializer


class MenuListAPIView(APIView):
    """
    custom menu views containing userlistapiview
    """
    def get(self, request):
        menus = Menu.objects.all()
        serializer = MenuSerializer(menus, many = True)

        return Response(serializer.data)

    def post(self, request):
        serializer = MenuSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class MenuDetailAPIView(APIView):
    """
    custom menu views containing userdetailapiview
    """
    def get(self, request, pk):
        menu = get_object_or_404(Menu, id=pk)
        serializer = MenuSerializer(menu)

        return Response(serializer.data)

    def put(self, request, pk):
        menu = get_object_or_404(Menu, id=pk)
        serializer = MenuSerializer(menu, data=request.data)

        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        menu = get_object_or_404(Menu, id=pk)
        menu.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)