from rest_framework import serializers
from .models import CustomUser
from rest_framework.authtoken.models import Token
from django.contrib.auth.hashers import make_password
from django.contrib.auth.password_validation import validate_password

class UserSerializer(serializers.ModelSerializer):
    confirm_password = serializers.CharField(write_only=True)
   
        
    class Meta:
        model = CustomUser
        fields = ["email", "password", "confirm_password","name","dob"]
        extra_kwargs = {"password": {"write_only": True}}

    def validate(self, data):
        if data["password"] != data["confirm_password"]:
            raise serializers.ValidationError("Passwords do not match")
        validate_password(data["password"])
        data.pop("confirm_password", None)
        return data
        
    def create(self, validated_data):
        validated_data['password'] = make_password(validated_data['password'])
        return super(UserSerializer, self).create(validated_data)