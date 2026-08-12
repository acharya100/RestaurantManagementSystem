from django.urls import path
from menu.views import MenuListAPIView, MenuDetailAPIView

urlpatterns = [
    path('menus/', MenuListAPIView.as_view(), name = 'menu-list'),
    path('menus/<uuid:pk>/', MenuDetailAPIView.as_view(), name = 'menu-detail')
]
