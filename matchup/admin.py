from django.contrib import admin
from matchup.models import Match, Event, MatchPlayer, MatchAdmin
# Register your models here.

@admin.register(Match)
class MatchAdmin(admin.ModelAdmin):
    pass

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    pass

@admin.register(MatchPlayer)
class MatchPlayerAdmin(admin.ModelAdmin):
    pass

#@admin.register(MatchAdmin)
#class MatchAdminAdmin(admin.ModelAdmin):
#    pass


