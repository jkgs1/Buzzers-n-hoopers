from rest_framework_nested import routers
from django.urls import include, path

from common import views

router = routers.DefaultRouter()
router.register('users', views.UserViewSet)
router.register('groups', views.GroupViewSet)
router.register('permissions', views.PermissionViewSet)

app_name = 'common'
urlpatterns = [
    path('', include(router.urls))
]