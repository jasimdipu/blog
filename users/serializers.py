from django.contrib.auth import get_user_model
from rest_framework import serializers
from django.contrib.auth.models import User
from django.conf import settings


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        exclude = ["password"]


class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(validated_data['username'], validated_data['email'], validated_data['password'])
        return user


# class UserRegisterSerializer(serializers.ModelSerializer):
#
#     email = serializers.EmailField(required=True)
#     username = serializers.CharField(required=True)
#     password = serializers.CharField(min_length=8, write_only=True)
#
#     class Meta:
#         model = settings.AUTH_USER_MODEL
#         fields = ('email', 'user_name', 'first_name')
#         extra_kwargs = {'password': {'write_only': True}}
