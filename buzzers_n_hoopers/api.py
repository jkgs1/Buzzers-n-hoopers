from django.urls import path, include

import rest_framework.urls

import clubber.api
import common.api
import matchup.api

app_name = 'api'
urlpatterns = [
    path('', include(common.api, namespace='common')),
    path('clubber/', include(clubber.api, namespace='clubber')),
    path('matchup/', include(matchup.api, namespace='matchup')),
]
