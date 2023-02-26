from django.shortcuts import render
from .permissions import IsOwnerOrReadOnly
from rest_framework import generics, permissions
from .serializers import *
from .models import *



class UserList(generics.ListCreateAPIView):
    permission_classes = (IsOwnerOrReadOnly,)
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (permissions.IsAdminUser,)
    queryset = User.objects.all()
    serializer_class = UserSerializer

class CalendarList(generics.ListCreateAPIView):
    permission_classes = (IsOwnerOrReadOnly,)
    queryset = Calendar.objects.all()
    serializer_class = CalendarSerializer


class CalendarDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (permissions.IsAdminUser,)
    queryset = Calendar.objects.all()
    serializer_class = CalendarSerializer


class EventList(generics.ListCreateAPIView):
    permission_classes = (IsOwnerOrReadOnly,)
    queryset = Event.objects.all()
    serializer_class = EventSerializer


class EventDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (permissions.IsAdminUser,)
    queryset = Event.objects.all()
    serializer_class = EventSerializer


class InvitesList(generics.ListCreateAPIView):
    permission_classes = (IsOwnerOrReadOnly,)
    queryset = Invites.objects.all()
    serializer_class = InvitesSerializer


class InvitesDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (permissions.IsAdminUser,)
    queryset = Invites.objects.all()
    serializer_class = InvitesSerializer
