from django.urls import path
from users.views import UserListAPIView, UserDetailAPIView

urlpatterns = [
    path('users/', UserListAPIView.as_view(), name = 'user-list'),
    path('users/<uuid:pk>/', UserDetailAPIView.as_view(), name = 'user-detail')
]
