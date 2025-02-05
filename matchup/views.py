from django.shortcuts import render
from rest_framework import viewsets

from .models import *
from .serializers import *
# Create your views here.
class MatchViewSet(viewsets.ModelViewSet):
    queryset = Match.objects.all()
    serializer_class = MatchSerializer

class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer

class MatchPlayerViewSet(viewsets.ModelViewSet):
    queryset = MatchPlayer.objects.all()
    serializer_class = MatchPlayerSerializer

class MatchAdminViewSet(viewsets.ModelViewSet):
    queryset = MatchAdmin.objects.all()
    serializer_class = MatchAdminSerializer
