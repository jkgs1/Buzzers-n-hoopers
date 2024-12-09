from django.shortcuts import render
from rest_framework import viewsets

from .models import Player, TeamPlayer, Team, Shirt, Club
from .serializers import PlayerSerializer, TeamPlayerSerializer, TeamSerializer, ShirtSerializer, ClubSerializer


# Create your views here.
class PlayerViewSet(viewsets.ModelViewSet):
    queryset = Player.objects.all()
    serializer_class = PlayerSerializer

class TeamPlayerViewSet(viewsets.ModelViewSet):
    queryset = TeamPlayer.objects.all()
    serializer_class = TeamPlayerSerializer

class TeamViewSet(viewsets.ModelViewSet):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer

class ShirtViewSet(viewsets.ModelViewSet):
    queryset = Shirt.objects.all()
    serializer_class = ShirtSerializer

class ClubViewSet(viewsets.ModelViewSet):
    queryset = Club.objects.all()
    serializer_class = ClubSerializer
