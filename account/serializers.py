from rest_framework import serializers
from .models import *

class UserRegiterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['name', 'last_name', 'phone_number', 'password', 'email', 'photo']

    def create(self, validated_data):
        user = User(
            name=validated_data['name'],
            last_name=validated_data['last_name'],
            phone_number=validated_data['phone_number'],
            email=validated_data['email'],
            photo=validated_data['photo']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'name', 'last_name', 'phone_number', 'email', 'photo']