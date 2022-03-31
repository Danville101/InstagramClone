from rest_framework import serializers
from django.contrib.auth import get_user_model



class UserProfileSerializer(serializers.ModelSerializer):
     """ Serializer for Usermodel"""
     class Meta:
          model = get_user_model()
          fields = ("email", "fullname", "username", "password")
          extra_kwargs = {
               "password": {"write_only": True, "min_length": 6}
          }
     
     def create(self, validated_data):
          
          return get_user_model().objects.create_user(**validated_data)