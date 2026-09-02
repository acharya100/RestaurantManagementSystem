from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from rest_framework import status

from users.models import User
from users.serializers import UserSerializer, UserRegistrationSerializer

class UserRegisterAPIView(APIView):
    def post(self, request):
        serializer = UserRegistrationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



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

            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserDetailAPIView(APIView):
    """
    custom user views containing userdetailapiview
    """
    def get(self, request, pk):
        user = get_object_or_404(User, id=pk)
        serializer = UserSerializer(user)

        return Response(serializer.data)

    def put(self, request, pk):
        user = get_object_or_404(User, id =pk)
        serializer = UserSerializer(user, data = request.data)

        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        user = get_object_or_404(User, id=pk)
        user.delete()

        return Response(status = status.HTTP_204_NO_CONTENT)