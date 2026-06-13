from django.contrib.auth import authenticate
from rest_framework import serializers



class LoginSerializer(serializers.Serializer):

    username = serializers.CharField()
    password=serializers.CharField()

    def validate(self,data):
        username=data.get('username')
        password=data.get('password')

        if username is None or password is None:
            raise serializers.ValidationError("username and password is required")

        user=authenticate(username=username,password=password)

        if user is None:
            raise serializers.ValidationError("Invalid credentials")

        data["user"]=user
        return data
