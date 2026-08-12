from rest_framework.views import APIView
from rest_framework.response import Response

from menu.models import Menu
from menu.serializers import MenuSerializer

class MenuListAPIView(APIView):
    def get(self, request):
        menus = Menu.objects.all()
        serializer = MenuSerializer(menus, many = True)

        return Response(serializer.data)

    def post(self, request):
        serializer = MenuSerializer(data = request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors) 


class MenuDetailAPIView(APIView):
    def put(self, request, pk):
        menu = Menu.objects.get(id = pk)
        serializer = MenuSerializer(menu, data = request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors)

    def delete(self, request, pk):
        menu = Menu.objects.get(id = pk)
        menu.delete()

        return Response({
            'message': 'Menu deleted successfully'
        })