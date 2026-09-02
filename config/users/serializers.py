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


class UserRegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        write_only = True,
        required = True,
        style = {'input_type': 'password'}
    )

    class Meta:
        model = User
        fields = ['id', 'email', 'name', 'password', 'role']

    def create(self, validated_data):
        user = User.objects.create_user( 
        email=validated_data['email'],
        username = validated_data['name'],
        password=validated_data['password'],
        role = validated_data.get('role', 'CUSTOMER'))

        return user
    