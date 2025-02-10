from django.urls import path, include
from rest_framework import routers
from rest_framework_nested.routers import NestedSimpleRouter
from rest_framework.decorators import action

from .views import *

router = routers.DefaultRouter()
router.register('match', MatchViewSet)

match_router = NestedSimpleRouter(router, 'match', lookup='match')

match_router.register('events', EventViewSet, basename='match-events')
match_router.register('matchPlayer', MatchPlayerViewSet, basename='match-matchPlayer')
match_router.register('matchAdmin', MatchAdminViewSet, basename='match-matchAdmin')


app_name = 'matchup'
urlpatterns = [
    path('', include(router.urls)),    
    path('', include(match_router.urls)),    
]
