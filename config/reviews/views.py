from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import get_object_or_404

from reviews.models import Review
from reviews.serializers import ReviewSerializer


class ReviewListAPIView(APIView):
    """
    custom review views for reviewlistapiview
    """
    def get(self, request):
        reviews = Review.objects.all()
        serializer = ReviewSerializer(reviews, many = True)

        return Response(serializer.data)

    def post(self, request):
        serializer = ReviewSerializer(data= request.data)

        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data, status = 201)
        return Response(serializer.errors, status = 400)


class ReviewDetailAPIView(APIView):
    """
    custom review views for reviewdetailapiview
    """
    def get(self, request,pk):
        review = get_object_or_404(Review, id=pk)
        serializer = ReviewSerializer(review)

        return Response(serializer.data)


    def put(self, request, pk):
        review = get_object_or_404(Review, id=pk)
        serializer = ReviewSerializer(review, data = request.data)

        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def delete(self, request, pk):
        review = get_object_or_404(Review, id=pk)
        review.delete()

        return Response(status=204)
    