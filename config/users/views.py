from rest_framework.views import APIView
from rest_framework.response import Response

from users.models import User
from users.serializers import UserSerializer


class UserListAPIView(APIView):
    def get(self, request):
        users = User.objects.all()
        serializer = UserSerializer(users, many = True)

        return Response(serializer.data)

    def post(self, request):
        serializer = UserSerializer(data = request.data)

        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data)
        return Response(serializer.errors)

class UserDetailAPIView(APIView):
    def put(self, request, pk):
        user = User.objects.get(id =pk)
        serializer = UserSerializer(user, data = request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
    
        return Response(serializer.errors)

    def delete(self, request, pk):
        user = User.objects.get(id=pk)
        user.delete()

        return Response(
            {
            'message': 'user deleted successfully'
            }
        )