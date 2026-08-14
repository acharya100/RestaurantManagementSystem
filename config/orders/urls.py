from django.urls import path
from orders.views import OrderDetailAPIView, OrderListAPIView, OrderItemDetailAPIView, OrderItemListAPIView


urlpatterns = [
    path('orders/', OrderListAPIView.as_view(), name = 'order-list'),
    path('orders/<uuid:pk>/', OrderDetailAPIView.as_view(), name = 'order-detail'),
    path('orderitems/', OrderItemListAPIView.as_view(), name = 'orderitem-list'),
    path('orderitems/<uuid:pk>/', OrderItemDetailAPIView.as_view(), name = 'orderitem-detail')
]

