from django.urls import path, include
from .views import *

urlpatterns = [
	path('users/',UserList.as_view()),
    path('users/<int:pk>/',UserDetail.as_view()),
    path('calendars/',CalendarList.as_view()),
    path('calendars/<int:pk>/',CalendarDetail.as_view()),
    path('events/',EventList.as_view()),
    path('events/<int:pk>/',EventDetail.as_view()),
    path('invites/',InvitesList.as_view()),
    path('invites/<int:pk>/',InvitesDetail.as_view()),
]