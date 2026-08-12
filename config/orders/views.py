from rest_framework.views import APIView
from rest_framework.response import Response

from orders.models import Order, OrderItem
from orders.serializers import OrderSerializer, OrderItemSerializer

class OrderListAPIView(APIView):
    def get(self, request):
        orders = Order.objects.all()
        serilaizer = OrderSerializer(orders, many = True)

        return Response(request.data)

    def post(self, request):
        serializer = OrderSerializer(data = request.data)

        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data)
        return Response(serializer.errors)


class OrderDetailAPIView(APIView):
    def put(self, request, pk):
        order = Order.objects.get(id = pk)
        serializer = OrderSerializer(order, data=request.data)

        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data)
        return Response(serializer.errors)

    def delete(self, request, pk):
        order = Order.objects.get(id = pk)
        order.save()

        return Response(
            {
                'message': 'order deleted successfully'
            }
        )


class OrderItemListAPIView(APIView):
    def get(self, request):
        order_items = OrderItem.objects.all()
        serializer = OrderSerializer(order_items, many = True)

        return Response(serializer.data)

    def post(self, request):
        serializer = OrderItemSerializer(data = request.data)

        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data)
        return Response(serializer.errors)

class OrderItemDetailAPIView(APIView):
    def put(self, request, pk):
        order_item = OrderItem.objects.get(id = pk)
        serializer = OrderItemSerializer(order_item, data=request.data)

        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data)
        return Response(serializer.errors)

    def delete(self, request, pk):
        order_item = OrderItem.objects.get(id=pk)
        order_item.save()

        return Response(
            {
                'message': 'Order item deleted successfully'
            }
        )
