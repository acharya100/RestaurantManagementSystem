from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import get_object_or_404

from orders.models import Order, OrderItem
from orders.serializers import OrderSerializer, OrderItemSerializer


class OrderListAPIView(APIView):
    """
    custom order views for orderlistapiview
    """
    def get(self, request):
        orders = Order.objects.all()
        serializer = OrderSerializer(orders, many = True)

        return Response(serializer.data)

    def post(self, request):
        serializer = OrderSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


class OrderDetailAPIView(APIView):
    """
    custom order views for orderdetailapiview
    """
    def get(self, request, pk):
        order = get_object_or_404(Order, id=pk)
        serializer = OrderSerializer(order)

        return Response(serializer.data)

    
    def put(self, request, pk):
        order = get_object_or_404(Order, id=pk)
        serializer = OrderSerializer(order, data = request.data)

        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def delete(self, request, pk):
        order = get_object_or_404(Order, id=pk)
        order.delete()

        return Response(status = 204)


class OrderItemListAPIView(APIView):
    """
    custom order item views for orderlistapiview
    """
    def get(self, request):
        orderitems = OrderItem.objects.all()
        serializer = OrderItemSerializer(orderitems, many = True)

        return Response(serializer.data)

    def post(self, request):
        serializer = OrderItemSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

class OrderItemDetailAPIView(APIView):
    """
    custom order item views for orderdetailapiview
    """
    def get(self, request,pk):
        orderitem = get_object_or_404(OrderItem, id=pk)
        serializer = OrderItemSerializer(orderitem)

        return Response(serializer.data)


    def put(self, request, pk):
        orderitem = get_object_or_404(OrderItem, id=pk)
        serializer = OrderItemSerializer(orderitem, data = request.data)

        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def delete(self, request, pk):
        orderitem = get_object_or_404(OrderItem, id=pk)
        orderitem.delete()

        return Response(status = 204)