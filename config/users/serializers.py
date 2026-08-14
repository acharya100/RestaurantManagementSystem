from rest_framework import serializers
from users.models import User

class UserSerializer(serializers.ModelSerializer):
    """
    custom user serializers
    """
    class Meta:
        model = User
        fields = [
            'id', 'name', 'bio', 'role',
            'email', 'phone_number', 'address',
            'date_of_birth', 'image'
        ]