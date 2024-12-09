from colorfield.fields import ColorField
from django.db import models
from common.models import User

# Create your models here.
class Player(models.Model):
    user = models.OneToOneField(User, on_delete=models.SET_NULL, null=True, blank=True)
    givenName = models.CharField(max_length=64)
    surname = models.CharField(max_length=64)
    bio = models.TextField(blank=True, default="")
    portrait = models.ImageField(blank=True, null=True)
    anon = models.BooleanField(default=True)

class Club(models.Model):
    name = models.CharField(max_length=64)
    logo = models.ImageField(blank=True, null=True)
    description = models.TextField(blank=True, default="")

class TeamPlayer(models.Model):
    team = models.ForeignKey("Team", on_delete=models.CASCADE)
    player = models.ForeignKey("Player", on_delete=models.CASCADE)
    shirt = models.OneToOneField("Shirt", on_delete=models.CASCADE)
    number = models.IntegerField(null=True, blank=True)

class Team(models.Model):
    name = models.CharField(max_length=64)
    club = models.ForeignKey(Club, on_delete=models.SET_NULL, null=True, blank=True)
    logo = models.ImageField(blank=True, null=True)
    description = models.TextField(blank=True, default="")
    players = models.ManyToManyField(Player, through=TeamPlayer)

class Shirt(models.Model):
    name = models.CharField(max_length=64)
    col = ColorField()
    accent = ColorField()
    team = models.ForeignKey("Team", on_delete=models.CASCADE)
