from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import *

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
    
    def create(self, validated_data):
        return User.objects.create(**validated_data)

class CalendarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Calendar
        fields = '__all__'
    
    def create(self, validated_data):
        return Calendar.objects.create(**validated_data)

class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = '__all__'
    
    def create(self, validated_data):
        return Event.objects.create(**validated_data)


class InvitesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Invites
        fields = '__all__'

    def create(self, validated_data):
        return Invites.objects.create(**validated_data)