from django.contrib import admin

from clubber.models import Player, TeamPlayer, Team, Shirt, Club


# Register your models here.
@admin.register(Player)
class PlayerAdmin(admin.ModelAdmin):
    pass

@admin.register(TeamPlayer)
class TeamPlayerAdmin(admin.ModelAdmin):
    pass

@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    pass

@admin.register(Shirt)
class ShirtAdmin(admin.ModelAdmin):
    pass

@admin.register(Club)
class ClubAdmin(admin.ModelAdmin):
    pass
