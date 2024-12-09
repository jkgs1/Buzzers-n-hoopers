from django.urls import path, include

import rest_framework.urls

import clubber.api
import common.api

app_name = 'api'
urlpatterns = [
    path('', include(common.api, namespace='common')),
    path('clubber/', include(clubber.api, namespace='clubber')),
]