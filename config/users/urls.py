from django.urls import path
from users.views import (UserListAPIView, UserDetailAPIView, UserRegisterAPIView)


urlpatterns = [
    path('users/register/', UserRegisterAPIView.as_view(), name='user-register'),

    path('users/', UserListAPIView.as_view(), name = 'user-list'),
    path('users/<uuid:pk>/', UserDetailAPIView.as_view(), name = 'user-detail')
]
