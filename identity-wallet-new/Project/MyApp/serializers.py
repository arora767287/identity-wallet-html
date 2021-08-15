from rest_framework import serializers
from .models import User
from django.contrib.auth import get_user_model


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'email')
    def create(self, validated_data):
        user = User.objects.create(**validated_data)
        #Find setting password
        user.save()
        return user
