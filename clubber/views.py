from django.shortcuts import render
from rest_framework import viewsets

from .models import Player, TeamPlayer, Team, Shirt, Club
from .serializers import PlayerSerializer, TeamPlayerSerializer, TeamSerializer, ShirtSerializer, ClubSerializer


# Create your views here.
class PlayerViewSet(viewsets.ModelViewSet):
    serializer_class = PlayerSerializer
    queryset = Player.objects.all()

class TeamViewSet(viewsets.ModelViewSet):
    serializer_class = TeamSerializer

    def get_queryset(self):
        if self.kwargs.get('club_pk'):
            return Team.objects.filter(club=self.kwargs['club_pk'])
        else:
            return Team.objects.all()

class TeamPlayerViewSet(viewsets.ModelViewSet):
    serializer_class = TeamPlayerSerializer

    def get_queryset(self):
        if self.kwargs.get('team_pk'):
            return TeamPlayer.objects.filter(team=self.kwargs['team_pk'])
        else:
            return TeamPlayer.objects.all()


class ShirtViewSet(viewsets.ModelViewSet):
    serializer_class = ShirtSerializer

    def get_queryset(self):
        if self.kwargs.get('team_pk'):
            return Shirt.objects.filter(team=self.kwargs['team_pk'])
        else:
            return Shirt.objects.all()

class ClubViewSet(viewsets.ModelViewSet):
    queryset = Club.objects.all()
    serializer_class = ClubSerializer
