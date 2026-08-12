from django.urls import path
from orders.views import OrderListAPIView, OrderDetailAPIView, OrderItemDetailAPIView, OrderItemListAPIView

urlpatterns = [
    path('orders/', OrderListAPIView.as_view(), name = 'order-list'),
    path('orders/<uuid:pk>/', OrderDetailAPIView.as_view(), name = 'order-detail'),
    path('ordertems/', OrderItemListAPIView.as_view(), name = 'orderitems-list'),
    path('orderitems/<uuid:pk>/', OrderItemDetailAPIView.as_view(), name = 'orderitems-detail')
]
