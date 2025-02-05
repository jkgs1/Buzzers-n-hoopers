from django.db import models
from clubber.models import Team 
from clubber.models import Player 
from common.models import User
# Create your models here.
class Match(models.Model):
    # Support for series yet to be implemented 
    #  seriesId = models.ForeignKey(Series, null=True, blank=True)
    homeTeamId = models.ForeignKey(Team, related_name='homeId', null=False, on_delete=models.CASCADE)
    awayTeamId = models.ForeignKey(Team, related_name='awayId', null=False, on_delete=models.CASCADE)
     

class Event(models.Model):
    match = models.ForeignKey(Match, null=False, blank=False, on_delete=models.CASCADE)
    player1 = models.ForeignKey("MatchPlayer", related_name='p1', on_delete=models.CASCADE)
    player2 = models.ForeignKey("MatchPlayer", related_name='p2', on_delete=models.CASCADE)
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
    match = models.ForeignKey(Match, on_delete=models.CASCADE)
    player = models.ForeignKey(Player, null=True, blank=True, on_delete=models.CASCADE)
    team = models.ForeignKey(Team, null=True, blank=True, on_delete=models.CASCADE)

class MatchAdmin(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    match = models.OneToOneField(Match, on_delete=models.CASCADE)
    PERMISSIONS = [
    
            ]
    
