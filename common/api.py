from rest_framework_nested import routers
from django.urls import include, path

from common import views

router = routers.DefaultRouter()
router.register('users', views.UserViewSet)
router.register('groups', views.GroupViewSet)
router.register('permissions', views.PermissionViewSet)

from rest_framework.authtoken import views

app_name = 'common'
urlpatterns = [
    path('auth/', views.obtain_auth_token)
    path('', include(router.urls))
]