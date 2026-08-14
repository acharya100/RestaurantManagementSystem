from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import get_object_or_404

from users.models import User
from users.serializers import UserSerializer


class UserListAPIView(APIView):
    """
    custom user views containing userlistapiview
    """
    def get(self, request):
        users = User.objects.all()
        serializer = UserSerializer(users, many = True)

        return Response(serializer.data)

    def post(self, request):
        serializer = UserSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data)
        return Response(serializer.errors)


class UserDetailAPIView(APIView):
    """
    custom user views containing userdetailapiview
    """
    def put(self, request, pk):
        user = get_object_or_404(User, id =pk)
        serializer = UserSerializer(user, data = request.data)

        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data)
        return Response(serializer.errors)

    def delete(self, request, pk):
        user = get_object_or_404(User, id=pk)
        user.delete()

        return Response(status = 204)