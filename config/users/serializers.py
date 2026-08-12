from rest_framework import serializers
from users.models import User

class UserSerializer(serializers.ModelSerializer):
    """
    custom user serializers
    """
    class Meta:
        model = User
        fields = [
            'id', 'email', 'phone_number', 'bio',
            'date_of_birth', 'image', 'role'
        ]