from rest_framework.views import APIView
from rest_framework.response import Response

from reviews.models import Review
from reviews.serializers import ReviewSerializer


class ReviewListAPIView(APIView):
    def get(self, request):
        reviews = Review.objects.all()
        serializer = ReviewSerializer(reviews, many = True)

        return Response(serializer.data)

    def post(self, request):
        serializer = ReviewSerializer(data = request.data)

        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data)
        return Response(serializer.errors)

class ReviewDetailAPIView(APIView):
    def put(self, request, pk):
        review = Review.objects.get(id =pk)
        serializer = ReviewSerializer(review, data = request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
    
        return Response(serializer.errors)

    def delete(self, request, pk):
        review = Review.objects.get(id=pk)
        review.delete()

        return Response(
            {
            'message': 'review deleted successfully'
            }
        )