from django.db import models
from clubber.models import Team 
from clubber.models import Player 
from common.models import User
# Create your models here.

class Match(models.Model):
    # Support for series yet to be implemented 
    #  seriesId = models.ForeignKey(Series, null=True, blank=True)
    homeTeamId = models.ForeignKey(Team, null=False)
    awayTeamId = models.ForeignKey(Team, null=False)
    events = models.ManyToManyField(Event)

class Event(models.Model):
    match = models.ForeignKey(Match, on_delete=models.SET_NULL, null=False)
    player1 = models.ForeignKey(MatchPlayer)
    player2 = models.ForeignKey(MatchPlayer)
    EVENT_TYPE = [
        ("1P", "1 Point"),
        ("2P", "2 Points"),
        ("3P", "3 Points"),
        ("FP", "Personal foul"),
        ("FO", "Other foul"),
        ("EX", "Exchange"),
        ("TO", "Timeout")
        ]

class MatchPlayer(models.Model):
    match = models.ForeignKey(Match)
    player = models.ForeignKey(Player, null=True, blank=True)
    team = models.ForeignKey(Team, null=True, blank=True)

class MatchAdmin(models.Model):
    user = models.ForeignKey(User)
    match = models.OneToOneField(Match)
    PERMISSIONS = [
    
            ]
    
