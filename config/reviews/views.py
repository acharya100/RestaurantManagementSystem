from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from rest_framework import status
from reviews.models import Review
from reviews.serializers import ReviewSerializer


class ReviewListAPIView(APIView):
    """
    custom review views for reviewlistapiview
    """
    def get(self, request):
        reviews = Review.objects.all()
        serializer = ReviewSerializer(reviews, many = True)

        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def post(self, request):
        serializer = ReviewSerializer(data= request.data)

        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)


class ReviewDetailAPIView(APIView):
    """
    custom review views for reviewdetailapiview
    """
    def get(self, request,pk):
        review = get_object_or_404(Review, id=pk)
        serializer = ReviewSerializer(review)

        return Response(serializer.data, status=status.HTTP_201_CREATED)


    def put(self, request, pk):
        review = get_object_or_404(Review, id=pk)
        serializer = ReviewSerializer(review, data = request.data)

        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        review = get_object_or_404(Review, id=pk)
        review.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)
    