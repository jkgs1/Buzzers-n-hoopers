from django.urls import path, include
from rest_framework import routers
from rest_framework_nested.routers import NestedSimpleRouter

from .views import PlayerViewSet, TeamPlayerViewSet, ClubViewSet, TeamViewSet, ShirtViewSet

router = routers.DefaultRouter()
router.register('clubs', ClubViewSet, basename='clubs')
router.register('players', PlayerViewSet, basename='players')
router.register('teams', TeamViewSet, basename='teams')

club_router = NestedSimpleRouter(router, 'clubs', lookup='club')
club_router.register('teams', TeamViewSet, basename='club-teams')

team_router = NestedSimpleRouter(club_router, 'teams', lookup='team')
team_router.register('team_players', TeamPlayerViewSet, basename='team-players')
team_router.register('shirts', ShirtViewSet, basename='team-shirts')

app_name = 'clubber'
urlpatterns = [
    path('', include(router.urls)),
    path('', include(club_router.urls)),
    path('', include(team_router.urls)),
]